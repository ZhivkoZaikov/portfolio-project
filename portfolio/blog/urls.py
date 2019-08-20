from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('blog/', include('blog.urls')),
    path('', views.allblogs, name='allblogs'),
    path('<str:slug>/', views.detail, name='detail'),
#     declare static media files
]
