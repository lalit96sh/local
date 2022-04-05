from uuid import uuid4
from .user_share import UserShare
from repo.group_repo import GroupRepo
from repo.user_repo import UserRepo
from .expense import Expense
class Group:
    def __init__(self,name,created_by=None):
        self._id = uuid4().hex
        self.name = name
        self.created_by = created_by
        self.members = {created_by} if created_by else set()
        self.user_share_map = UserShare()
        self.expenses = []
        self.add_group_to_group_repo()

    def add_group_to_group_repo(self):
        GroupRepo.group_id_to_group_map[self._id] = self
        
    def add_member_to_group(self,member_id):
        self.members.add(member_id)
        UserRepo.user_id_to_user_map.get(member_id).add_group(self._id)
        
    def get_group_members(self):
        return self.members
        
    def add_expense_in_group(self,user_id,amount,description,user_share_map):
        self.expenses.append(Expense(user_id,amount,description,user_share_map))
        self.user_share_map.process_user_map(user_id,user_share_map)
        
    def get_group_user_share_result(self,user_id):
        return self.user_share_map.get_user_share_with_respect_to_user(user_id)
    
    def get_group_expenses_transactions(self,user_id):
        response = []
        for expense in self.expenses:
            response.append(expense.get_expense_description_with_respect_to_user(user_id))
        return response
    
    def get_complete_group_response_with_transaction(self,user_id):
        return [self.get_group_user_share_result(user_id),self.get_group_expenses_transactions(user_id)]
        
        