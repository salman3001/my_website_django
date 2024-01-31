from django.conf import settings


def master_template(request):
    return {
        "master_template": "core/base-dev.html" if settings.DEBUG else "core/base.html"
    }
