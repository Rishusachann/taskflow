from fastapi import FastAPI

app = FastAPI(title="TaskFlow API")


@app.get("/")
def root():
    return {
        "application": "TaskFlow",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }