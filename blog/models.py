from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50)
    score = models.BigIntegerField(default=100)

    def add(self, n):
        self.score += n
        self.save()
    def sub(self, n):
        self.score -= n
        self.save()

class Player(models.Model):
    alias = models.CharField(max_length=5, unique = True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    score = models.BigIntegerField(default=1000)
    team = models.CharField(max_length=50, choices=(("Team #ForTheKids", "Team #ForTheKids"),
    ("B-Rate Anime Club", "B-Rate Anime Club"),
    ("Team Breaking Dustin's Back", "Team Breaking Dustin's Back")))

    def add(self, n):
        self.score += n
        self.save()
    def sub(self, n):
        self.score -= n
        self.save()

    def publish(self):
        self.save()

    def __str__(self):
        return self.name
