from django.db import models 
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.TextField(unique=True)
    password = models.TextField()
    role = models.TextField(default='viewer')
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.TextField(null=True)

    class Meta:
        db_table = 'users'
        app_label = 'rts_app'



