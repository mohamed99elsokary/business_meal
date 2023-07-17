from cities_light.models import Country, Region
from factory import Faker
from factory.declarations import SubFactory
from factory.django import DjangoModelFactory
from pytest_factoryboy import register


@register
class CountryFactory(DjangoModelFactory):
    class Meta:
        model = Country

    name = Faker("text", max_nb_chars=60)
    continent = "AF"


@register
class RegionFactory(DjangoModelFactory):
    class Meta:
        model = Region

    country = SubFactory(CountryFactory)
    display_name = Faker("text", max_nb_chars=60)
