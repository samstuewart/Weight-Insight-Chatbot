async function askBot() {
  const insight = document.getElementById("insight-text");
  const image = document.getElementById("chart-image");
  insight.innerText = "Loading...";
  image.src = "";

  try {
    const response = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ intent: "weight_trend" })
    });

    if (!response.ok) {
      const error = await response.json();
      insight.innerText = `❌ ${error.error || "Failed to get response"}`;
      return;
    }

    const data = await response.json();
    insight.innerText = data.insight;
    image.src = data.chart_url;

  } catch (err) {
    insight.innerText = `❌ Network or Server Error: ${err.message}`;
  }
}
