from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
#landing page
def landing(request):
    form = forms.AuthenticationForm
    return render(request, 'landing_page.html', locals())
