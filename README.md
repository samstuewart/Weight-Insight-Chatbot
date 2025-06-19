# 💬 Weight Insight Chatbot

A lightweight chatbot web application that provides personalized weight trend insights using natural language and generates dynamic charts using Highcharts.

---

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Charting Library:** Highcharts  
- **Backend:** Python, FastAPI  
- **LLM Integration:** LLaMA 3 via Ollama  
- **Data Source:** Mock weight data  
- **Image Generation:** Chart converted to image from Highcharts  

---

## Features

- Natural language chatbot for weight insight queries  
- LLaMA 3 used for generating textual insights  
- Highcharts used for dynamic chart rendering  
- Clean and responsive user interface  
- Frontend-backend communication via REST API  

---

## How to Run the Project

### 1. Install Python Dependencies

Make sure you have **Python 3.10+** and **Ollama** installed.

```bash
pip install fastapi uvicorn python-multipart
2. Install and Run Ollama
Download the model and start the LLM server:

bash
Copy
Edit
ollama pull llama3
ollama run llama3
⚠️ Keep this running in a separate terminal.

3. Start Backend Server
bash
Copy
Edit
cd backend
uvicorn main:app --reload
Backend runs at: http://localhost:8000

4. Open the Frontend
Open the frontend/index.html file directly in your browser.
Click the "Show Weight Trend" button to fetch the insight and chart.

💡 How It Works
User clicks the "Show Weight Trend" button

Frontend sends POST request with { intent: "weight_trend" } to /chat endpoint

Backend loads mock weight data and calls LLaMA 3 to generate insight

A chart is created using Highcharts, converted to image, and returned

Frontend displays the insight text and the generated chart image

📸 Example Output
🧠 Insight: "Your weight trend has been stable over the past 30 days with slight fluctuations."
📈 Chart: Rendered with Highcharts and embedded as an image

📦 Deployment
Backend: Can be deployed using Uvicorn or Gunicorn behind a reverse proxy

Frontend: Static HTML, easily hostable via GitHub Pages, Netlify, Vercel, etc.

📝 License
MIT License. Feel free to use, modify, and distribute with credit.

🙌 Acknowledgements
Ollama — for running LLaMA 3 models locally

Highcharts — for rich chart rendering

FastAPI — for the async Python backend



---

