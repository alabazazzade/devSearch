from tkinter import CASCADE
from django.db import models
import uuid
from users.models import profile

from traitlets import default

class Project(models.Model):
    owner = models.ForeignKey(profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    desctiption = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default='default.png')
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                            primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-vote_ratio','-vote_total']

    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        total = reviews.count()
        ratio = (upVotes / total) * 100
        self.vote_ratio = ratio
        self.vote_total = total
        self.save()
class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    owner= models.ForeignKey(profile, on_delete=models.CASCADE, null=True)
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                            primary_key=True, editable=False)

    def __str__(self):
        return self.value

    class Meta:
        unique_together = [['owner', 'project']] # this way one owner cant leave reviews for a project more than once

    

class Tag(models.Model):
    name = models.CharField(max_length=200)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                        primary_key=True, editable=False)

    def __str__(self):
        return self.name