from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .models import Person
from .serializers import PeopleSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def index(request):
    courses = [
        {
            'id': 1,
            'title': 'Course 1',
            'description': 'Description 1',
            'instructor': 'Instructor 1'
        },
        {
            'id': 2,
            'title': 'Course 2',
            'description': 'Description 2',
            'instructor': 'Instructor 2'
        }
    ]
    
    if request.method == 'GET':
        print(request.GET.get('search'))
        return Response(courses)
    elif request.method == 'POST':
        data = request.data
        print(data)
        return Response({'message': 'Data created'}, status=201)
    elif request.method == 'PUT':
        return Response({'message': 'Data updated'}, status=200)
    
    return Response(courses)

@csrf_exempt
@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def people(request):
    if request.method == 'GET':
        obj = Person.objects.all() 
        serialized_data = PeopleSerializer(obj, many=True) 
        return Response(serialized_data.data)
    
    if request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    if request.method == 'PUT':
        data = request.data
        person = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(person, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    if request.method == 'PATCH':
        data = request.data
        person = Person.objects.get(id=data['id'])
        serializer = PeopleSerializer(person, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
