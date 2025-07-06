from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.



class Subject(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='subject/images/')

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)
        super(Subject, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

    @property
    def get_num_of_courses(self):
        return self.courses.count()

class Course(models.Model):
    title = models.CharField(max_length=255, unique=True)
    overview = models.TextField(null=True, blank=True)
    duration = models.TimeField()
    price = models.DecimalField(max_digits=14, decimal_places=2)
    owner = models.ForeignKey(User,related_name='user_courses', on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='course/images/')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='courses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def get_num_of_modules(self):
        return self.modules.count()


class Module(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, related_name='modules', null=True, blank=True)

    def __str__(self):
        return self.title


class ItemBase(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Video(ItemBase):
    url = models.URLField()
    def __str__(self):
        return self.title

class Image(ItemBase):
    image = models.FileField(upload_to='images/')
    def __str__(self):
        return self.title

class Text(ItemBase):
    text = models.TextField()
    def __str__(self):
        return self.title

class File(ItemBase):
    file = models.FileField(upload_to='files/')
    def __str__(self):
        return self.title

class Topic(models.Model):
    module = models.ForeignKey(Module,
                               related_name='topics',
                               on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE,
                                     limit_choices_to={'model__in': (
                                         'text',
                                         'video',
                                         'image',
                                         'file',
                                     )}
                                     )
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    my_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f"{self.module.title} - {self.content_type} - {self.item}"


class Student(models.Model):
    name = models.CharField(max_length=255)
    opinion = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='student/images/')
    course = models.ForeignKey(Course, related_name = 'student', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='teacher/images/')
    job = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Comment(models.Model):
    class RatingChoices(models.IntegerChoices):
        ZERO = 0
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    topic = models.TextField(blank=True, null=True)
    content = models.TextField()
    rating = models.IntegerField(choices=RatingChoices.choices, default=RatingChoices.THREE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.topic

