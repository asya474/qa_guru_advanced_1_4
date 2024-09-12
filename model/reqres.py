
from utils.base_session import BaseSession
from config import Server
from model.response_get_user import ResponseGetUser
class Reqres:
    def __init__(self, env):
        self.session = BaseSession(base_url=Server(env).reqres)

    def get_user(self, user_id: int):
        return ResponseGetUser(response=self.session.get(f"/api/users/{user_id}"))

    def get_users(self):
        return ResponseGetUsers(response=self.session.get(f"/api/users"))

    def create_user(self):
        return ResponseCreateUser(response=self.session.get(f"/api/users/{user_id}"))

    def update_user(self):
        return ResponseUpdateUser(response=self.session.get(f"/api/users/{user_id}"))

    def delete_user(self):
        return ResponseDeleteUser(response=self.session.get(f"/api/users/{user_id}"))
