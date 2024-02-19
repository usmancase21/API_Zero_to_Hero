# Step 1 Import Libraries
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from random import randrange
app = FastAPI()

# Step 2 Pydantic Class Validation
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
# Step 3 Creating Dummy Database , hardcoded Values
my_posts = [
    {"title": "My First Post","content": "This is the content of my first post","id":1,},
    {"title": "My Second Post","content": "This is the content of my second post","id":2,},
]

# Step 6.1 Getting id of each user and passign to Get 
def find_post(id):
    for p in my_posts:
        if p['id'] ==id:
            return p
# Step 4 Creating Get Routes with / and /posts
@app.get("/")
def root():
    return {"message":"Hello World"}

@app.get("/posts")
def get_posts():
    return {"data":my_posts}
# Step 5 Creating Post to Send Dummy Database 
@app.post("/posts")
def create_post(post: Post):
    # print(post)
    # print(post.model_dump())
    post_dict=post.model_dump()
    post_dict["id"] =randrange(0,1000000)
    my_posts.append(post_dict)
    return {"data":post_dict}
# Step # 6 Getting Data by Matching id with Dummy Database 
@app.get("/posts/{id}")
def get_post(id:int):
    print(id)
    post = find_post(id)
    return {"post details":post}
