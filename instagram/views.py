from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,views, forms
from django.contrib.auth.decorators import login_required
from .forms import LikesForm, CommentsForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse,Http404,HttpResponseRedirect



#landing page
def landing(request):
    form = forms.AuthenticationForm
    return render(request, 'landing_page.html', locals())

#home page
@login_required(login_url='/accounts/login')
def home(request):
    likesForm = LikesForm
    commentForm = CommentsForm
    images = Image.objects.all()
    user = request.user.get_username()
    profile = Profile.objects.all()
    likes = Like.objects.all()
    # numberOfLikes = len(likes)
    # comments = Comment.get_comments(id)
    # comments = Comment.objects.all()
    # numberOfComments=len(comments)
    # commentsPerImage = Comment.objects.filter(image_id=images.id).all()
    
    
    return render(request,'instagram_pages/home.html', locals())

def likes(request,image_id):
    likesForm = LikesForm()
    # if request.method == 'POST':
    #     likesForm = LikesForm(request.POST)
    #     if likesForm.is_valid():
    #         form = likesForm.save(commit=False)
            # form.user=request.user
            # form.image= get_object_or_404(Image,pk=image_id)
            # form.like= 1
            # form.save()
    #    CRUD     
    obj1=Like.objects.create(user=request.user,image=get_object_or_404(Image,pk=image_id),likes=1)
    obj1.save()
    print(obj1)
    return redirect('instagramHome')

def comments(request,image_id):
    commentsForm = CommentsForm()
    if request.method == 'POST':
        commentsForm = CommentsForm(request.POST)
        if commentsForm.is_valid():
            form = commentsForm.save(commit=False)
            form.user=request.user
            form.image = get_object_or_404(Image,pk=image_id)
            form.save()
  
    return redirect('instagramHome')

#search feature
@login_required(login_url='/accounts/login')
def search_results(request):
    likesForm = LikesForm
    commentForm = CommentsForm
    images = Image.objects.all()
    user = request.user.get_username()
    current_user = request.user
    photos = Image.objects.filter(profile=current_user.id)
    profile = Profile.objects.all()
    likes = Like.objects.all()
    
      
    try:
        user = User.objects.get(id =request.user.id)
    except ObjectDoesNotExist:
        raise Http404()
    message = 'based on your search term'
    return render(request, 'instagram_pages/search.html',locals())
    
    
    if 'username' in request.GET and request.GET["username"]:
        form = forms.AuthenticationForm
        images = Image.objects.all()
        user = request.user.get_username()
        profile = Profile.objects.all()
        search_term = request.GET.get("username")
        searched_users = Image.search_by_username(search_term)
        message = f"{search_term}"
        # print(User.objects.get(username=search_term))
        photos = Image.objects.filter(profile=User.objects.get(username=search_term))


        return render(request, 'instagram_pages/search.html',locals())

    else:
        message = "You haven't searched for any term"
        return render(request, 'instagram_pages/search.html',locals())


#profile page
@login_required(login_url='/accounts/login')
def profilePage(request):
    likesForm = LikesForm
    commentForm = CommentsForm
    images = Image.objects.all()
    user = request.user.get_username()
    current_user = request.user
    photos = Image.objects.filter(profile=current_user.id)
    profile = Profile.objects.all()
    likes = Like.objects.all()
 
    
    return render(request,'instagram_pages/profile.html', locals())

