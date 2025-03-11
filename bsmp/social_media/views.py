from django.shortcuts import render, redirect, get_object_or_404
from .models import  Post, Comment, Category,Like
from django.contrib.auth.decorators import login_required

def social_media(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST['title']
            content = request.POST['content']
            category_id = request.POST['category']
            category = get_object_or_404(Category, id=category_id)
            
            return redirect('social_media')
        posts = Post.objects.all()
        return render(request, 'all_posts.html', {'posts': posts})
    else:
        return redirect('login')

def create_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST['title']
            content = request.POST['content']
            category_id = request.POST['category']
            category = get_object_or_404(Category, id=category_id)
            Post.objects.create(
                title=title,
                content=content,
                category=category,
                user=request.user
            )
            return redirect('social_media')
        categories = Category.objects.all()
        return render(request, 'create_post.html', {'categories': categories})
    else:
        return redirect('login')

def update_post(request, id):
    my_post = get_object_or_404(Post, id=id, user=request.user)
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        category_id = request.POST['category']
        category = get_object_or_404(Category, id=category_id)
        my_post.title = title
        my_post.content = content
        my_post.category = category
        my_post.save()
        return redirect('social_media')
    return render(request, 'update.html', {'social_media': my_post})

def delete_post(request, id):
    my_post = get_object_or_404(Post, id=id, user=request.user)
    my_post.delete()
    return redirect('social_media')

def create_comment(request, id):
    my_post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(
            post=my_post,
            content=content,
            user=request.user
        )
        return redirect('single_post', id=my_post.id)
    return render(request, 'single_post.html', {'post': my_post})

def delete_comment(request, id):
    my_comment = get_object_or_404(Comment, id=id, user=request.user)
    my_comment.delete()
    return redirect('social_media')

def single_post(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'single_post.html', {'post': post, 'comments': comments})

def user_dashboard(request):
    user = request.user
    user_posts = Post.objects.filter(user=user)
    return render(request, 'user_dashboard.html', {'user': user, 'posts': user_posts})

def posts_by_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    posts = Post.objects.filter(category=category)
    return render(request, 'posts_by_category.html', {'category': category, 'posts': posts})

@login_required
def like_post(request, id):
    post = get_object_or_404(Post, id=id)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if not created:
        like.delete()
    return redirect('single_post', id=id)