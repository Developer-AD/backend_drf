
import django_filters
from .models import Account
from django.forms.widgets import DateInput

class AccountFilter(django_filters.FilterSet):
    # date__gte = django_filters.DateFilter(widget=DateInput(attrs={'type': 'date'}), field_name='creation_date', lookup_expr='gte')
    # date__lte = django_filters.DateFilter(widget=DateInput(attrs={'type': 'date'}), field_name='creation_date', lookup_expr='lte')

    name = django_filters.CharFilter(lookup_expr='icontains')
    bank = django_filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Account
        fields = ['created_at', 'name', 'bank']