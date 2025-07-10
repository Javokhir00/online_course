from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from pip._vendor.requests.models import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from course import serializers
from course.models import Subject, Course, Student, Teacher

# Create your views here.

class BaseView(TemplateView):
    template_name = 'course/base.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        return context



class IndexView(TemplateView):
    template_name = 'course/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] =Subject.objects.all()
        context['students'] = Student.objects.all()
        context['teachers'] = Teacher.objects.all()
        context['courses'] = Course.objects.annotate(student_count=Count('student'))
        return context


class CourseView(TemplateView):
    template_name = 'course/course.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        context['subjects'] = Subject.objects.all()
        return context


class SubjectCoursesView(ListView):
    model = Course
    template_name = 'course/subject_courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.filter(subject__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subject'] = Subject.objects.get(slug=self.kwargs['slug'])
        return context

class AboutView(TemplateView):
    template_name = 'course/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['students'] = Student.objects.all()
        return context


class TeacherView(TemplateView):
    template_name = 'course/teachers.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = Teacher.objects.all()
        return context




class CourseDetailView(DetailView):
    model = Course
    template_name = 'course/course_detail.html'
    context_object_name = 'course'




class CourseViewDetail(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'course/course_view_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        context['modules'] = course.modules.prefetch_related('topics__content_type')
        return context






