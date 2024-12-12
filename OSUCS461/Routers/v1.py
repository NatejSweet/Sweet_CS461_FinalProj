from fastapi import APIRouter, FastAPI
from Models import WriteUser, ReadUser, WriteUserPost, ReadUserPost, UpdateUser
from Classes.Database import UserLogic, UserPostLogic
from fastapi import HTTPException
from fastapi.responses import JSONResponse


app = FastAPI()


router = APIRouter()

@router.get("/users")
async def read_users():
    users = UserLogic.read()
    # print(users)
    if users:
        return users
    else:
        raise HTTPException(status_code=404, detail="Users not found")

@router.get("/users/{user_id}")
async def read_user(user_id: str):
    user = UserLogic.read(user_id)
    print(user)
    if user:
        return user
    else:   
        raise HTTPException(status_code=404, detail="User not found")

@router.post("/users")
async def write_user(user : WriteUser):
    try:
        uuid = UserLogic.write(user.name, user.time_created)
        user = UserLogic.read(uuid)
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
    
@router.put("/users/{user_id}")
async def update_user(user_id: str, user: UpdateUser):
    name = user.name
    user = UserLogic.update(user_id, name)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router.delete("/users/{user_id}")
async def delete_user(user_id: str):
    res = UserLogic.delete(user_id)
    if res:
        return JSONResponse(status_code=200, content={"message": "User deleted"})
    else:
        raise HTTPException(status_code=404, detail="User not found")
    
@router.get("/posts")
async def read_posts():
    res = UserPostLogic.read()
    if res:
        return res
    else:
        raise HTTPException(status_code=404, detail="Posts not found")

@router.get("/posts/{post_id}")
async def read_post(post_id: str):
    res = UserPostLogic.read(post_id)
    if res:
        return res
    else:
        raise HTTPException(status_code=404, detail="Post not found")

@router.post("/posts")
async def write_post(post : WriteUserPost):
    res = UserPostLogic.write(post.user_uuid, post.post_9char, post.text, post.time_created)
    if res:
        return res
    else:
        raise HTTPException(status_code=404, detail="Failed to write post")
    
@router.put("/posts/{post_id}")
async def update_post(post_id: str, post: WriteUserPost):
    text = post.text
    res = UserPostLogic.update(post_id, text)
    if res:
        return res
    else:
        raise HTTPException(status_code=404, detail="Failed to update post")

@router.delete("/posts/{post_id}")
async def delete_post(post_id: str):
    res = UserPostLogic.delete(post_id)
    if res:
        return JSONResponse(status_code=200, content={"message": "Post deleted"})
    else:
        raise HTTPException(status_code=404, detail="Post not found")

@router.get("/users/{user_id}/posts")
async def read_user_posts(user_id: str):
    res = UserPostLogic.readUserPosts(user_id)
    if res:
        return res
    else:
        raise HTTPException(status_code=404, detail="Posts not found")



app.include_router(router, prefix="/v1")