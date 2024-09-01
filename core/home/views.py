from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
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
    return Response(courses)