from django.shortcuts import render
from django.utils import timezone
from .models import Post, Player, Team
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import ReportForm

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





# Form stuff below
# ==========================

def report(request):
    if request.method== 'POST':
        form = ReportForm(request.POST)
        if valiForm(form, request):
            reportGame(form, request)
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/reportError/')
    else:
        form = ReportForm()
    return render(request, 'blog/report.html', {'form': form})

def valiForm(form, request):
    if form.is_valid():
        for x in request.POST.getlist('winners'):
            for y in request.POST.getlist('losers'):
                if x == y:
                    return False
                    break
        return True
    else:
        return False

def reportGame(form, request):
    omega = calcOmega(form['c'].data, form['d'].data, form['l'].data, form['t'].data)
    winSum = 0
    winVXP = 0
    # Simple calc
    for winner in request.POST.getlist('winners'):
        Player.objects.all()[int(winner) - 1].add(100)
        Team.objects.all().get(name=Player.objects.all()[int(winner) - 1].team).add(1)
    for loser in request.POST.getlist('losers'):
        Player.objects.all()[int(loser) - 1].sub(100)
        Team.objects.all().get(name=Player.objects.all()[int(loser) - 1].team).sub(1)

def calcOmega(c, d, _l, t):
    c = int(c)
    d = int(d)
    t = int(t)
    _l = int(_l)
    l = 0
    # Normalize t
    if _l == 1:
        l = 3
    elif _l == 2:
        l = 2
    elif _l == 3:
        l = 1
    elif _l == 4:
        l = 1/2
    else:
        l == 1/3

    return (c + d + t)*l
