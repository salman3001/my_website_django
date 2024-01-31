from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Blog, Category, Tag
from django.views.generic import ListView, DetailView

# Create your views here.


class BlogListView(ListView):
    base_template = "web/base.html"
    model = Blog
    context_object_name = "blogs"
    template_name = "blog/blog_list.html"
    paginate_by = 1

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["base_template"] = self.base_template
        context["categories"] = Category.objects.all()
        return context


class BlogDetailView(DetailView):
    base_template = "web/base.html"
    model = Blog
    context_object_name = "blog"
    template_name = "blog/blog_detail.html"
    slug_field = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["base_template"] = self.base_template
        return context


class TagDetailView(DetailView):
    base_template = "web/base.html"
    model = Tag
    context_object_name = "tag"
    template_name = "blog/tag_detail.html"
    slug_field = "slug"

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["base_template"] = self.base_template
        context["categories"] = Category.objects.all()
        return context
