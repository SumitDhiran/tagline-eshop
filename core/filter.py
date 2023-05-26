from django_filters import FilterSet, RangeFilter
from .models import Product

class PriceFilter(FilterSet):
    price = RangeFilter()

    class Meta:
        model = Product
        fields = ['price']