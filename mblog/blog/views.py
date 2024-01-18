from django.shortcuts import render,redirect
from .models import *
from .forms import CreatePost,CreateProfile
from django.contrib import messages


# Create your views here.
def home(request):
    posts = Post.objects.all()
    posts_to_show = []

    search = request.GET.get("search")
    print(search)
    if search:
        for post in posts:
            if str(search).lower()in post.title.lower() or str(search).lower() in str(post.author.author_name).lower():
                posts_to_show.append(post)
            else:
                continue

    else:
        posts_to_show = posts
    return render(request, "home.html", context={"posts": posts_to_show})
    
def update_profile(request):


    if request.method == "POST":
        print('Post Request!')
        form = CreateProfile(request.POST)
        if form.is_valid():
            author_name = form.data['author_name']
            age = form.data['age']
            occupation = form.data['occupation']
            clg_yr = form.data['clg_yr']
            degree = form.data['deg']

        all_prof = Profile.objects.all()

        p = Profile(author_real=request.user,author_name=author_name,age=age,occupation=occupation,clg_yr=clg_yr,deg=degree)
        prof_exists = True
        for prof in all_prof:
            if str(request.user.username).lower() == str(prof.author_real.username).lower():
                p = Profile.objects.filter(author_real=request.user)[0]
                print(p)
                prof_exists = True
                break
            else:
                prof_exists = False
        print(prof_exists)
        if prof_exists:
            p.author_name = author_name
            p.occupation = occupation
            p.clg_yr =  clg_yr
            p.age = age
            p.deg = degree
            p.save()
            print(p.author_name)
        else:
            p.save() 
        messages.success(request,'Profile updated successfully!')
        return redirect('profile_show')
    else:
        # p = Profile.objects.filter(author_real=request.user)[0]
        form = CreateProfile()
        
        return render(request,'update_profile.html',context={"form":form})
    
def create_post(request):
    profile_inst = Profile.objects.filter(author_real=request.user).first()

    print(profile_inst)

    if request.method == 'POST':
        print('POST request')
        form = CreatePost(request.POST,request.FILES)
        if form.is_valid():
            print(request.FILES)
            post=form.save(commit=False)
            post.post_id = Post.objects.all().count() + 1
            post.author = profile_inst
            post.save()
        messages.success(request,'Posted successfully!')
        return redirect("/")
                
    else:
        print('JUST a VISIT!')
        form=CreatePost(initial={'author':profile_inst})
    
    return render(request,'create_post.html',{'form':form})

def profile(request):
    profile = Profile.objects.filter(author_real=request.user).first()

    return render(request,'profile_show.html',{'profile':profile})

def delete_post(request):
    post_id = request.GET.get('post_id')
    post = Post.objects.filter(id=post_id).first()
    if request.method == "POST":
        print("POST REQUEST")
        post.delete()
        messages.success(request,"Post deleted successfully!")
        return redirect('/')
    else:
           
        return render(request,'delete_post.html',{"post":post})

def user_posts(request,user_id):
    print(user_id)
    user = User.objects.filter(id=user_id).first()
    print(user)
    profile = Profile.objects.filter(author_real=user).first()
    print(profile)
    posts = Post.objects.all().filter(author=profile)
    
    return render(request,'user_posts.html',{"profile":profile,"posts":posts})