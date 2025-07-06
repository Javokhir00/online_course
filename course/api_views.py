from django.db.models import Count, Avg
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Subject, Course, Comment
from .serializers import SubjectModelSerializer, CourseModelSerializer, CommentModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT
from rest_framework.generics import RetrieveUpdateDestroyAPIView


# ----------------------------- SUBJECT ---------------------------

# class SubjectList(APIView):
#     def get(self, request):
#         subjects = Subject.objects.all().order_by('id')
#         serializer = SubjectModelSerializer(subjects, many=True, context={'request': request})
#         return Response(serializer.data, status=HTTP_200_OK)

class SubjectList(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectModelSerializer

    def get_queryset(self):
        queryset = Subject.objects.all()
        queryset = queryset.annotate(course_count=Count('courses'))
        queryset = queryset.order_by('-course_count')
        return queryset


class SubjectListCrud(RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectModelSerializer

    def get_queryset(self):
        queryset = Subject.objects.all()
        # queryset = queryset.annotate(course_count=Count('courses'))
        # queryset = queryset.order_by('course_count')
        return queryset


class SubjectDetail(APIView):
    def get(self, request, pk):
        try:
            subject = Subject.objects.get(id=pk)
            serializer = SubjectModelSerializer(subject)
            return Response(serializer.data, status=HTTP_200_OK)
        except Subject.DoesNotExist:
            subject = None
            data = {
                'status': HTTP_400_BAD_REQUEST,
                'message': 'Subject does not exist'
            }
            return Response(data)


class SubjectCreate(APIView):
    def post(self,request):
        serializer = SubjectModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(f'{serializer.data['title']} successfully created',status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



class SubjectUpdate(APIView):
    def put(self, request, pk):
        try:
            subject = Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            return Response({"error": "Subject not found"}, status=HTTP_404_NOT_FOUND)

        serializer = SubjectModelSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class SubjectDelete(APIView):
    def delete(self, request, pk):
        try:
            subject = Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            return Response({"error": "Subject not found"}, status=HTTP_404_NOT_FOUND)

        subject.delete()
        return Response({"message": "Subject deleted successfully"}, status=HTTP_204_NO_CONTENT)


# ----------------------------- COURSE ---------------------------

class CourseList(APIView):
    def get(self, request):
        courses = Course.objects.all()
        courses = courses.annotate(avg_rating=Avg('comments__rating'), count_comments = Count('comments'))
        courses = courses.order_by('-avg_rating')
        serializer = CourseModelSerializer(courses, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class CourseDetail(APIView):
    def get(self, request, pk):
        try:
            course = Course.objects.get(id=pk)
            serializer = CourseModelSerializer(course)
            return Response(serializer.data, status=HTTP_200_OK)
        except Course.DoesNotExist:
            course = None
            data = {
                'status': HTTP_400_BAD_REQUEST,
                'message': 'Course does not exist'
            }
            return Response(data)


class CourseCreate(APIView):
    def post(self,request):
        serializer = CourseModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(f'{serializer.data['title']} successfully created',status=HTTP_201_CREATED)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class CourseUpdate(APIView):
    def put(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=HTTP_404_NOT_FOUND)

        serializer = CourseModelSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class CourseDelete(APIView):
    def delete(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=HTTP_404_NOT_FOUND)

        course.delete()
        return Response({"message": "Course deleted successfully"}, status=HTTP_204_NO_CONTENT)


class CourseListCrud(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer

    def get_queryset(self):
        queryset = Course.objects.all()
        return queryset


# ----------------------------- COMMENT ---------------------------

class CommentCrud(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer

