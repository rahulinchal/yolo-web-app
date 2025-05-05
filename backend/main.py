from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from datetime import datetime
import uuid

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (change in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple database (in memory)
projects_db = {}

@app.get("/")
def read_root():
    return {"message": "YOLO Backend is running"}

@app.post("/projects")
async def create_project(name: str, description: str = "", task_type: str = "detection"):
    project_id = str(uuid.uuid4())
    project = {
        "id": project_id,
        "name": name,
        "description": description,
        "task_type": task_type,
        "created_at": datetime.now().isoformat(),
        "datasets": [],
        "models": []
    }
    projects_db[project_id] = project
    return project

@app.get("/projects")
async def get_projects():
    return list(projects_db.values())

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Create uploads directory if it doesn't exist
    os.makedirs("uploads", exist_ok=True)
    
    # Save file
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    
    return {"filename": file.filename, "path": file_path}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

from ultralytics import YOLO
import shutil

@app.post("/train")
async def train_model():
    # This is a very basic example
    model = YOLO("yolov8n.pt")  # Load a pretrained model
    
    # Train the model (you'll need a proper dataset)
    results = model.train(
        data="coco128.yaml",  # Example dataset config
        epochs=3,
        imgsz=640
    )
    
    # Return training results
    return {
        "status": "completed",
        "metrics": results.results_dict
    }