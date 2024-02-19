from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
def root():
    return {"message":"Hello World"}

@app.get("/posts")
def get_posts():
    return {"data":"This is your post"}

@app.post("/posts")
def create_post(post: Post):
    print(post)
    print(post.model_dump())
    return {"data":post}