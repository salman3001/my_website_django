from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.BlogListView.as_view(), name="index"),
    path("<slug:slug>/", views.BlogDetailView.as_view(), name="detail"),
    path("tag/<str:tag>/", views.BlogListByTagView.as_view(), name="index-by-tag"),
    path(
        "category/<slug:slug>/",
        views.BlogListByTagView.as_view(),
        name="index-by-category",
    ),
]
