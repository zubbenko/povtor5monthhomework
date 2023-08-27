from rest_framework import serializers
from .models import Director
from .models import Movie
from .models import Review, Director



class DirectorSerializer(serializers.ModelSerializer):
    movie_cound = serializers.SerializerMethodField()
    class Meta:
        model = Director

        fields = ' id name movie_cound'.split()

    def get_movie_counds(self, director):
        return director.movie.set.cound()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie

        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'




class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director

        fields = 'name'.split()



