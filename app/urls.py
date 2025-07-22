from django.urls import path,include
# ai_tool_hub/app/urls.py
from .router import router
from .import views
urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls))
] 