import uvicorn  # type:ignore
from api import app  # Import FastAPI instance

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
