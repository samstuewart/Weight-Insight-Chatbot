import requests
import uuid

def build_chart_config(intent, data):
    if intent == "weight_trend":
        return {
            "infile": {
                "chart": {"type": "line"},
                "title": {"text": "Weight Trend Over Months"},
                "xAxis": {"categories": data["months"]},
                "yAxis": {"title": {"text": "Weight (kg)"}},
                "series": [{"name": "Weight", "data": data["weights"]}]
            },
            "type": "image/png"
        }

def export_chart(config, intent):
    file_name = f"{intent}_{uuid.uuid4().hex[:8]}.png"
    res = requests.post("http://localhost:7801", json=config)
    res.raise_for_status()
    with open(f"./static/{file_name}", "wb") as f:
        f.write(res.content)
    return file_name
