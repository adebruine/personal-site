from django.shortcuts import render
from projects.models import Project, Person
from bakery.views import BuildableListView

def project_index(request):
    projects = Project.objects.all()
    people = Person.objects.all()
    context = {
        'projects': projects,
        'people': people
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Person.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

class ExampleTemplateView(BuildableListView):
    model = Person
    build_path = 'index.html'
    template_name = 'project_index.html'
