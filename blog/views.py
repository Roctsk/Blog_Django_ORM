from django.shortcuts import render ,get_object_or_404

from blog.models import Post,Author

def post_list(request):
    posts = Post.objects.all().order_by('-published_date')

    return render( request, "post_list.html" ,{"posts":posts})

def post_detail(request,pk):
    posts = get_object_or_404(Post,pk=pk)

    return render( request, "post_detail.html" ,{"post":posts})


def post_by_author(request,author_id):
    author = get_object_or_404(Author,pk=author_id)
    posts = Post.objects.filter(author = author)
    return render( request, "post_by_author.html" ,{"post":posts},{"author":author})