from rest_framework import serializers
from .models import programmer


class Modelo_1_Serializer(serializers.ModelSerializer):
    class Meta:
        model = programmer
# fields = ('fullname','languaje','is_active’) acápodemos traer cualquier atributo o campo del modelo.
fields = '__all__'
# con la opción '__all__' traemos todos loscampos para ver y tener acceso a todo el registrode cada elemento que pertenezca al modelo