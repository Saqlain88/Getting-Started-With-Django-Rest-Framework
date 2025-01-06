from rest_framework import serializers

from .models import CustomerModel

class CustomerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model=CustomerModel
        fields=('name','address')