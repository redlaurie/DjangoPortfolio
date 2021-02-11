import django_filters
from .models import *

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['image',]

class ProfileFilter(django_filters.FilterSet):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['image','CV']