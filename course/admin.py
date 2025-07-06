from django.contrib import admin
from .models import Subject, Course, Module, Topic, Video, Image, Text, File, Student, Teacher
from import_export.admin import ImportExportModelAdmin
# Register your models here.



@admin.register(Subject)
class SubjectAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    list_display = ['title', 'image', 'slug']

    prepopulated_fields = {'slug': ('title',)}

@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    list_display = ['title']


@admin.register(Module)
class ModuleAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    list_display = ['title']


@admin.register(Topic)
class TopicAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    list_display = ['module', 'content_type']


@admin.register(Video)
class VideoAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    list_display = ['title']


@admin.register(Image)
class ImageAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    list_display = ['title']


@admin.register(Text)
class TextAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    list_display = ['title']


@admin.register(File)
class FileAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    list_display = ['title']


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    list_display = ['name']


@admin.register(Teacher)
class TeacherAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    list_display = ['name', 'job']