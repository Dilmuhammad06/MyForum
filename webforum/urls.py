from django.urls import path
from . import views


urlpatterns = [
    path('',views.IndexView.as_view(),name='home'),
    path('treads/<int:category_id>/',views.TreadsView.as_view(),name='treads'),
    path('posts/<tread_id>/',views.PostsView.as_view(),name='posts'),

]
