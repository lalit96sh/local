from models.group import Group
from models.user import User
from repo.group_repo import GroupRepo

class TestUserData:
    users = {}
    groups = {}
    def add_groups(self,name):
        TestUserData.groups[name] = TestUserData.groups.get(name,Group(name))
    def add_user(self,name,group=None):
        TestUserData.users[name] = TestUserData.users.get(name, User(name))
        if group:
            TestUserData.groups[group].add_member_to_group(TestUserData.users[name]._id)

def create_sample_groups():
    TestUserData().add_groups("Mnit")
    TestUserData().add_groups("Surya Apartments")
    
def create_sample_users():
    TestUserData().add_user("Lalit","Mnit")
    TestUserData().add_user("Rohit","Mnit")
    TestUserData().add_user("Ankit","Mnit")

    TestUserData().add_user("Lalit","Surya Apartments")
    TestUserData().add_user("Tanishk Dudi","Surya Apartments")
    TestUserData().add_user("Tanishq Rohela","Surya Apartments")
    
def add_expense(user,group,amount,description,user_share_map):
    user_id = TestUserData.users[user]._id
    # import pdb;pdb.set_trace()
    TestUserData.groups[group].add_expense_in_group(user_id,amount,description,user_share_map)


def equal_share_map(paid_by,group_name,amount):
    paid_by_id = TestUserData.users[paid_by]._id
    users = TestUserData.groups[group_name].get_group_members()
    equal_share = amount/len(users)
    user_map = {}
    for user_id in users:
        if paid_by_id != user_id:
            user_map[user_id] = equal_share
    return user_map

def get_all_user_groups(user_name):
    groups = TestUserData.users[user_name].get_all_groups()
    group_names = []
    for group in groups:
        group_names.append(GroupRepo.group_id_to_group_map.get(group).name)
    return group_names

def get_group_data(group_name,user_name):
    header, transactions = TestUserData.groups[group_name].get_complete_group_response_with_transaction(TestUserData.users[user_name]._id)
    divider = "\n---------------------------------------\n"
    result = "\n".join(header)+divider+"\n".join(transactions)
    return result
            
create_sample_groups()
create_sample_users()

#
add_expense("Lalit","Surya Apartments",90,"butter & bread",equal_share_map("Lalit","Surya Apartments",90))
add_expense("Tanishk Dudi","Surya Apartments",105,"chai sutta",equal_share_map("Tanishk Dudi","Surya Apartments",105))
add_expense("Tanishk Dudi","Surya Apartments",300,"khracha pani",equal_share_map("Tanishk Dudi","Surya Apartments",300))
add_expense("Lalit","Mnit",75,"butter & bread",equal_share_map("Lalit","Mnit",75))



# 
def show_data_for_user(me):
    print("\n\n*************************Showing for {}********************".format(me))
    user_groups = get_all_user_groups(me)
    print(user_groups)
    # import pdb;pdb.set_trace()
    #
    for each in user_groups:
        print('----------------------{}------------------'.format(each))
        print(get_group_data(each,me))

show_data_for_user("Lalit")
show_data_for_user("Tanishk Dudi")
show_data_for_user("Tanishq Rohela")
show_data_for_user("Ankit")
show_data_for_user("Rohit")
# import pdb;pdb.set_trace()
