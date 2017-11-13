from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from .forms import TodoItemForm

# Create your views here.

def get_index(request):
    results = TodoItem.objects.all()
    return render(request, "index.html", { 'items': results })
    
def add_item(request):
    if request.method == "POST":
        # Get the details from the request
        form = TodoItemForm(request.POST)
        # Handle Saving to DB
        if form.is_valid():
            form.save()
            return redirect(get_index) # points to the function get_index above
    else:
        # GET Request so just give them a blank form
        form = TodoItemForm()    
    
    return render(request, "item_form.html", { 'form': form })
    
def edit_item(request, id):
    item = get_object_or_404(TodoItem, pk=id)
    
    if request.method == "POST":
        form = TodoItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(get_index)
    else:
        form = TodoItemForm(instance=item)
    
    return render(request, "item_form.html", { 'form': form })
    
def toggle_item(request, id):
    item = get_object_or_404(TodoItem, pk=id)
    
    item.done = not item.done # this line is the toggle. Reads in the done value and passes the oppisote of that value into the variable item.done
    item.save()
        
    return redirect(get_index)
    
def get_login(request):
    return render(request, "login.html")
    
    
