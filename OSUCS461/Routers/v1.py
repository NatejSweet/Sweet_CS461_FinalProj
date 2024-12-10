from fastapi import APIRouter, FastAPI
from Models import WriteUser, ReadUser, WriteUserPost, ReadUserPost
from Classes.Database import UserLogic, UserPostLogic
from fastapi import HTTPException


app = FastAPI()


router = APIRouter()

@router.get("/users")
async def read_users():
    users = UserLogic.read()
    if users:
        return users
    else:
        raise HTTPException(status_code=404, detail="Users not found")

@router.get("/users/{user_id}")
async def read_user(user_id: int):
    user = UserLogic.read(user_id)
    if user:
        return user
    else:   
        raise HTTPException(status_code=404, detail="User not found")

@router.post("/users")
async def write_user(user : WriteUser):
    # try:
        uuid = UserLogic.write(user.username, user.time_created)
        user = UserLogic.read(uuid)
        return user
    # except Exception as e:
        # raise HTTPException(status_code=500, detail=e)
    
@router.put("/users/{user_id}")
async def update_user(user_id: int, username: str):
    UserLogic.update(user_id, username)

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    UserLogic.delete(user_id)
    

@router.get("posts")
async def read_posts():
    UserPostLogic.read()

@router.get("posts/{post_id}")
async def read_post(post_id: int):
    UserPostLogic.read(post_id)

@router.post("posts")
async def write_post(post : WriteUserPost):
    UserPostLogic.write(post.user_uuid, post.post_9char, post.text, post.time_created)
    
@router.put("posts/{post_id}")
async def update_post(post_id: int, text: str):
    UserPostLogic.update(post_id, text)

@router.delete("posts/{post_id}")
async def delete_post(post_id: int):
    UserPostLogic.delete(post_id)

@router.get("users/{user_id}/posts")
async def read_user_posts(user_id: int):
    UserPostLogic.readUserPosts(user_id)



app.include_router(router, prefix="/v1")