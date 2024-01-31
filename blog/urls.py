from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.BlogListView.as_view(), name="list"),
    path("<slug:slug>/", views.BlogDetailView.as_view(), name="detail"),
    path("tag/<slug:slug>/", views.TagDetailView.as_view(), name="tag-detail"),
    path(
        "category/<slug:slug>/",
        views.TagDetailView.as_view(),
        name="category-detail",
    ),
]
