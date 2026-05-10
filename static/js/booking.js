/**
 * Live total for booking page: travelers × package price per person.
 */
(function () {
  const travelersEl = document.getElementById("id_travelers_count");
  const totalEl = document.getElementById("booking-total");
  const ppp = document.getElementById("booking-ppp");

  function fmt(n) {
    const num = Number(n);
    return num.toLocaleString('en-IN', {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2,
    });
  }

  function recalc() {
    if (!travelersEl || !totalEl || !ppp) return;
    const t = Number(travelersEl.value || 1);
    const unit = Number(ppp.textContent);
    if (!Number.isFinite(unit)) return;
    totalEl.textContent = fmt(unit * Math.max(t, 1));
  }

  if (travelersEl) travelersEl.addEventListener("input", recalc);
  recalc();
})();
