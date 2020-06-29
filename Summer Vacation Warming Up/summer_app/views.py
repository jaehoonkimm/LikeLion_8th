from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Question

from .forms import photoForm

# Create your views here.
def main(request):
    Question_obj = Question.objects
    return render(request, 'main.html', {'main_key':Question_obj})

def detail(request, detail_id):
    detail_obj = get_object_or_404(Question, pk=detail_id)
    return render(request, 'detail.html', {"detail_key":detail_obj})

def create(request):
    if request.method == "POST":
        Question_val = Question()
        Question_val.subject = request.POST['subject']
        Question_val.image = request.FILES['image']
        Question_val.content = request.POST['content']
        Question_val.create_date = request.POST['create_date']
        Question_val.save()
        return redirect('main')
    else:
        pass
    return render(request, 'create.html')

def update(request, update_id):
    update_obj = get_object_or_404(Question, pk=update_id)
    if request.method == "POST":
        update_obj.subject = request.POST['subject']
        update_obj.content = request.POST['content']
        update_obj.create_date = request.POST['create_date']
        update_obj.save()
        return redirect(reverse('detail', args=str(update_id)))
    else:
        pass
    return render(request, 'update.html', {"update_key":update_obj})

def delete(request, delete_id):
    delete_obj = get_object_or_404(Question, pk=delete_id)
    delete_obj.delete()
    return redirect('main')

# def photoForm_function(request):
#     if request.method == 'POST':
#         pass
#     elif request.method == 'GET':
#         form = photoForm()
#         return render(request, 'main.html', {'form': form})
#     else:
#         pass