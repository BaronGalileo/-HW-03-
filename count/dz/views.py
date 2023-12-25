from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin, DeleteView

from .forms import PostForm, Wordcount
from .models import MyText


# Create your views here.



def create(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            myfile_l = str(request.POST['text'].lower())
            words_in_file = myfile_l.split()
            count_m = 0
            for i in words_in_file:
                if form.count == i:
                    count_m += 1
            form.wordcount = count_m


            form.save()



            return redirect('text', pk=form.pk)


        else:
            error = 'Форма была неверной'

    form = PostForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html', data)

class PostDetail(DetailView):
    model = MyText
    template_name = 'count.html'
    context_object_name = 'text'

class PostDelete(DeleteView):
    model = MyText
    template_name = 'delete.html'
    context_object_name = 'text'
    success_url = '/'

