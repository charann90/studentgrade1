from rest_framework import serializers

from grade_app.models import Grades


class GradesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Grades
        fields=['student_name','class_name','grade','marks']

