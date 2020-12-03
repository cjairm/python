from movies.models import Movie
from movies.serializers import MovieSerializer
from django.http import Http404
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class MovieList(APIView):
    def get(self, request, format=None):
        paginator = PageNumberPagination()

        q = request.GET.get('q')
        order = request.GET.get('order_by')
       
        if order and q:
            movies = Movie.objects.order_by(order).filter(title__contains=q)
        elif order and not q:
            movies = Movie.objects.order_by(order).all()
        elif not order and not q:
            movies = Movie.objects.all()
        else:
            movies = Movie.objects.filter(title__contains=q)
        context = paginator.paginate_queryset(movies, request)
        serializer = MovieSerializer(context, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieObject(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
