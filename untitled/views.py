#from django.shortcuts import render

#def index(request):
 #   return render(request, 'index.html', context={
  #      'who': 'World',
   # })
#<iframe src="header.html" seamless/>

from django.views.generic.base import TemplateView

class IndexView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #print(context['HTTP_X_FORWARDED_FOR'])
        context['who'] = 'World'
        return context

class AboutPageView(TemplateView):
    template_name = 'fun.html'

class TempPageView(TemplateView):
    template_name = 'temp.html'