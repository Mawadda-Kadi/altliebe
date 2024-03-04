from django.core.management.base import BaseCommand
from users.models import State, City

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

        for state_name, cities in states_cities.items():
            state, created = State.objects.get_or_create(name=state_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added state {state_name}'))
            for city_name in cities:
                City.objects.get_or_create(state=state, name=city_name)
                self.stdout.write(self.style.SUCCESS(f'Added city {city_name}'))
