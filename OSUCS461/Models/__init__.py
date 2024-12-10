from pydantic import BaseModel


class BasePydanticModel(BaseModel):
    class Config:
        from_attributes = False
        validate_assignment = True


# User Models
class WriteUser(BasePydanticModel):
    name: str 
    time_created: int


class ReadUser(WriteUser):
    uuid: str

# UserPost Models
class WriteUserPost(BasePydanticModel):
    user_uuid: str 
    post_9char: str
    text: str
    time_created: int



class ReadUserPost(WriteUserPost):
    uuid: str
