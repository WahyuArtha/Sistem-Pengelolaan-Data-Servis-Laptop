from django.contrib.auth.decorators import login_required, user_passes_test
from akun.models import LevelUser

user_login_required = user_passes_test(lambda LevelUser: LevelUser.is_admin, login_url='/akun/login')

def admin_area(view_func):
    decorated_view_func = login_required(user_login_required(view_func))
    return decorated_view_func