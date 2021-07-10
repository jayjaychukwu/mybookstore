import django_filters
from .models import *

class bookfilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {'Genre': ['icontains'],
                  'Language': ['icontains']}
