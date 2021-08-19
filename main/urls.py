
from django.urls import path

from .views import *

urlpatterns = [
   path('', MainPageView.as_view(), name='home'),
   path('category/<str:slug>/', Category_detail_view.as_view(), name='category'),
   path('post-detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
   path('add-post/', add_post, name='add-post'),
   path('update_post/<int:pk>/', update_post, name='update-post'),
   path('delete-post/<int:pk>/',  DeletePostView.as_view(), name='delete-post'),
   path('comment/<int:pk>/', post_detail, name='comment-add'),

]
