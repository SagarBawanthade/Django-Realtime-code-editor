from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseBadRequest
from .models import UserFile
from django.views.decorators.csrf import csrf_exempt
import json









def auth_page(request):
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

@login_required
@csrf_exempt
def save_code(request):
    """Save user's code to database"""
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=400)
    
    try:
        data = json.loads(request.body)
        code = data.get("code", "")
        filename = data.get("filename", "main.js")

        # Validate inputs
        if not filename:
            return JsonResponse({"error": "Filename required"}, status=400)

        # Get or create the file for this user
        user_file, created = UserFile.objects.get_or_create(
            user=request.user,
            filename=filename,
            defaults={'code': code}
        )
        
        # If file already exists, update it
        if not created:
            user_file.code = code
            user_file.save()

        return JsonResponse({
            "status": "ok",
            "saved_at": user_file.updated_at.isoformat(),
            "created": created
        })

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        print(f"Save error: {e}")
        return JsonResponse({"error": "Server error"}, status=500)


@login_required
def load_code(request):
    """Load user's code from database"""
    try:
        filename = request.GET.get("filename", "main.js")
        
        # Try to get existing file
        try:
            user_file = UserFile.objects.get(
                user=request.user,
                filename=filename
            )
            return JsonResponse({
                "code": user_file.code or "",
                "last_updated": user_file.updated_at.isoformat()
            })
        except UserFile.DoesNotExist:
            # Create new empty file
            user_file = UserFile.objects.create(
                user=request.user,
                filename=filename,
                code=""
            )
            return JsonResponse({
                "code": "",
                "last_updated": user_file.updated_at.isoformat()
            })

    except Exception as e:
        print(f"Load error: {e}")
        return JsonResponse({"error": "Server error", "code": ""}, status=500)