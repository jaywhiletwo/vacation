from django.db import models


class KeyGoal(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class KeyActivity(models.Model):
    name = models.CharField(max_length=255)
    key_goal = models.ForeignKey(KeyGoal)

    def __unicode__(self):
        return self.name
