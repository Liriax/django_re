from django.shortcuts import redirect

def redirect_to_admin(request):
    response = redirect('/admin/')
    return response