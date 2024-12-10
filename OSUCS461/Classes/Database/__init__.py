from OSUCS461.Config import MySQL as DatabaseConfig
from OSUCS461.ThirdParty.MySQL import MySQL
from Models import WriteUser, WriteUserPost, ReadUser, ReadUserPost
import hashlib
DB = MySQL(**DatabaseConfig)

class UserLogic:
    def generate_uuid(name: str, time_created: int):
        return hashlib.md5((name+str(time_created)).encode()).hexdigest()
    @staticmethod
    def write(name: str = None, time_created: int = None):
        user = WriteUser(name = name, time_created = time_created)
        uuid = UserLogic.generate_uuid(user.name, user.time_created)
        query = f"insert INTO user (name, time_created, uuid) VALUES ('{user.name}', {user.time_created}, '{uuid}')"
        res = DB.query(query)
        if res:
            query = f"SELECT * FROM user WHERE uuid = '{uuid}'"
            user = DB.get_row(query)
            return ReadUser(uuid=user.get('uuid'), name=user.get('name'), time_created=user.get('time_created'))
        else:
            return None
    @staticmethod
    def read(uuid: str = None):
        if uuid:
            query = f"SELECT * FROM user WHERE uuid = '{uuid}'"
            return DB.get_row(query)
        else:
            query = f"SELECT * FROM user"
            return DB.get_results(query)
        
    @staticmethod
    def delete(uuid: str):
        query = f"delete FROM user WHERE uuid = '{uuid}'"
        res = DB.query(query)
        if res.get('affected_rows') > 0:
            return True
        else:
            return None

    @staticmethod
    def update(uuid: str, name: str):
        if name:
            query = f"UPDATE user SET name = '{name}' WHERE uuid = '{uuid}'"
            DB.run(query)
            user_updated = UserLogic.read_one(uuid)
            if user_updated and user_updated.name == name:
                return user_updated
            else:
                return None
            
class UserPostLogic:
    def generate_uuid(user_uuid: str, post_9char: str, time_created: int):
        return hashlib.md5((user_uuid+post_9char+str(time_created)).encode()).hexdigest()
    @staticmethod
    def write(user_uuid : str = None, post_9char: str = None, text: str = None, time_created: int = None):
        uuid = UserPostLogic.generate_uuid(user_uuid, post_9char, time_created)
        user_post = WriteUserPost(user_uuid = user_uuid, post_9char = post_9char, text = text, time_created = time_created)
        query = f"insert INTO user_post (user_uuid, post_9char, text, time_created, uuid) VALUES ('{user_post.user_uuid}', '{user_post.post_9char}', '{user_post.text}', '{user_post.time_created}', '{uuid}')"
        res = DB.query(query)
        if res:
            query = f"SELECT * FROM user_post WHERE uuid = '{uuid}'"
            user_post = DB.get_row(query)
            return ReadUserPost(uuid=user_post.get('uuid'), user_uuid=user_post.get('user_uuid'), post_9char=user_post.get('post_9char'), text=user_post.get('text'), time_created=user_post.get('time_created'))
        else:
            return None

    @staticmethod
    def read(uuid: str = None):
        if uuid:
            query = f"SELECT * FROM user_post WHERE uuid = '{uuid}'"
            return DB.get_row(query)
        else:
            query = f"SELECT * FROM user_post"
            return DB.get_results(query)
    
    @staticmethod
    def delete(uuid: str):
        query = f"delete FROM user_post WHERE uuid = '{uuid}'"
        res  = DB.query(query)
        print(res)
        if res.get('affected_rows') > 0:
            return True
        else:
            return None
    
    @staticmethod
    def update(uuid: str, text: str):
        if text:
            query = f"UPDATE user_post SET text = '{text}' WHERE uuid = '{uuid}'"
            DB.run(query)
            user_post_updated = UserPostLogic.read(uuid)
            if user_post_updated and user_post_updated.get('text') == text:
                return user_post_updated
            else:
                return None

    @staticmethod
    def readUserPosts(user_uuid: str):
        query = f"SELECT * FROM user_post WHERE user_uuid = '{user_uuid}'"
        return DB.get_results(query)