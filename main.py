from fastapi import FastAPI

app = FastAPI(
    title= "RAG Document Assistant",
    description= "Ask questions about your documents using AI",
)

app.get("/")
def home():
    return {
        "message": "RAG Document Assistant is running",
        "status" : "success",
    }

app.get("/health")
def health_check():
    return {"status": "healthy"}