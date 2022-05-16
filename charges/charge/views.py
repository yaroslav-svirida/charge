from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from charge.models import Category
from charge.serializaers import CategorySerializers


class CategoryView(APIView):
    def post(self, request):
        name = request.data.get('name')

        post = Category.objects.create(name=name)
        post_serialezed = CategorySerializers(post).data
        return Response(post_serialezed)

    def get(self, request, pk=None):
        try:
            if not pk:
                category = Category.objects.all()
                category_serialized = CategorySerializers(category, many=True).data
                return Response(category_serialized)
            category = Category.objects.filter(id=pk)
            category_serialized = CategorySerializers(category,many=True).data
            return Response(category_serialized)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    def put(self,request,pk):

        name = Category.objects.get(id=pk)
        serializer = CategorySerializers(name, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, pk):
        try:
            cat=Category.objects.get(pk=pk)

        except Category.DoesNotExist:
            raise Http404
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
