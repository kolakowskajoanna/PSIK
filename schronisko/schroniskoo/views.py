
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import *
from django.http import Http404, HttpResponse, JsonResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello homie .")


@csrf_exempt
def pies_list(request):
    if request.method == 'GET':
        piess = Pies.objects.all()
        serializer = PiesSerializer(piess, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PiesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def pies_detail(request, pk):
    try:
        pies = Pies.objects.get(pk=pk)
    except Pies.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PiesSerializer(pies)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = PiesSerializer(pies, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        pies.delete()
        return HttpResponse(status=204)

@csrf_exempt
def box_list(request):
    if request.method == 'GET':
        boxs = Box.objects.all()
        serializer = BoxSerializer(boxs, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def adopter_list(request):
    if request.method == 'GET':
        adopters = Adopter.objects.all()
        serializer = AdopterSerializer(adopters, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdopterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def adopter_detail(request, pk):
    try:
        adopter = Adopter.objects.get(pk=pk)
    except Adopter.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AdopterSerializer(adopter)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = AdopterSerializer(adopter, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        adopter.delete()
        return HttpResponse(status=204)

@csrf_exempt
def adopcja_list(request):
    if request.method == 'GET':
        adopcjas = Adopcja.objects.all()
        serializer = AdopcjaSerializer(adopcjas, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdopcjaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def adopcja_detail(request, pk):
    try:
        adopcja = Adopcja.objects.get(pk=pk)
    except Adopcja.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AdopcjaSerializer(adopcja)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = AdopcjaSerializer(adopcja, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        adopcja.delete()
        return HttpResponse(status=204)
