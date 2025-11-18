from django.db import models
from django.contrib.auth.models import User

class UserFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')
    filename = models.CharField(max_length=255, default="main.js")
    code = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'filename')  # One file per user per filename
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.user.username} - {self.filename}"