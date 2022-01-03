from django.shortcuts import redirect, render
from .settings import FUNCTION_APP_PATH
def redirect_to_admin(request):
    response = redirect('/'+FUNCTION_APP_PATH+'/admin/')
    return response
def index(request):
    return render(request, "build/index.html")