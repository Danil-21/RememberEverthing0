from django.urls import path
from . import views


app_name = 'mail'

urlpatterns = [
    path('send/', views.send_message, name='sendMessage'),
    path('inbox/', views.view_inbox, name='view_inbox'),
    path('outbox/', views.view_outbox, name='view_outbox'),
    path('message/<int:message_id>/', views.view_message, name='view_message'),
    path('move/<int:message_id>/', views.move_message, name='move_message'),
    path('delete/<int:message_id>/', views.delete_message, name='delete_message'),
    path('archive/', views.view_archive, name='view_archive'),
    path('trash/', views.view_trash, name='view_trash'),
]
