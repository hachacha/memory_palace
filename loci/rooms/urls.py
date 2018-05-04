from django.urls import path



from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:room_iter>/', views.detail, name='detail'),#this is not roomid it should be iteration/placeholder in the derive.
	path('clear',views.clear_session, name='clear_session'),
]