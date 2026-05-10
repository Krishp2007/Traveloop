(function () {
  const payload = window.traveloopBudgetData;
  if (!payload) return;

  const labels = payload.labels || [];
  const values = payload.values || [];

  const pieCtx = document.getElementById("budgetPie");
  const barCtx = document.getElementById("budgetBar");
  if (!pieCtx || !barCtx) return;

  const colors = ["#0ea5e9", "#8b5cf6", "#f59e0b", "#10b981", "#f43f5e"];

  new Chart(pieCtx, {
    type: "pie",
    data: { labels, datasets: [{ data: values, backgroundColor: colors }] },
    options: { plugins: { legend: { labels: { color: "#e2e8f0" } } } },
  });

  new Chart(barCtx, {
    type: "bar",
    data: { labels, datasets: [{ label: "USD", data: values, backgroundColor: colors }] },
    options: {
      scales: {
        x: { ticks: { color: "#e2e8f0" }, grid: { color: "rgba(226,232,240,0.1)" } },
        y: { ticks: { color: "#e2e8f0" }, grid: { color: "rgba(226,232,240,0.1)" } },
      },
      plugins: { legend: { labels: { color: "#e2e8f0" } } },
    },
  });
})();
