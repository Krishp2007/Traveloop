"""Core data models for the Traveloop travel planning application."""
import uuid
from decimal import Decimal

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class UserProfile(models.Model):
    """Optional user profile details shown on the profile screen."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)
    preferred_travel_style = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return f"Profile: {self.user.username}"


class Trip(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="trips",
    )
    title = models.CharField(max_length=180)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    cover_image = models.ImageField(upload_to="trip_covers/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    public_slug = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    is_public = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} ({self.user.username})"

    def get_absolute_url(self):
        return reverse("travel:trip_detail", kwargs={"trip_id": self.pk})

    @property
    def total_budget(self):
        if hasattr(self, "budget"):
            return self.budget.total_cost
        return Decimal("0.00")

    @property
    def total_days(self):
        days = (self.end_date - self.start_date).days + 1
        return max(days, 1)


class CityStop(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="city_stops")
    city_name = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ["order", "arrival_date"]
        unique_together = ("trip", "order")

    def __str__(self):
        return f"{self.city_name}, {self.country}"


class Activity(models.Model):
    CATEGORY_CHOICES = [
        ("sightseeing", "Sightseeing"),
        ("food", "Food"),
        ("adventure", "Adventure"),
        ("culture", "Culture"),
        ("shopping", "Shopping"),
        ("other", "Other"),
    ]

    city_stop = models.ForeignKey(CityStop, on_delete=models.CASCADE, related_name="activities")
    title = models.CharField(max_length=150)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default="other")
    description = models.TextField(blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    duration_hours = models.DecimalField(
        max_digits=5, decimal_places=2, default=1, validators=[MinValueValidator(0)]
    )
    activity_date = models.DateField()

    class Meta:
        ordering = ["activity_date", "city_stop__order"]

    def __str__(self):
        return f"{self.title} ({self.city_stop.city_name})"


class Budget(models.Model):
    trip = models.OneToOneField(Trip, on_delete=models.CASCADE, related_name="budget")
    transport_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    hotel_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    food_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    activity_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    miscellaneous_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    @property
    def total_cost(self):
        return (
            self.transport_cost
            + self.hotel_cost
            + self.food_cost
            + self.activity_cost
            + self.miscellaneous_cost
        )

    def __str__(self):
        return f"Budget for {self.trip.title}"


class PackingItem(models.Model):
    CATEGORY_CHOICES = [
        ("documents", "Documents"),
        ("clothing", "Clothing"),
        ("electronics", "Electronics"),
        ("toiletries", "Toiletries"),
        ("medicine", "Medicine"),
        ("other", "Other"),
    ]

    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="packing_items")
    item_name = models.CharField(max_length=120)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default="other")
    is_packed = models.BooleanField(default=False)

    class Meta:
        ordering = ["category", "item_name"]

    def __str__(self):
        return self.item_name


class Note(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
