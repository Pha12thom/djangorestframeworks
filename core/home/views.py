from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Person
from serializers import PeopleSerializer

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

api_view(['GET', 'POST', 'PUT', 'DELETE'])
def people(request):
    if request.GET:
        obj = Person.object.all()
        Person = PeopleSerializer(obj, many=True)
        return Response(Person.data)
    
    if request.POST:
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
     
        
        