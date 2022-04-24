from global_contacts import GlobalContacts
from models.user import User
from models.contacts import Contact
class TrueCaller:
    
    # def __init__(self):
    #     self
        
        
    # Test case 1: Create user and register

    user1 = User("lalit","8003750089")
    user1.register_user()

    # Test case 2: Add contacts to user
    user1.add_contacts(Contact(""))
    

    # Test case 3: check added contacts count

    # Test case 4: search for contacts by name

    # Test case 5: search for contacts by name

    # Test case 6a: search for contacts by phone

    # Test case 6b: search for contacts by phone


    # Test case 6c: search for contacts by phone

    # Test case 7: Block a number

    # Test case 8: should not receive call from blocked caller

    # Test case 9: Unblock number


    # Test case 10: should receive call from un blocked caller

    # Test case 11: Should be able to report spam to global list

    # Test case 12: Should be able to block global spammers