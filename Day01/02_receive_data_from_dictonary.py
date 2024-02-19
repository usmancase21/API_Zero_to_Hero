from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [
    {"title": "My First Post","content": "This is the content of my first post","id":1,},
    {"title": "My Second Post","content": "This is the content of my second post","id":2,},
]

@app.get("/")
def root():
    return {"message":"Hello World"}

@app.get("/posts")
def get_posts():
    return {"data":my_posts}

@app.post("/posts")
def create_post(post: Post):
    print(post)
    print(post.model_dump())
    return {"data":post}