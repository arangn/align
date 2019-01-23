from django.contrib import admin
from . models import Pose
from . models import Sequence


# Register your models here.
admin.site.register(Pose)
admin.site.register(Sequence)
