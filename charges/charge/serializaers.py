from rest_framework import serializers

from charge.models import Category, Charges


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Category


class ChargesSerializers(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Charges
