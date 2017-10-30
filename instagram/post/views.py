from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

from member.decorators import login_required
from post.forms import PostForm, CommentForm
from post.models import Post, PostComment


def post_list(request):
    posts = Post.objects.all()
    comment_form = CommentForm()
    context = {
        'posts': posts,
        'comment_form': comment_form,
    }

    return render(request, 'post/post_list.html', context)


def post_detail(request, post_pk):
    post = get_object_or_404(
        Post,
        pk=post_pk
    )
    comment_form = CommentForm()
    context = {
        'post': post,
        'comment_form': comment_form,
    }
    return render(request, 'post/post_detail.html', context)


@login_required
def post_add(request):
    """
    post 추가 기능
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post:post_list')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'post/post_form.html', context)


def post_delete(request, post_pk):
    if request.method == 'POST':
        post = get_object_or_404(
            Post,
            pk=post_pk,
        )
        if post.author == request.user:
            post.delete()
            return redirect('post:post_list')
        else:
            raise PermissionDenied('작성자가 아닙니다')


@login_required
def post_like_toggle(request, post_pk):
    if request.method == 'POST':
        next_path = request.GET.get('next')
        post = get_object_or_404(Post, pk=post_pk)
        user = request.user
        filtered_like_posts = user.like_posts.filter(pk=post.pk)
        if filtered_like_posts.exists():
            user.like_posts.remove(user.like_posts.get(pk=post.pk))
        else:
            user.like_posts.add(post)

        if next_path:
            return redirect(next_path)
        return redirect('post:post_detail', post_pk=post_pk)


@login_required
def comment_add(request, pk):
    """
    comment 추가 기능
    :param request:
    :param pk: Post의 pk값
    :return:
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

            next1 = request.GET.get('next')
            if next1:
                return redirect(next1)
        return redirect('post:post_detail', post_pk=pk)


def comment_delete(request, comment_pk):
    next1 = request.GET.get('next')

    if request.method == 'POST':
        comment = get_object_or_404(
            PostComment,
            pk=comment_pk,
        )
        if comment.author == request.user:
            comment.delete()
            if next1:
                return redirect(next1)
            return redirect('post:post_detail', post_pk=comment.post.pk)
        else:
            raise PermissionDenied('작성자가 아닙니다')
