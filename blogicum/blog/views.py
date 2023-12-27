from django.shortcuts import render


def post_detail(request, pk):
    template = 'blog/detail.html'
    return render(request, template)


def category_posts(request):
    template = 'blog/category.html'
    return render(request, template)
