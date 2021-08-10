
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/', include("job.urls",namespace="jobs")),
    path('', include("home.urls",namespace="home")),
    path('contact/', include("contact.urls")),
    path('accounts/', include("accounts.urls",namespace="accounts")),
    path('blog/', include("blog.urls",namespace="blog")),
    path('api/', include('rest_framework.urls')),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

