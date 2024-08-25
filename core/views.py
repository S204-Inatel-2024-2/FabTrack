from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PrintModel
from .forms import PrintModelForm

@login_required
def home(request):
    return render(request, 'core/home.html')

@login_required
def send_model(request):
    if request.method == 'POST':
        form = PrintModelForm(request.POST, request.FILES)
        if form.is_valid():
            print_model = form.save(commit=False)
            print_model.user = request.user
            print_model.save()
            return redirect('core/history')
    else:
        form = PrintModelForm()
    
    return render(request, 'core/send_model.html', {'form': form})

@login_required
def history(request):
    orders = PrintModel.objects.filter(user=request.user)
    return render(request, 'core/history.html', {'orders': orders})
