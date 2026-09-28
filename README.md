# HealthInfo AI

HealthInfo AI is a Python-based Generative AI application that provides an API interface for interacting with Google's Gemini AI model. The project demonstrates how Generative AI can be integrated into a practical application using FastAPI and REST APIs.

## Features

* REST API built with FastAPI
* Integration with Google Gemini API
* AI-powered question-and-answer functionality
* Request validation using Pydantic
* Environment-variable based API key configuration
* Interactive API documentation through FastAPI/Swagger

## Technologies

* Python
* FastAPI
* Google Gemini API
* Pydantic
* python-dotenv
* Uvicorn

## How It Works

1. A user submits a question to the `/ask` API endpoint.
2. FastAPI validates the request.
3. The application sends the question to the Gemini API.
4. Gemini generates an AI response.
5. The API returns the response to the user.

## API Endpoint

### POST `/ask`

Example request:

```json
{
  "question": "What are the symptoms of malaria?"
}
```

The API processes the question and returns an AI-generated response.

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/alakebally/HealthInfo-AI.git
cd HealthInfo-AI
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Do not commit your `.env` file or expose your API key publicly.

### 5. Start the API

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## Project Purpose

This project was developed to gain practical experience integrating Generative AI into software applications and to strengthen skills in Python, API development, AI services, and backend application development.

## Future Improvements

* Add conversation history
* Add authentication and authorization
* Improve error handling
* Add automated testing
* Deploy the API to a cloud platform
* Add a frontend interface
* Explore additional AI-powered healthcare information features

## Disclaimer

HealthInfo AI is a learning and software-development project. It is not a substitute for professional medical advice, diagnosis, or treatment.
