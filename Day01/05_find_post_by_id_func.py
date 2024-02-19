from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from random import randrange
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


def find_post(id):
    for p in my_posts:
        if p['id'] ==id:
            return p


@app.get("/")
def root():
    return {"message":"Hello World"}

@app.get("/posts")
def get_posts():
    return {"data":my_posts}

@app.post("/posts")
def create_post(post: Post):
    # print(post)
    # print(post.model_dump())
    post_dict=post.model_dump()
    post_dict["id"] =randrange(0,1000000)
    my_posts.append(post_dict)
    return {"data":post_dict}

@app.get("/posts/{id}")
def get_post(id:int):
    print(id)
    post = find_post(id)
    return {"post details":post}
