import random
from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel
app=FastAPI()
class Post(BaseModel):
  title:str
  content:str
  published:bool=True
  rating:Optional[int]=None
my_posts=[{'title':'title of post 1','content':"Content of post 1","id":1}]
@app.get("/")
async def root():
    return {"message":"Welcome to  !!!! my api"}
@app.get("/post")
def get_post():
    return {"data":my_posts}
@app.post("/posts")
def create_post(post:Post):
  post_dict=post.dict()
  post_dict['id']=random.randint(0,1000000)
  my_posts.append(post_dict)
  return(post_dict)
