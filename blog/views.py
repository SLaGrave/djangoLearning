from django.shortcuts import render
from django.utils import timezone
from .models import Post, Player, Team
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def rank_list(request):
    players = Player.objects.all().order_by('score').reverse()
    teams = Team.objects.all().order_by('score').reverse()
    return render(request, 'blog/rank_list.html', {'teams': teams, 'players': players})

def player_detail(request, alias):
    player = get_object_or_404(Player, alias=alias)
    return render(request, 'blog/player_detail.html', {'player': player})
