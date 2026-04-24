from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/hello")
def hello():
    return {"message": "hello its working"}


class SurveyEntry(BaseModel):
    favoriteColor: str


users = []

@app.post("/api/survey")
def survey(entry: SurveyEntry):
    users.append(entry.model_dump())
    return {"status": "ok", "total_responses": len(users)}


@app.get("/api/responses")
def get_responses():
    return {"users": users}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("index:app", host="0.0.0.0", port=5001, reload=True)
