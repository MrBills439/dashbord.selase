from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from services.models import Service
from blog.models import BlogPost
import json

def is_admin(user):
    """Check if user is admin (staff or superuser)"""
    return user.is_authenticated and (user.is_staff or user.is_superuser)

def admin_login(request):
    """Custom admin login view"""
    if request.user.is_authenticated and is_admin(request.user):
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user and is_admin(user):
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid credentials or insufficient permissions.')
        else:
            messages.error(request, 'Please enter both username and password.')
    else:
        # Initialize empty form for GET requests
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def dashboard(request):
    """Main dashboard view"""
    # Get statistics
    total_services = Service.objects.count()
    total_posts = BlogPost.objects.count()
    published_posts = BlogPost.objects.filter(is_published=True).count()
    total_users = User.objects.count()
    
    # Get recent items
    recent_services = Service.objects.all()[:5]
    recent_posts = BlogPost.objects.all()[:5]
    recent_users = User.objects.all()[:5]
    
    context = {
        'total_services': total_services,
        'total_posts': total_posts,
        'published_posts': published_posts,
        'total_users': total_users,
        'recent_services': recent_services,
        'recent_posts': recent_posts,
        'recent_users': recent_users,
    }
    
    return render(request, 'admin_dashboard/dashboard.html', context)

@login_required
@user_passes_test(is_admin)
def services_list(request):
    """Services management view"""
    services = Service.objects.all()
    return render(request, 'admin_dashboard/services_list.html', {'services': services})

@login_required
@user_passes_test(is_admin)
def blog_list(request):
    """Blog posts management view"""
    posts = BlogPost.objects.all()
    return render(request, 'admin_dashboard/blog_list.html', {'posts': posts})

@login_required
@user_passes_test(is_admin)
def users_list(request):
    """Users management view (read-only)"""
    users = User.objects.all()
    return render(request, 'admin_dashboard/users_list.html', {'users': users})

@csrf_exempt
@require_http_methods(["POST"])
@login_required
@user_passes_test(is_admin)
def toggle_post_publish(request, post_id):
    """Toggle blog post publish status via AJAX"""
    try:
        post = BlogPost.objects.get(id=post_id)
        post.is_published = not post.is_published
        post.save()
        
        return JsonResponse({
            'success': True,
            'is_published': post.is_published,
            'message': f'Post {"published" if post.is_published else "unpublished"} successfully'
        })
    except BlogPost.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Post not found'
        })
