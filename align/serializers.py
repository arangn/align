from rest_framework import serializers
from .models import Pose, Sequence

class SequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sequence
        fields = ("id", "name", "poses", "target")

    def get_sequence(self, validated_data):
        return Sequence.objects.all()

class PoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pose
        fields = ("id", "name", "description", "image", "height", "width")

    def get_sequence(self, validated_data):
        return Pose.objects.all()
