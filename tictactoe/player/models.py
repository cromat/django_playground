from django.contrib.auth.models import User
from django.db import models


class Invitation(models.Model):
    from_user = models.ForeignKey(User, related_name="invitations_sent", on_delete=models.CASCADE)
    to_user = models.ForeignKey(
        User, related_name="invitations_received",
        verbose_name="User to invite",
        help_text="Pleasre select the user you want to play a game with.",
        on_delete=models.CASCADE
    )
    message = models.CharField(
        max_length=300,
        verbose_name="Optional Message",
        help_text="It's always nice to add a friendly message."
    )
    timestamp = models.DateTimeField(auto_now_add=True)
