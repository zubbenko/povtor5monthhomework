from .models import Review
from .serializers import ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Director
from .serializers import DirectorSerializer
from .serializers import MovieSerializer
from .models import Movie


@api_view(['GET'])
def review_list_api_view(request):
    review_list = Review.objects.all()

    review_jsone = ReviewSerializer(instance=review_list, many=True).data
    return Response(data=review_jsone)


@api_view(['GET'])
def movie_list_api_view(reques):
    movie_list = Movie.objects.all()

    movie_jsone = MovieSerializer(instance=movie_list, many=True).data
    return Response(data=movie_jsone)



@api_view(['GET'])
def director_list_api_view(request):
    director_list = Director.objects.all()

    director_jsone = DirectorSerializer(instance=director_list, many=True).data


    return Response(data=director_jsone)


@api_view(['GET'])
def testir_api_view(request):
    data_dict = {
        'text' : 'home1',
        'int' : 123,
        'float' : 12.4 ,
        'list' : [1,2,3]
    }
    return Response(data=data_dict)

