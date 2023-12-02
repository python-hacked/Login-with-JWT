from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .api import UserAPI, LoginAPIView

urlpatterns = [
    path("", views.index),
    path("login/", views.login),
    path("login_user/", views.login_user),
    path("table/", views.table),
    path("ragistration/", views.ragistration),
    path("add_product/", views.add_product),
    path("product/", views.product),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("update/<int:uid>/", views.update, name="update"),
    path("update_product/", views.update_product),


    # APi URL
    path("register/", UserAPI.as_view(), name="register"),
    path("api/login/", LoginAPIView.as_view(), name="api_login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
