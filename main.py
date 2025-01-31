from fastapi import FastAPI
from datetime import datetime, timezone
from fastapi.middleware.cors import CORSMiddleware
import pytz

app = FastAPI()

@app.get("/")
def fetch_info():
    return {
        "email": "elijahosas@gmail.com",  
        "current_datetime": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "github_url": "https://github.com/elijahkato/hng12_project0" 
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
