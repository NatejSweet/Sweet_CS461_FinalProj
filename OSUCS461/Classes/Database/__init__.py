from OSUCS461.Config import MySQL as DatabaseConfig
from OSUCS461.ThirdParty.MySQL import MySQL
from Models import WriteUser, WriteUserPost

DB = MySQL(**DatabaseConfig)

class UserLogic:
    @staticmethod
    def write(name: str = None, time_created: int = None):
        user = WriteUser(name, time_created)
        print(user.username)
        query = f"INSERT INTO User (username, time_created) VALUES ('{user.username}', {user.time_created})"
        DB.query(query)

    @staticmethod
    def read(uuid: str = None):
        if uuid:
            query = f"SELECT * FROM User WHERE uuid = '{uuid}'"
        else:
            query = f"SELECT * FROM User"
        return DB.query(query)
    @staticmethod
    def delete(uuid: str):
        query = f"DELETE FROM User WHERE uuid = '{uuid}'"
        DB.query(query)

    @staticmethod
    def update(uuid: str, username: str):
        if username:
            query = f"UPDATE User SET username = '{username}' WHERE uuid = '{uuid}'"
            DB.query(query)
    
class UserPostLogic:
    @staticmethod
    def write(user_uuid : str = None, post_9char: str = None, text: str = None, time_created: int = None):
        user_post = WriteUserPost(user_uuid, post_9char, text, time_created)
        query = f"INSERT INTO User_Post (user_uuid, post_9char, text, time_created) VALUES ('{user_post.user_uuid}', '{user_post.post_9char}', '{user_post.text}', {user_post.time_created})"
        DB.query(query)

    @staticmethod
    def read(uuid: str = None):
        if uuid:
            query = f"SELECT * FROM User_Post WHERE uuid = '{uuid}'"
        else:
            query = f"SELECT * FROM User_Post"
        return DB.query(query)
    
    @staticmethod
    def delete(uuid: str):
        query = f"DELETE FROM User_Post WHERE uuid = '{uuid}'"
        DB.query(query)
    
    @staticmethod
    def update(uuid: str, text: str):
        if text:
            query = f"UPDATE User_Post SET text = '{text}' WHERE uuid = '{uuid}'"
            DB.query(query)

    @staticmethod
    def readUserPosts(user_uuid: str):
        query = f"SELECT * FROM User_Post WHERE user_uuid = '{user_uuid}'"
        return DB.query(query)