from django.db import models
from django.contrib.auth.models import User


# Database model to store race results
class RaceResult(models.Model):
    race_name = models.CharField(max_length=100)
    date = models.DateField()
    position = models.PositiveIntegerField()
    car_used = models.CharField(max_length=50)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.race_name} ({self.date})"


# Database model to store comments
class Comment(models.Model):
    # If user is deleted all messages are deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    race_result = models.ForeignKey(RaceResult, on_delete=models.CASCADE,
                                    related_name="comments")
    comment_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} on {self.race_result.race_name}"


# Database model to store events
class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.date})"
