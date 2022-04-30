from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
from .views import by_category, product_detail, delivery, index, order, support

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/<slug:slug>', product_detail, name='product_detail'),
    path('delivery/', delivery, name='delivery'),
    path('order/', order, name='order'),
    path('support/', support, name='support'),
    path('<slug:category_slug>/', index, name='by_category'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
