from rest_framework import serializers
from .models import Subject, Course, Comment
# from django.contrib.auth.models import User
from config.settings import AUTH_USER_MODEL
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class CourseModelSerializer(serializers.ModelSerializer):
    subject_title = serializers.StringRelatedField(source = 'subject.title')
    subject_slug = serializers.SlugRelatedField(read_only=True, slug_field = 'slug', source = 'subject')
    username = serializers.CharField(source = 'owner.username')
    avg_rating = serializers.FloatField(read_only=True, default=0.0)
    count_comments = serializers.IntegerField(read_only=True, default=0)

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



from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserModelSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError('Password must be at least 6 characters')
        return value




class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['password'] = user.password
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = {
            "username": self.user.username,
            "password": self.user.password,
        }

        return data
