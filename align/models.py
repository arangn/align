from django.db import models
from django.contrib.postgres.fields import ArrayField


class Pose(models.Model):
    name = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to="align/photos/", null=True, blank=True)
    description = models.CharField(max_length=500, null=False)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    def __str__(self):
        return '%s %s' % (self.name, self.password)

class SavedRoutine(models.Model):
    # INTENSITY_CHOICES = (
    # ('beginner', 'Beginner'),
    # ('intermediate', 'Intermediate'),
    # ('advanced', 'Advanced')
    # )

    PRACTICE_CHOICES = (
    ('strength', 'Strength'),
    ('mobility', 'Mobility')
    )

    name = models.CharField(max_length=25)
    user = models.ForeignKey(User, related_name='saved_routines', on_delete=models.CASCADE)
    # intensity = models.CharField(max_length=12, choices=INTENSITY_CHOICES)
    practice = models.CharField(max_length=15, choices=PRACTICE_CHOICES)
    targets = ArrayField(models.CharField(max_length=200), blank=True)
    pose = models.ManyToManyField('align.Pose', related_name='routine_poses')
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
