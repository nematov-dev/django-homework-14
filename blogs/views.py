from typing import Any
from django.shortcuts import redirect,render
from django.views.generic import ListView,DetailView
from django.db.models import Q


from blogs import models


class BlogListView(ListView):
    template_name = 'blogs/blog.html'
    model = models.BlogModel
    context_object_name = 'blogs'
    paginate_by = 1

    def get_queryset(self):
        blogs = models.BlogModel.objects.all()
        cat = self.request.GET.get('cat')
        tag = self.request.GET.get('tag')
        q = self.request.GET.get('q')
        
        if cat:
            blogs = blogs.filter(categories=cat)
        if tag:
            blogs = blogs.filter(tags=tag)
        if q:
            blogs = blogs.filter(
                Q(title__icontains=q) | Q(short_description__icontains=q)
            )
       
        return blogs

    def get_context_data(self,*,object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        context['categories'] = models.BlogCategoryModel.objects.all()
        context['tags'] = models.BlogTagModel.objects.all()
        context['comments'] = models.BlogCommentModel.objects.all()
        return context


class BlogDetailView(DetailView):
    
    model = models.BlogModel
    template_name = "blogs/blog_detail.html"
    context_object_name = "blog"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['all_blogs'] = models.BlogModel.objects.all()
        context['categories'] = models.BlogCategoryModel.objects.all()
        context['tags'] = models.BlogTagModel.objects.all()
        context['comments'] = models.BlogCommentModel.objects.filter(blog=self.object)

        return context
    
    def post(self, request, *args, **kwargs):
        pass