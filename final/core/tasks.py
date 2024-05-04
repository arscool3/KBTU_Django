import dramatiq
from .models import Country, Citizen

@dramatiq.actor
def update_country_population(country_id, population):
    try:
        country = Country.objects.get(id=country_id)
        country.population = population
        country.save()
    except Country.DoesNotExist:
        print(f"Country with id {country_id} does not exist.")

@dramatiq.actor
def notify_new_citizen(citizen_id):
    try:
        citizen = Citizen.objects.get(id=citizen_id)
        print(f"New citizen created: {citizen.name}")
    except Citizen.DoesNotExist:
        print(f"Citizen with id {citizen_id} does not exist.")
