from rest_framework import serializers
from .models import Subject, Course

class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ()

class SubjectModelSerializer(serializers.ModelSerializer):
    courses = CourseModelSerializer(many=True, read_only=True)
    course_count = serializers.SerializerMethodField()

    class Meta:
        model = Subject
        exclude = ()

    def get_course_count(self, obj):
        return obj.courses.count()

