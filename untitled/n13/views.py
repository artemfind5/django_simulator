from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from untitled.n13.models import act_type

# <a href="{% url '13' %}">
#     <button>Upload A.</button></a>

# TODO: pip install psycopg2 - db connect
# TODO: pip install django-tables2 - table view
# TODO: 'input new act row' to table preview
# TODO: rename app n13

def main(request):
    if request.method == 'POST' and request.FILES:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'data.html', {'uploaded_file_url' : uploaded_file_url
                                             })
    #at = act_type(id=6, type='X')
    #at = act_type.objects.get(id=6)

    #at.delete()
    #at.save()

    query_results = act_type.objects.all()
    #order_numb = request.POST.get('order_numb'))
    return render(request, "data.html", {'query_results' : query_results})