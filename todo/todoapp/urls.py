
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.add, name="add"),
     path('delete/<int:id>',views.deletes, name="deletes"),
          path('update/<int:id>/',views.update, name="update"),
          path('chome/',views.Tasklistview.as_view(),name='chome'),
          path('dhome/<int:pk>/',views.TaskDetail.as_view(),name='dhome'),
          path('udelete/<int:pk>/',views.TaskDelete.as_view(),name='udelete'),

   
    
]
