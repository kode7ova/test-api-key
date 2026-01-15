# Import FastAPI, Unicorn, os
from fastapi import FastAPI, Header, HTTPException
import uvicorn
import os

# Create FastAPI, get API key
app = FastAPI()
API_KEY = os.getenv("API_KEY")

# Defining endpoint, API key check
@app.get("/protected")
def protected_endpoint(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return {"secret": "ok"}

# Run Uvicorn server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
