from django.db import models

class ChecklistItem(models.Model):
    description = models.CharField(max_length=300)
    publish_date = models.DateTimeField(auto_now_add=True, blank=True)
    item_completed = models.BooleanField()
