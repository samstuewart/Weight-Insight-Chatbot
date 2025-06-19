import subprocess

def generate_insight(intent, data):
    if intent == "weight_trend":
        prompt = f"""
Analyze this weight trend:
Months: {', '.join(data['months'])}
Weights: {', '.join(map(str, data['weights']))}
Goal: {data['goal_weight']}

Respond with 2-3 sentences summarizing the progress.
"""
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=120  # prevent infinite hang
    )
    return result.stdout.decode().strip()
