from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.BlogList.as_view(), name="list"),
    path(
        "search/",
        views.BlogListBySearch.as_view(),
        name="list-by-search",
    ),
    path(
        "create/",
        views.BlogCreate.as_view(),
        name="create",
    ),
    path("<slug:slug>/", views.BlogDetail.as_view(), name="detail"),
    path("tag/<slug:slug>/", views.BlogListByTag.as_view(), name="list-by-tag"),
    path(
        "category/<slug:slug>/",
        views.BlogListByCategory.as_view(),
        name="list-by-category",
    ),
]
