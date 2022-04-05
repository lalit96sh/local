from collections import defaultdict
from repo.user_repo import UserRepo
from constants import OWES,LENTS
class UserShare:
    def __init__(self,user_id=None,user_map={}):
        self.share_dict = defaultdict(lambda: defaultdict(int))
        self.process_user_map(user_id,user_map)
        
    def process_user_map(self,user_id,user_map):
        for benificiary_user_id,amount in user_map.items():
            self.share_dict[user_id][benificiary_user_id]+=amount
            self.share_dict[benificiary_user_id][user_id]-=amount
        
    def get_user_share_with_respect_to_user(self,user_id):
        result = []
        for benificiary_id,amount in self.share_dict[user_id].items():
            print_string = self.get_prettified_print(benificiary_id,amount)
            if print_string:
                result.append(print_string)
        return result
    def get_prettified_print(self,u2,amount):
        if amount==0:
            return None
        if amount>0:
            first_person = UserRepo.user_id_to_user_map.get(u2).name
            second_person = "You"
        else:
            second_person = UserRepo.user_id_to_user_map.get(u2).name
            first_person = "You"
            
        return "{} owes {} Rs {}".format(first_person,second_person,abs(amount))
    
    def get_short_overall_description(self,user_id):
        overall_amount = sum(self.share_dict[user_id].values())
        if overall_amount == 0:
            "You are not included"
        dependency = OWES if overall_amount<0 else LENTS
        return "You {} Rs {}".format(dependency,abs(overall_amount))