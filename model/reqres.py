from model.response_create_user import ResponseCreateUser
from model.response_delete_user import ResponseDeleteUser
from model.response_get_users import ResponseGetUsers
from model.response_update_user import ResponseUpdateUser
from utils.base_session import BaseSession
from config import Server
from model.response_get_user import ResponseGetUser
class Reqres:
    def __init__(self, env):
        self.session = BaseSession(base_url=Server(env).reqres)

    def get_user(self, user_id: int):
        return ResponseGetUser(response=self.session.get(f"/api/users/{user_id}"))

    def get_users(self):
        return ResponseGetUsers(response=self.session.get(f"/api/users/"))

    def create_user(self, user_id: int):
        return ResponseCreateUser(response=self.session.post(f"/api/users/{user_id}"))

    def update_user(self, user_id: int):
        return ResponseUpdateUser(response=self.session.patch(f"/api/users/{user_id}"))

    def delete_user(self, user_id: int):
        return ResponseDeleteUser(response=self.session.delete(f"/api/users/{user_id}"))
