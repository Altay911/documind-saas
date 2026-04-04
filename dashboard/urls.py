from django.urls import path
from . import views

urlpatterns = [
    # When someone goes to the base URL, trigger the dashboard_home view
    path('', views.dashboard_home, name='dashboard_home'),
    path('register/', views.register , name='register'), # the new sign-up route.
    path('chat/<int:doc_id>/', views.chat_with_pdf, name='chat_with_pdf'),
    path('delete/<int:doc_id>/', views.delete_document, name='delete_document'),
    path('rename/<int:doc_id>/', views.rename_document, name='rename_document'),
]