from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
import pytz

app = FastAPI()

@app.get("/")
def fetch_info():
    return {
        "email": "elijahosas@gmail.com",  
        "current_datetime": datetime.now(pytz.utc).replace(microsecond=0).isoformat(),
        "github_url": "hhttps://github.com/elijahkato/hng12_project0.git" 
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)