from dataclasses import dataclass
from pickle import NONE
import random

from typing import Optional

from fastapi import HTTPException, Response,status
from fastapi import Body, FastAPI
from pydantic import BaseModel

app=FastAPI()
class Post(BaseModel):
  title:str
  content:str
  published:bool=True
  rating:Optional[int]=None
my_posts=[{'title':'title of post 1','content':"Content of post 1","id":1},
          {'title':'title of post 1','content':"Content of post 2","id":2}]
@app.get("/")
def root():
    return {"message":"Welcome to  !!!! my api"}
@app.get("/post")
def get_posts():
    return {"data":my_posts}
@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(post:Post):
  post_dict=post.dict()
  post_dict['id']=random.randint(0,1000000)
  my_posts.append(post_dict)
  return(post_dict)
@app.get("/posts/{id}")
def get_post(id:int,response:Response):
  print(id)
  post=find_post(id)
  print(post)
  if post is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Post of {id } not found")
       
  return post

@app.delete("/posts/{id}")
def delete_post(id:int):
  index=find_index(id)
  print(index)
  if index is None:
    HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")
  my_posts.pop(index)
  return Response(status_code=status.HTTP_200_OK)
@app.put("/posts/{id}")
def update_post(id:int,post:Post):
  index=find_index(id)
  if index is None:
    HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")
  post=post.dict()
  my_posts[index]["title"]=post['title']
  my_posts[index]['content']=post['content']
  return Response(status_code=status.HTTP_200_OK)
  
  
  

def find_index(id:int):
  return next((idx for idx, data in enumerate(my_posts) if data["id"]==id), None)  
def find_post(id:int):
  return next((data for data in my_posts if data["id"]==id), None)
       
