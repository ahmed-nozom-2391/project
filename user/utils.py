
from .models import MyUser



def get_username(user_name):
    try   :
        username = MyUser.objects.get(phone=user_name).username
    except:
        username = user_name
    return username

