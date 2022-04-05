from uuid import uuid4
from repo.user_repo import UserRepo
from repo.expense_repo import ExpenseRepo
from .user_share import UserShare
class Expense:
    def __init__(self,user_id,amount,description="",user_share_map={}):
        self._id = uuid4().hex
        self.user_id = user_id
        self.description = description
        self.user_share = UserShare(user_id,user_share_map)
        self.amount = amount
    
    def _add_expense_to_expense_repo(self):
        ExpenseRepo.expense_id_to_expense_map[self._id] = self
        
    def get_expense_description_with_respect_to_user(self,user_id):
        if user_id==self.user_id:
            user_name = "You"
        else:
            user_name = UserRepo.user_id_to_user_map.get(self.user_id).name
        pay_string = "{} paid Rs. {}".format(user_name, self.amount)
        return "{:<20}{:<35}{}".format(self.description, pay_string, self.user_share.get_short_overall_description(user_id))