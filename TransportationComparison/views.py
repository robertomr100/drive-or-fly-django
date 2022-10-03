from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import TripOutput
from django.http import Http404


# Create your views here.


def Index(request):
    template = loader.get_template('index.html')
    context = {}

    return HttpResponse(template.render(context, request))


def Result(request, trip_output_id):
    try:
      trip = TripOutput.objects.get(pk=trip_output_id)
    except TripOutput.DoesNotExist:
      raise Http404("Trip does not exist")
  
    template = loader.get_template('result.html')
    #leemos la base de datos y la guardamos en una variable X
    context = {
        "flightDuration":trip.flight_duration,
        "driveDuration":trip.drive_duration,
        "flightCost":trip.flight_cost,
        "driveCost":trip.drive_cost
    }
    return HttpResponse(template.render(context, request))


def Compare(request):
    title = request.POST['title']
    starting_destination = request.POST['starting_destination']
    #hacer los api calls;

    #guardar el resultado en un TripOutput con key = tripOutput_id;

    #redireccionar a Result pasando el valor de tripOutput_id;

    #return HttpResponseRedirect(reverse('comparison:results', args=(trip_output.id,)))
    print(title)
    return HttpResponseRedirect(reverse('comparison:result', args=(1, )))
