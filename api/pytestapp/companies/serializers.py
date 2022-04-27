from rest_framework import serializers
from .models import Company


class Companyserializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = [
            'id',
            'name',
            'status',
            'application_link',
            'last_update',
            'comentario_thiaguinho'
        ]
