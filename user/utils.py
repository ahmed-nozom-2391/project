
from .models import MyUser
from datetime import datetime


def get_username(user_name):
    try   :
        username = MyUser.objects.get(phone=user_name).username
    except:
        username = user_name
    return username


def expired(date):
    target = datetime.strptime(date, "%d-%m-%y")
    return target < datetime.now()