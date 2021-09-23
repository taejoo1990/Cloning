from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):

    participants = models.ManyToManyField(
        "users.User", related_name="conversation", blank=True
    )

    def __str__(self):
        usernames = []
        for user in self.participants.all():  # read every user
            usernames.append(user.username)
        return ", ".join(usernames)

    def count_message(self):
        return self.messages.count()

    def count_participants(self):
        return self.participants.count()


class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says : {self.message}"
