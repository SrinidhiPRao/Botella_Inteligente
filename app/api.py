from fastapi import FastAPI  # type:ignore
from fastapi.middleware.cors import CORSMiddleware  # type:ignore

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/data")
def get_data():
    """Returns time-series water intake data as JSON."""
    return {
        "labels": ["08:00", "10:00", "12:00", "14:00", "16:00"],
        "datasets": [
            {
                "label": "Water Intake",
                "data": [250, 300, 200, 400, 350],
                "borderColor": "blue",
                "fill": False,
            }
        ],
    }
