# from django.urls import path
# from .import views

# urlpatterns = [
#     path('',views.work,name='work'),
#     path('api/projects/', views.project_list_api, name='project_list_api'),
# ]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, portfolio

router = DefaultRouter()
router.register('projects', ProjectViewSet, basename='project')

urlpatterns = [
    path('api/', include(router.urls)),   # → Your REST API
    path('', portfolio, name='portfolio'),  # → Your frontend page
]


