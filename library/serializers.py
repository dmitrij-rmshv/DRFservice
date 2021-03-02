from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Author

class AuthorModelsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"



