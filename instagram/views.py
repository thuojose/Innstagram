from django.shortcuts import render
from django.contrib.auth import login,views, forms
from django.contrib.auth.decorators import login_required
from .forms import LikesForm, CommentsForm

# Create your views here.
#landing page
def landing(request):
    form = forms.AuthenticationForm
    return render(request, 'landing_page.html', locals())

#home page
@login_required(login_url='/accounts/login')
def home(request):
    likesForm = LikesForm
    commentForm = CommentsForm
    
    
    return render(request,'instagram_pages/home.html', locals())
