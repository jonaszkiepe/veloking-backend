import uvicorn
from decouple import config

if __name__ == "__main__":
    uvicorn.run("app.api:app", host="localhost", port=8080, reload=True)
