from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Blog
from django.views.generic import ListView, DetailView

# Create your views here.


class BlogListView(ListView):
    base_template = "web/base.html"
    model = Blog
    context_object_name = "blogs"
    template_name = "blog/home.html"
    paginate_by = 20

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["base_template"] = self.base_template
        return context


class BlogListByTagView(ListView):
    base_template = "web/base.html"
    model = Blog
    context_object_name = "blogs"
    template_name = "blog/home.html"
    paginate_by = 20

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["base_template"] = self.base_template
        return context


class BlogDetailView(DetailView):
    base_template = "web/base.html"
    model = Blog
    context_object_name = "blog"
    template_name = "blog/detail.html"
    slug_field = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["base_template"] = self.base_template
        return context
