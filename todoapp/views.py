from django.shortcuts import render,redirect,get_object_or_404
from.models import Todo

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    return render(request,"index.html", {'todos': todos} )



def add_todo(request):
    if request.method == "POST":
        tittle = request.POST.get('tittle','').strip()
        if tittle:
            Todo.objects.create(tittle=tittle)  
    return redirect('index')
    


def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect('index')    




def toggle_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.done = not todo.done
    todo.save()
    return redirect('index')










