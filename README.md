# Weight Insight Chatbot

A lightweight chatbot web application that provides personalized weight trend insights using natural language and displays visual charts using Highcharts.

## Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python with FastAPI  
- **LLM Integration:** LLaMA 3 via Ollama  
- **Charting:** Highcharts (converted to image)  
- **Data Source:** Simulated mock weight data  

## Features

- Simple and clean chatbot interface for querying weight trends  
- Backend uses LLaMA 3 to generate intelligent health insights  
- Highcharts is used to create visual trend charts based on weight data  
- FastAPI handles communication between frontend and backend  
- The application provides a fully responsive UI  

## Workflow

1. User clicks a button on the frontend to request a weight trend insight  
2. A request is sent to the backend with the intent  
3. The backend loads mock weight data  
4. LLaMA 3 (via Ollama) generates a natural language insight  
5. Highcharts generates a weight trend chart, which is saved as an image  
6. The backend returns the chart image path and insight  
7. The frontend displays both in a user-friendly layout  

## Example Output

- **Insight:** “Your weight has remained stable over the past few weeks with minor fluctuations.”  
- **Chart:** Displayed using Highcharts, rendered as an image  

## Local Setup

- Requires Python 3.10+, FastAPI, and Ollama with LLaMA 3 model  
- LLaMA 3 must be running as a local service via Ollama  
- Backend serves the `/chat` endpoint to accept intent requests  
- Frontend uses plain HTML, CSS, and JavaScript, and can be opened directly in a browser  

## Deployment

- Backend can be deployed using Uvicorn or Gunicorn  
- Frontend is static and can be hosted on platforms like GitHub Pages or Netlify  

## License

This project is licensed under the MIT License. You’re free to use, modify, and share with credit.

## Acknowledgements

- **Ollama** for local LLaMA model integration  
- **Highcharts** for elegant chart visualizations  
- **FastAPI** for building a modern, async backend  
