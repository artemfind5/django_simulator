from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from untitled.n13.models import act_type, acts
from pathlib import Path

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

        print(str(Path(__file__).resolve().parent.parent.parent) + uploaded_file_url + "\n" + str(request.POST.get('myfile')))
        newact = acts(act_date=request.POST.get('date'),
                      act_type=request.POST.get('typebox'),
                      order_numb=request.POST.get('order_numb'),
                      order_date=request.POST.get('order_date'),
                      #file_path=request.POST.get('myfile'),
                      #file_path=uploaded_file_url
                      # TODO: Save the file correctly
                      file_path=str(Path(__file__).resolve().parent.parent.parent) + uploaded_file_url
                      )
        #newact.save()
        return render(request, 'data.html', {'uploaded_file_url' : uploaded_file_url,
                                             'acts': acts.objects.all()
                                             })
    #at = act_type(id=6, type='X')
    #at = act_type.objects.get(id=6)

    #at.delete()
    #at.save()

    #order_numb = request.POST.get('order_numb'))
    return render(request, "data.html", {'query_results' : acts.objects.all(),
                                         'acts': acts.objects.all()
                                         })