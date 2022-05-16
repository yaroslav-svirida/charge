from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from charge.models import Charges, Category
from charge.serializaers import ChargesSerializers


class ChargesView(APIView):
    def post(self, request):
        price = request.data.get('price')

        cat_id = request.data.get('cat')
        category =Category.objects.get(id=cat_id)
        post = Charges.objects.create(price=price, cat=category)

        post_serialezed = ChargesSerializers(post).data
        return Response(post_serialezed)

    def get(self, request, pk=None):
        try:
            if not pk:
                prices = Charges.objects.all()
                prices_serialized = ChargesSerializers(prices, many=True).data
                return Response(prices_serialized)
            prices = Charges.objects.filter(id=pk)
            prices_serialized = ChargesSerializers(prices, many=True).data
            return Response(prices_serialized)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):

        name = Charges.objects.get(id=pk)
        serializer = ChargesSerializers(name, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):

        try:
            price = Charges.objects.get(pk=pk)

        except Charges.DoesNotExist:
            raise Http404
        price.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request):

        price = Charges.objects.all()
        price.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
