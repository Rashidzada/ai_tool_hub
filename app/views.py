# views.py
from django.shortcuts import render
from django.db.models import Count
from .models import Category, AITool, SiteStat, Article

def index(request):
    # Get all categories with tool counts
    categories = Category.objects.annotate(tool_count=Count('aitool')).order_by('name')
    
    # Get featured tools
    featured_tools = AITool.objects.filter(featured=True).order_by('-created_at')[:6]
    
    # Get latest tools
    latest_tools = AITool.objects.filter(is_verified=True).order_by('-created_at')[:6]
    
    # Get site statistics
    stats = SiteStat.objects.filter(is_active=True)
    
    # Get latest articles
    articles = Article.objects.filter(is_published=True).order_by('-created_at')[:3]
    
    # Get all tools for the search functionality
    all_tools = AITool.objects.filter(is_verified=True).order_by('name')
    
    context = {
        'categories': categories,
        'featured_tools': featured_tools,
        'latest_tools': latest_tools,
        'stats': stats,
        'articles': articles,
        'all_tools': all_tools,
    }
    
    return render(request, 'index.html', context)