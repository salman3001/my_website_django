from django import forms


class BlogSearchForm(forms.Form):
    search = forms.CharField(
        min_length=2,
        max_length=20,
        widget=forms.TextInput(
            attrs={"placeholder": "Search Blogs"},
        ),
    )
