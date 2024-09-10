from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views as mv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    # customer
    path('login/customer', mv.customer_login_view, name='customer_login'),
    path('register/customer', mv.customer_register_view, name='customer_register'),
    path('forgot/customer', mv.customer_forgot_pass_view, name='customer_forgot_pass'),
    # seller
    path('login/seller', mv.seller_login_view, name='seller_login'),
    path('register/seller', mv.seller_register_view, name='seller_register'),
    path('forgot/seller', mv.seller_forgot_pass_view, name='seller_forgot_pass'),
    # common to both
    path('logout', mv.logout_view, name='logout'),
    # index
    path('', mv.home_view, name='home'),
    path('cat/<slug:name>', mv.category_view, name='category'),
    path('detail/<int:id>', mv.detail_view, name='detail'),
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)