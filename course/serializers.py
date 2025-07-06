from rest_framework import serializers
from .models import Subject, Course, Comment


class CourseModelSerializer(serializers.ModelSerializer):
    subject_title = serializers.StringRelatedField(source = 'subject.title')
    subject_slug = serializers.SlugRelatedField(read_only=True, slug_field = 'slug', source = 'subject')
    username = serializers.CharField(source = 'owner.username')
    avg_rating = serializers.FloatField()
    count_comments = serializers.IntegerField()

    class Meta:
        model = Course
        exclude = ()

class SubjectModelSerializer(serializers.ModelSerializer):
    courses = CourseModelSerializer(many=True, read_only=True) #nested serializer
    course_count = serializers.SerializerMethodField()

    class Meta:
        model = Subject
        exclude = ()

    def get_course_count(self, obj):
        return obj.courses.count()


class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ()

