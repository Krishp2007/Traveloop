/**
 * Shared UI helpers: navbar scroll shadow, testimonials auto-advance fallback.
 */
(function () {
  const nav = document.getElementById("main-navbar");
  if (nav) {
    const onScroll = () => {
      if (window.scrollY > 10) nav.classList.add("shadow");
      else nav.classList.remove("shadow");
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /** Simple carousel for testimonials if Bootstrap JS not loaded yet */
  const slides = document.querySelectorAll("[data-ts-slide]");
  if (slides.length > 1) {
    let i = 0;
    window.setInterval(() => {
      i = (i + 1) % slides.length;
      slides.forEach((el, idx) => {
        el.classList.toggle("opacity-100", idx === i);
        el.classList.toggle("opacity-0", idx !== i);
      });
    }, 5200);
  }
})();
