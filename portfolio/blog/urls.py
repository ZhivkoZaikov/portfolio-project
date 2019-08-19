from django.urls import path
from .views import index_view

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('blog/', include('blog.urls')),
    path('', index_view)
#     declare static media files
]
