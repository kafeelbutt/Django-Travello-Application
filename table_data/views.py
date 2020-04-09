from django.shortcuts import render,redirect,get_object_or_404
from travello.models import Destination
from django.forms import ModelForm

# Create your views here.

class DestinationForm(ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'img','desc','price','offer']

def dest_list(request):
    dest = Destination.objects.all()
    data = {}
    data['object_list'] = dest
    return render(request, 'destination_list.html', data)

def view_data(request):
    model = Destination
    field_names = [f.name for f in model._meta.get_fields()]
    data = [[getattr(ins, name) for name in field_names]
            for ins in model.objects.prefetch_related().all()]
    return render(request, 'table_data.html', {'field_names': field_names, 'data': data})


def create_data(request):
    form = DestinationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('view_data')
    return render(request, "book_form.html", {'form':form})

def dest_view(request, pk ):
    dest= get_object_or_404(Destination, pk=pk)    
    return render(request, 'dest_detail.html', {'object':dest})

def update_data(request, pk ):
    destination= get_object_or_404(Destination, pk=pk)
    form = DestinationForm(request.POST or None, instance=destination)
    if form.is_valid():
        form.save()
        return redirect('view_data')
    return render(request, "book_form.html", {'form':form})

def delete_data(request, pk ):
    destination= get_object_or_404(Destination, pk=pk)    
    if request.method=='POST':
        destination.delete()
        return redirect('view_data')
    return render(request, "book_confirm_delete.html", {'object':destination})