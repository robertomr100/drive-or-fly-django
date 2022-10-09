from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import TripOutput
from django.http import Http404
import datetime

from .forms import TripForm



# Create your views here.


def Index(request):
    template = loader.get_template('index.html')
    form = TripForm()
    context = {'form':form}

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
   # starting_destination = request.POST["starting_destination"]
    #final_destination = request.POST["final_destination"] 
    #date_start = request.POST["date_start"]
    #date_end = request.POST["date_end"]
  # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TripForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...

            print(form)
            starting_destination = form.data['starting_destination']
            final_destination = form.data['final_destination'] 
            date_start = form.data['date_start']
            date_end = form.data['date_end']
            print(date_start)

    # if a GET (or any other method) we'll create a blank form
    else:
        raise Http404("Form is not valid")



    format_str = '%Y-%m-%d'
    date_start_datetime = datetime.datetime.strptime(date_start, format_str)
    date_end_datetime = datetime.datetime.strptime(date_end, format_str)
    
    duration = date_end_datetime - date_start_datetime
    duration_in_s = duration.total_seconds()  
    hours = divmod(duration_in_s, 3600)[0] 
    
    tripOutput = TripOutput(flight_cost=hours*10,drive_cost=hours*5,flight_duration=hours,drive_duration=hours*2)
    tripOutput.save()
    #hacer los api calls;

    #guardar el resultado en un TripOutput con key = tripOutput_id;

    #redireccionar a Result pasando el valor de tripOutput_id;

    #return HttpResponseRedirect(reverse('comparison:results', args=(trip_output.id,)))
    return HttpResponseRedirect(reverse('comparison:result', args=(tripOutput.id, )))
