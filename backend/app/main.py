from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os
from typing import Optional

app = FastAPI()

# Set up the directory to store uploaded files temporarily
UPLOAD_DIR = "./uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Route to upload image and other parameters
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), prompt: Optional[str] = None, params: Optional[str] = None):
    try:
        # Save file temporarily
        file_location = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_location, "wb") as f:
            f.write(await file.read())
        
        return JSONResponse(content={"filename": file.filename, "prompt": prompt, "params": params}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

# Root route for testing the server
@app.get("/")
async def root():
    return {"message": "FastAPI Backend Running"}
