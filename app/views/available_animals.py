from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse
from django.contrib import messages
from app.models import Animal, Application

def available_animals(request):
    """
        This view retrieves all unadopted animals from the animal table and renders a grid-based template to display bootstrap cards.
    """

    if request.method == 'GET':
        animals = Animal.objects.filter(date_adopted=None).order_by('date_arrival')
        context = {
            'animals': animals
        }
        return render(request, 'app/available_animals.html', context)

# def available_animals_search(request):
#     if request.method == "POST":
#     search_text = request.POST["search_text"]
#     if search_text is not "":
#         results = Animal.objects.filter(name__contains=search_text).order_by('date_arrival')
#         context = {
#             "results": results,
#             "length": len(results),
#             "search_text": search_text,
#             "no_results": True if len(results) is 0 else False
#         }
#     else:
#         context = {
#             "no_results": True,
#             "search_text": search_text
#         }
#     return render(request, 'app/available_animals.html', context)

def animal_detail(request, id):
    """
        This view retrieves a single animal from the animal table, checks to ensure the animal is not adopted or id doesn't exist (control for manual user navigation to the url) and renders a detail template (otherwise redirects user with notification of animal status).
    """

    if request.method == 'GET':
        animal = Animal.objects.filter(pk=id, date_adopted=None)

        # A user who manually navigates to an adopted animal's detail view is redirected to the main pets page -- animal[0] won't exist
        try:
            animal = animal[0]
            context = {'animal': animal}

            # Check to see if a logged in user has already applied to adopt this animal. Get the status of their application if they have.
            if request.user.is_authenticated:
                application = Application.objects.filter(user=request.user, animal=animal)

                if len(application) == 1:
                    context = {
                        'animal': animal,
                        'existing_application': True,
                        'application': application[0]
                    }

            return render(request, 'app/animal_detail.html', context)

        except IndexError:
            messages.success(request, 'The animal you\'re looking for has been adopted or does not exist.')
            return HttpResponseRedirect(reverse('app:pets'))