from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

BASE_DIR = Path(__file__).parent



app = FastAPI(
    title="Vercel + FastAPI",
    description="Vercel + FastAPI",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class SurveyEntry(BaseModel):
    favoriteColor: str  # must match the key your JS sends in JSON.stringify




@app.get("/", response_class=HTMLResponse)
def root():
    return (BASE_DIR / "index.html").read_text()


users = []

@app.post("/survey")
def survey(entry: SurveyEntry):
    # Convert the Pydantic model into a plain Python dict so it's easy to store
    # .model_dump() is the Pydantic v2 method (use .dict() if on Pydantic v1)
    new_user = entry.model_dump()
    
    # Append the dict to our in-memory list — this is the "add to db" step
    users.append(new_user)
        
    # Return a response so the frontend knows it worked
    # FastAPI auto-converts this dict to JSON
    return {"status": "ok", "total_responses": len(users)}




# Bonus: a GET route to actually SEE what's been collected
@app.get("/responses")
def get_responses():
    return {"users": users}
    
   
    





if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5001, reload=True)
