from django.urls import reverse_lazy
from .models import Blog, Category, Tag
from django.views.generic import ListView, DetailView, CreateView
from .forms import BlogSearchForm, CreateBlogForm
from django import forms

# Create your views here.


class BlogList(ListView):
    base_template = "web/base.html"
    model = Blog
    context_object_name = "blogs"
    template_name = "blog/bloglist.html"
    paginate_by = 20
    search_form = BlogSearchForm()

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["base_template"] = self.base_template
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
    base_template = "web/base.html"
    model = Blog
    context_object_name = "blog"
    template_name = "blog/blog_detail.html"
    slug_field = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["base_template"] = self.base_template
        return context


class BlogCreate(CreateView):
    model = Blog
    template_name = "blog/blog_create.html"
    base_template = "web/base.html"
    form_class = CreateBlogForm
    success_url = reverse_lazy("blog:list")

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["base_template"] = self.base_template
        return context
