import serializers as serializers

from book_api.models import NovelBook
from rest_framework import serializers

class NovelBookSerializer(serializers.ModelSerializer):
    class Meta:
        model =NovelBook
        fields = ['book_id','book_name','book_author']

