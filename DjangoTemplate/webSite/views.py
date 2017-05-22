from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader

from .models import *


class DTO(object):
    pib = ''
    currency = ''
    sum = 0
    period = 0
    percent = 0.0


def index(request):
    allDeposits = Deposit.objects.all();
    dtos = [];

    for deposit in allDeposits:
        dto = DTO();
        dto.deposit = deposit;
        dto.sum = float(deposit.sum);
        dto.period = deposit.periodDays;
        dto.pib = deposit.clientId.pib;
        dto.percent = (float(deposit.persent) - 1) * 100
        dtos.append(dto)

    template = loader.get_template('index.html')
    context = {
        'list': dtos,
    }
    return HttpResponse(template.render(context, request))

