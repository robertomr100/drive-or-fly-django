from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse


# Create your views here.


def Index(request):
    template = loader.get_template('index.html')
    context = {}
    
    return HttpResponse(template.render(context, request))


def Result(request, tripOutput_id):
    template = loader.get_template('result.html')
    #leemos la base de datos
    context = {
        # bla bla
        #TripOutput
    }
    return HttpResponse(template.render(context, request))


def Compare(request,trip_input_id):
    title = request.POST['title']
    #este resive un Post
    #logica que convierte un Comparison input a Comparison Output
    #guardamos el Comparison Output en base de datos
    #el key del nuevo entry va a ser ComparisonOutput.id

    #return HttpResponseRedirect(reverse('comparison:results', args=(trip_output.id,)))
    print(title)
    return HttpResponseRedirect(reverse('comparison:result', args=(1,)))



