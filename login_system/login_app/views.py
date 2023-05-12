from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_render(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard')  # Redirect to dashboard if user is already logged in
    else:
        return render(request, "login.html")
    
def perform_login(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_obj = authenticate(request, username=username, password=password)
        if user_obj is not None:
            login(request, user_obj)
            return HttpResponseRedirect(reverse("admin_dashboard"))
        else:
            messages.error(request, "Username or password is invalid!")
            return HttpResponseRedirect("/")

@login_required(login_url='/')
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def perform_logout(request):
    logout(request)
    return HttpResponseRedirect("/")


def newpage(request):
    return HttpResponse(request)


# from django.shortcuts import render, redirect  # Importing necessary functions for rendering templates and redirecting requests
# from django.http.response import HttpResponse, HttpResponseRedirect  # Importing classes for creating HTTP responses
# from django.contrib.auth import authenticate, login, logout  # Importing functions for user authentication
# from django.urls import reverse  # Importing function for generating URLs
# from django.contrib import messages  # Importing framework for storing and displaying messages
# from django.contrib.auth.decorators import login_required  # Importing decorator for requiring login

# def login_render(request):
#     if request.user.is_authenticated:
#         return redirect('admin_dashboard')  # Redirect to dashboard if user is already logged in
#     else:
#         return render(request, "login.html")  # Render the login.html template

# def perform_login(request):
#     if request.method != "POST":
#         return HttpResponse("Method not allowed")  # Return a "Method not allowed" HTTP response if the request method is not POST
#     else:
#         username = request.POST.get("username")  # Get the username from the POST data
#         password = request.POST.get("password")  # Get the password from the POST data
#         user_obj = authenticate(request, username=username, password=password)  # Authenticate the user with the provided credentials
#         if user_obj is not None:
#             login(request, user_obj)  # Log in the user
#             return HttpResponseRedirect(reverse("admin_dashboard"))  # Redirect to the admin dashboard
#         else:
#             messages.error(request, "Username or password is invalid!")  # Display an error message
#             return HttpResponseRedirect("/")  # Redirect back to the login page

# @login_required(login_url='/')
# def admin_dashboard(request):
#     return render(request, 'admin_dashboard.html')  # Render the admin_dashboard.html template

# def perform_logout(request):
#     logout(request)  # Log out the user
#     return HttpResponseRedirect("/")  # Redirect to the homepage
