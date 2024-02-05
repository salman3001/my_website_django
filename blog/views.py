from django import forms
from django.urls import reverse_lazy
from .models import Blog, Category, Tag
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import BlogSearchForm
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


class BlogList(ListView):
    model = Blog
    paginate_by = 20
    search_form = BlogSearchForm()

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["search_form"] = self.search_form
        return context


class BlogListByCategory(BlogList):
    template_name = "blog/blog_list_by_category.html"

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(category__slug=self.kwargs.get("slug"))

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.get(slug=self.kwargs.get("slug"))
        return context


class BlogListByTag(BlogList):
    template_name = "blog/blog_list_by_tag.html"

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(tags__slug=self.kwargs.get("slug"))

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["tag"] = Tag.objects.get(slug=self.kwargs.get("slug"))
        return context


class BlogListBySearch(BlogList):
    template_name = "blog/blog_list_by_search.html"

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(title__icontains=self.request.GET.get("search"))

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["search_form"] = BlogSearchForm(self.request.GET)
        return context


class BlogDetail(DetailView):
    model = Blog
    slug_field = "slug"


class BlogCreate(SuccessMessageMixin, CreateView):
    model = Blog
    base_template = "web/base.html"
    success_url = reverse_lazy("blog:list")
    success_message = "Blog Created Successfully"
    fields = [
        "title",
        "slug",
        "short_desc",
        "image",
        "published",
        "featured",
        "category",
        "tags",
        "content",
        "meta_title",
        "meta_keywords",
        "meta_desc",
        "meta_struct_data",
    ]


class BlogEdit(SuccessMessageMixin, UpdateView):
    model = Blog
    success_url = reverse_lazy("blog:list")
    success_message = "Blog Updated Successfully"
    fields = [
        "title",
        "slug",
        "short_desc",
        "image",
        "published",
        "featured",
        "category",
        "tags",
        "content",
        "meta_title",
        "meta_keywords",
        "meta_desc",
        "meta_struct_data",
    ]

    widgets = {
        "tags": forms.CheckboxSelectMultiple,  # Use the appropriate widget for ManyToManyField
    }


class BlogDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:list")
