from django import forms

from blog.models import Blog


class BlogSearchForm(forms.Form):
    search = forms.CharField(
        min_length=2,
        max_length=20,
        widget=forms.TextInput(
            attrs={"placeholder": "Search Blogs"},
        ),
    )


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
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
