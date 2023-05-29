from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel
app=FastAPI()
class Post(BaseModel):
  title:str
  content:str
  published:bool=True
  rating:Optional[int]=None

@app.get("/")
async def root():
    return {"message":"Welcome to  !!!! my api"}
@app.get("/post")
def get_post():
    return {"id":"Sachin",
            "data":"This is your post"}
@app.post("/create-post")
def create_post(pay_load:Post):
    print(pay_load.dict())
    