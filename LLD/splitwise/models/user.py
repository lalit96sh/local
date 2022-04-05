from uuid import uuid4
from repo.user_repo import UserRepo
class User:
    def __init__(self, name, phone=None, email=None):
        self._id = uuid4().hex
        self.name = name
        self.phone = phone
        self.email = email
        self.groups = set()
        self._add_to_user_repo()

    def _add_to_user_repo(self):
        UserRepo.user_id_to_user_map[self._id] = self
    def add_group(self,group_id):
        self.groups.add(group_id)
    def get_all_groups(self):
        return self.groups