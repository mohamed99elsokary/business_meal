from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication

from business_meal.swagger import CustomOpenAPISchemaGenerator

# URL settings

main_patterns = i18n_patterns(
    path("admin/", admin.site.urls),
    path("api/", include("business_meal.notificationapp.urls")),
    path("api/", include("business_meal.order_app.urls")),
    path("api/", include("business_meal.hotel_app.urls")),
    path("api/", include("business_meal.openbuffet_app.urls")),
    path("api/", include("business_meal.resturant_app.urls")),
    path("api/", include("business_meal.userapp.urls")),
    path("api/", include("business_meal.addonsapp.urls")),
)
urlpatterns = main_patterns


# Health url
urlpatterns += [path("health/", lambda res: HttpResponse("good"))]


# swagger urls and configuration
schema_view = get_schema_view(
    openapi.Info(
        title="business_meal API",
        default_version="v1",
        description="business_meal Swagger Documentation",
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
    authentication_classes=(SessionAuthentication,),
    generator_class=CustomOpenAPISchemaGenerator,
    patterns=main_patterns,
)
urlpatterns += [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
