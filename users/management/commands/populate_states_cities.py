from django.core.management.base import BaseCommand
from users.models import State, City
from django.db import transaction

class Command(BaseCommand):
    help = 'Populates the database with states and cities'

    def handle(self, *args, **options):
        states_cities = {
            'Baden-Württemberg': ['Stuttgart', 'Mannheim', 'Karlsruhe'],
            'Bavaria': ['Munich', 'Nuremberg', 'Augsburg'],
            'Berlin': ['Berlin'],
            'Brandenburg': ['Potsdam', 'Cottbus'],
            'Bremen': ['Bremen', 'Bremerhaven'],
            'Hamburg': ['Hamburg'],
            'Hesse': ['Frankfurt', 'Wiesbaden', 'Kassel'],
            'Lower Saxony': ['Hanover', 'Braunschweig', 'Oldenburg'],
            'Mecklenburg-Vorpommern': ['Rostock', 'Schwerin'],
            'North Rhine-Westphalia': ['Cologne', 'Düsseldorf', 'Dortmund'],
            'Rhineland-Palatinate': ['Mainz', 'Ludwigshafen', 'Koblenz'],
            'Saarland': ['Saarbrücken'],
            'Saxony': ['Dresden', 'Leipzig', 'Chemnitz'],
            'Saxony-Anhalt': ['Magdeburg', 'Halle', 'Merseburg'],
            'Schleswig-Holstein': ['Kiel', 'Lübeck'],
            'Thuringia': ['Erfurt', 'Jena']
}


        with transaction.atomic():  # Use a transaction to ensure data integrity
            # Clear the existing data
            City.objects.all().delete()
            State.objects.all().delete()

            # Populate the new data
            for state_name, cities in states_cities.items():
                state = State.objects.create(name=state_name)
                for city_name in cities:
                    City.objects.create(name=city_name, state=state)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with states and cities'))