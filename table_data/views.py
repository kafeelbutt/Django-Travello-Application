from django.shortcuts import render,redirect,get_object_or_404
from travello.models import Destination
from table_data.models import products_scrape
from django.forms import ModelForm

# Create your views here.

class DestinationForm(ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'img','desc','price','offer']

class ProductsForm(ModelForm):
    class Meta:
        model = products_scrape
        fields = ['name', 'image','description','price','rating']

def dest_list(request):
    dest = products_scrape.objects.all()
    data = {}
    data['object_list'] = dest
    return render(request, 'destination_list.html', data)

def view_data(request):
    model = products_scrape
    field_names = [f.name for f in model._meta.get_fields()]
    data = [[getattr(ins, name) for name in field_names]
            for ins in model.objects.prefetch_related().all()]
    return render(request, 'table_data.html', {'field_names': field_names, 'data': data})


def create_data(request):
    form = ProductsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('view_data')
    return render(request, "book_form.html", {'form':form})

def dest_view(request, pk ):
    dest= get_object_or_404(products_scrape, pk=pk)    
    return render(request, 'dest_detail.html', {'object':dest})

def update_data(request, pk ):
    destination= get_object_or_404(products_scrape, pk=pk)
    form = DestinationForm(request.POST or None, instance=destination)
    if form.is_valid():
        form.save()
        return redirect('view_data')
    return render(request, "book_form.html", {'form':form})

def delete_data(request, pk ):
    destination= get_object_or_404(products_scrape, pk=pk)    
    if request.method=='POST':
        destination.delete()
        return redirect('view_data')
    return render(request, "book_confirm_delete.html", {'object':destination})