import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.apps import apps
from django.core import serializers
from rails_profile_grinding.V1.lib import get_times_response

from rails_profile_grinding.V1.serializers import TemplateSerializer

# Create your views here.


class GetTimes(viewsets.ViewSet):
    def list(self, request):
        return HttpResponse({}, status=200)


def get_model_from_invnr(invnr):
    app_models = apps.get_app_config("rails_profile_grinding").get_models()
    for model in app_models:
        if invnr in model.__name__:
            return apps.get_model("rails_profile_grinding", model.__name__)
    return None


def GetTimes2(request, invnr):
    model = get_model_from_invnr(invnr)
    if model is None:
        return JsonResponse({"detail": "Machine not found."}, status=400)

    date_from = request.GET.get("dateFrom")
    if not date_from:
        return JsonResponse({"detail": "Parameter dateFrom is missing."}, status=400)

    date_to = request.GET.get("dateTo")
    if not date_to:
        return JsonResponse({"detail": "Parameter dateTo is missing."}, status=400)

    data = model.objects.filter(
        timestamp__gte=date_from, timestamp__lte=date_to, p001=30
    )
    serializer = TemplateSerializer(data, many=True)
    json_data = json.loads(json.dumps(serializer.data))
    response = get_times_response(
        data=json_data,
        date_to=date_to,
        date_from=date_from,
        invnr=invnr,
        model_name=model.__name__,
    )
    return JsonResponse(response, safe=False)
