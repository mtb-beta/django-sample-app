from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_POST

from sample1.forms import MyModelForm

def form_view(request):
    form = MyModelForm()
    return render(request, 'mymodel_form.html', {'form': form})


@require_POST
def post_view(request):
    form = MyModelForm(request.POST)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('success_view'))

def success_view(request):
    return HttpResponse("成功しました")
