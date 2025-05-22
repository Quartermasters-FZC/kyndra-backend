from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routes import ai  # this imports your LangChain-powered AI route

# Load .env variables (like OPENAI_API_KEY)
load_dotenv()

app = FastAPI()

# Allow CORS from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route registration
app.include_router(ai.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Kyndra Backend API"}
