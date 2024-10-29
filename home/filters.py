import django_filters

from .models import Packages

class PackagesFilter(django_filters.FilterSet):
    class Meta:
        model=Packages
        fields={
            'service':['exact'],
            'Charges':['lt','gt'],
        }
    