from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

def auth_page(request):
    # Return your auth.html file (signup/login)
    return render(request, "editor/auth.html")

@csrf_exempt
def api_login(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST allowed.")
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return JsonResponse({"success": True, "redirect": "/editor/"})
    else:
        return JsonResponse({"success": False, "error": "Invalid credentials."}, status=401)

@csrf_exempt
def api_signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            return JsonResponse({"error": "Missing fields"}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "User already exists"}, status=400)

        User.objects.create_user(username=username, password=password)

        # ✅ No login here — just show success popup on frontend
        return JsonResponse({
            "success": True,
            "message": "Signup successful! Redirecting to login...",
            "redirect": "/auth/login/"
        })

    return JsonResponse({"error": "Invalid request method"}, status=400)

def api_logout(request):
    logout(request)
    return redirect("/auth/login/")

@login_required
def editor_page(request, room_name="demo"):
    return render(request, "editor/editor.html", {
        "room_name": room_name,
        "username": request.user.username
    })
