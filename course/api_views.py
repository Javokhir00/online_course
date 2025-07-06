from django.http import Http404
from .models import Subject, Course
from .serializers import SubjectModelSerializer, CourseModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND, \
    HTTP_204_NO_CONTENT


# ----------------------------- SUBJECT ---------------------------

class SubjectList(APIView):
    def get(self, request):
        subjects = Subject.objects.all().order_by('id')
        serializer = SubjectModelSerializer(subjects, many=True)
        return Response(serializer.data, status=HTTP_200_OK)



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
        courses = Course.objects.all().order_by('id')
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