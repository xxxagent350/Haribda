from models.user import User
from DB_operators.BD_init import get_all_user_ids

users_id  = get_all_user_ids()
user_list = {}

for i in users_id:
    user_list[i] = User(i)