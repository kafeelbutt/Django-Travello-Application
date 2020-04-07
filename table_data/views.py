from django.shortcuts import render
from travello.models import Destination

# Create your views here.

def view_data(request):
    model = Destination
    field_names = [f.name for f in model._meta.get_fields()]
    data = [[getattr(ins, name) for name in field_names]
            for ins in model.objects.prefetch_related().all()]
    return render(request, 'table_data.html', {'field_names': field_names, 'data': data})
