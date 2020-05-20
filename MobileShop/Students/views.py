from django.shortcuts import render,redirect

# Create your views here.
from Students.models import Student
from Students.forms import StudentCreationForm,StudentUpdateForm
from django.views.generic import TemplateView


class CreateStudent(TemplateView):
    form_class= StudentCreationForm
    model_name= Student
    template_name = "students/studreg.html"

    def get(self,request, *args, **kwargs):
        context={}
        context["form"]=self.form_class
        return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listStud")

class ListStudent(TemplateView):
    model_name=Student
    template_name = "students/liststudent.html"

    def get_querySet(self):
        return self.model_name.objects.all()

    def get(self,request, *args, **kwargs):
        context={}
        context["students"]=self.get_querySet()
        return render(request,self.template_name,context)

class UpdateStudent(TemplateView):
    model_name= Student
    form_class= StudentUpdateForm
    template_name = 'students/studentEdit.html'

    def get_querySet(self):
        return self.model_name.objects.get(id=self.kwargs.get("pk"))

    def get(self, request, *args, **kwargs):
        form=self.form_class(instance=self.get_querySet())
        context={}
        context["form"]=form
        return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            # form.save()
            ob=self.get_querySet()
            ob.name=form.cleaned_data["name"]
            ob.course = form.cleaned_data["course"]
            ob.address = form.cleaned_data["address"]
            ob.password = form.cleaned_data["password"]
            ob.save()
            return redirect("listStud")

        else:
            context = {}
            context["form"] = form
            return render(request, self.template_name, context)


class StudentDelete(TemplateView):
    model_name=Student
    form_class=StudentCreationForm
    template_name = "students/deleteStudent.html"

    def get_queryset(self):
        return self.model_name.objects.get(id=self.kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
        form=self.form_class(instance=self.get_queryset())
        context={}
        context["form"]=form
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        self.get_queryset().delete()

        return redirect("listStud")