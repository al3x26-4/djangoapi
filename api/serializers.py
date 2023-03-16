from rest_framework.serializers import ModelSerializer
from .models import Note, Stories
from taggit.serializers import TagListSerializerField, TaggitSerializer


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class StorySerializer(TaggitSerializer, ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Stories
        fields = '__all__'
