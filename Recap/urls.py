from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from   .import views

urlpatterns = [
    path('',views.student_list,name='student_list'),
    path('add/',views.add_student,name='add'),
    path('edit/<int:student_id>/', views.edit_student, name='edit'),
    path('delete/<int:student_id>/',views.delete_student,name='delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)