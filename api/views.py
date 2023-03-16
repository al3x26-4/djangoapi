from django.http import response, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .models import Note, Stories, Category
from taggit.models import Tag
from .serializers import NoteSerializer, StorySerializer

# Create your views here.


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/stories/',
            'method': 'GET',
            'title': None,
            'body': None,
            'category': None,
            'story_img': None,
            'tags': None,
            'description': 'Returns an array of stories'
        },
        {
            'Endpoint': '/stories/id',
            'method': 'GET',
            'title': None,
            'body': None,
            'category': None,
            'story_img': None,
            'tags': None,
            'description': 'Returns a single story object'
        },
        {
            'Endpoint': '/stories/create/',
            'method': 'POST',
            'title': {'title': ""},
            'description': 'Creates new story with data sent in post request'
        },
        {
            'Endpoint': '/stories/id/update/',
            'method': 'PUT',
            'title': {'title': ""},
            'description': 'Creates an existing story with data sent in post request'
        },
        {
            'Endpoint': '/stories/id/delete/',
            'method': 'DELETE',
            'title': None,
            'body': None,
            'category': None,
            'story_img': None,
            'tags': None,
            'description': 'Deletes and exiting note'
        },
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    stories = category.stories.all()
    stories_a_to_z = category.stories.all().order_by('name')
    serializer = StorySerializer(stories, many=True)
    return Response(serializer.data)
  #  if request.GET.get('atoz'):
#        print("gotten")
#        products = category.products.all().order_by('name')
 #   elif request.GET.get('old'):
  #      products = category.products.all().order_by('name')
  #  product_filter = ProductFilter(request.GET, queryset=products)
 #   products = product_filter.qs
 #   return render(
#        request,
 #       'products/categoryPage.html',
  #      {
   #         'products_a_to_z': products_a_to_z,
   #         'products': products,
 #           'product_filter': product_filter,
  #          'category': category
  #      },
  #  )

@api_view(['GET'])
def getStories(request):
    stories = Stories.objects.all().order_by('-updated')
    serializer = StorySerializer(stories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getStory(request, pk):
    stories = Stories.objects.get(id=pk)
    serializer = StorySerializer(stories, many=False)
    content = {'please move along': 'nothing to see here'}
    return Response(serializer.data)


@api_view(['GET'])
def getNote(request, pk):
    notes = Note.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)
    content = {'please move along': 'nothing to see here'}
    return Response(serializer.data)


@api_view(["POST"])
def createNote(request):
    data = request.data
    note = Note.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(note, many=False)

    return Response(serializer.data)


@api_view(['PUT'])
def updateNote(request, pk):
    data = request.data
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteNote(request,pk):
    note = Note.objects.get(id=pk)
    note.delete()

    return Response('Note was deleted!')
