#from typing import Any, Dict
from typing import Any, Dict
from django.views.generic import TemplateView,FormView,DeleteView
from .forms import PersonForm,ExpForm,EduForm
from .models import Person,Experience, Education
from django_xhtml2pdf.views import PdfMixin

class Home(TemplateView):
    Person.objects.all().delete()
    Education.objects.all().delete()
    Experience.objects.all().delete
    template_name ='home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['person']=Person.objects.filter(name="Michał")
        return context
    
class ExpDeleteView(DeleteView):
    template_name = 'expDelete.html'
    model = Experience
    success_url = "/add_exp/"

class EduDeleteView(DeleteView):
    template_name = 'eduDelete.html'
    model = Education
    success_url = "/add_edu/"
    

class AddPersonView(FormView):
    template_name = 'addCv.html'
    form_class = PersonForm
    success_url = "/add_exp/"
    def form_valid(self, form):
            destroy = Person.objects.all().delete()
            destroy1 = Experience.objects.all().delete()
            destroy2 = Education.objects.all().delete()
            new_object = Person.objects.create(
            name = form.cleaned_data['name'],
            last_name = form.cleaned_data['last_name'],
            #birth_date = form.cleaned_data['birth_date'],
            phone_number = form.cleaned_data['phone_number'],
            mail = form.cleaned_data['mail'],
            address = form.cleaned_data['address'],
            photo = form.cleaned_data['photo']
        )
            return super().form_valid(form)


class AddExpView(FormView):
    template_name = 'addExp.html'
    form_class = ExpForm
    success_url = "/add_exp"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exp']=Experience.objects.all()
        return context
    
    def form_valid(self, form):
        new_object = Experience.objects.create(
        time = form.cleaned_data['time'],
        exp = form.cleaned_data['exp']

        )
        return super().form_valid(form)
    
class AddEduView(FormView):
    template_name = 'addEdu.html'
    form_class = EduForm
    success_url = "/add_edu"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edu']=Education.objects.all()
        return context
    
    def form_valid(self, form):
        new_object = Education.objects.create(
        school_time = form.cleaned_data['school_time'],
        school = form.cleaned_data['school']

        )
        return super().form_valid(form)

class SummaryView(TemplateView):
    template_name ='summary.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['person']=Person.objects.all()
        context['edu']=Education.objects.all()
        context['exp']=Experience.objects.all()
        return context
    

