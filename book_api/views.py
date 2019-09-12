from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from book_api.models import NovelBook
from book_api.mySerializer import NovelBookSerializer
from rest_framework.response import Response

@csrf_exempt
def NovelBook_list(request):

    if request.method=='GET':
        novelBook = NovelBook.objects.all()
        serializer = NovelBookSerializer(novelBook,many=True)
        import json
        return HttpResponse(json.dumps(serializer.data,ensure_ascii=False),content_type='application/json')

    elif request.method=='POST':
        data = JSONParser().parse(request)
        serializer =NovelBookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=200)
        return JsonResponse(serializer.errors,status=400)


