from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from blog import views as blogViews

app_name = "web"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path(
        "blogs/",
        blogViews.BlogList.as_view(template_name="web/blogs/blog_list.html"),
        name="blogs",
    ),
    path(
        "blogs/search/",
        blogViews.BlogListBySearch.as_view(
            template_name="web/blogs/blog_list_by_search.html"
        ),
        name="blogs_by_search",
    ),
    path(
        "blogs/category/<slug:slug>/",
        blogViews.BlogListByCategory.as_view(
            template_name="web/blogs/blog_list_by_category.html"
        ),
        name="blogs_by_category",
    ),
    path(
        "blogs/tag/<slug:slug>/",
        blogViews.BlogListByTag.as_view(
            template_name="web/blogs/blog_list_by_tag.html"
        ),
        name="blogs_by_tag",
    ),
    path(
        "blogs/<slug:slug>/",
        blogViews.BlogDetail.as_view(template_name="web/blogs/blog_detail.html"),
        name="blog_detail",
    ),
    path("login/", views.Login.as_view(), name="login"),
    path("signup/", views.Signup.as_view(), name="signup"),
    path("logout_confirm/", views.LogoutConfirm.as_view(), name="logout_confirm"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("password_change/", views.PasswordChange.as_view(), name="password_change"),
    path(
        "password_change_done/",
        views.PasswordChangeDone.as_view(),
        name="password_change_done",
    ),
    path("password_reset/", views.PasswordReset.as_view(), name="password_reset"),
    path(
        "password_reset_done/",
        views.PasswordResetDone.as_view(),
        name="password_reset_done",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>/",
        views.PasswordResetConfirm.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_complete/",
        views.PasswordResetComplete.as_view(),
        name="password_reset_complete",
    ),
]
