from django.contrib import admin
from django.urls import path, re_path
from app import views

urlpatterns = [

    path('admin/', admin.site.urls),

    # user URL
    path('login_user/', views.login_user, name='login_user'),#login_user
    path('reg_user/', views.reg_user, name='reg_user'),#user register
    path('home_user/<str:category>/', views.home_user, name='home_user'),  # home_user
    path('course_detail/<int:id>/', views.course_detail, name='course_detail'),  # course_detail
    path('my_comment/', views.my_comment, name='my_comment'),  # my_comment
    path('my_comment_guanli/', views.my_comment_guanli, name='my_comment_guanli'),
    path('home_test/<int:id>/', views.home_test, name='home_test'),  # home_test
    path('test_detail/<int:id>/', views.test_detail, name='test_detail'),  # test_detail
    path('logout/', views.logout, name='logout'),  # logout

    # teacher URL
    path('login_teacher/', views.login_teacher, name='login_teacher'),# login_teacher
    path('reg_teacher/', views.reg_teacher, name='reg_teacher'),# reg_teacher
    path('home_teacher/<str:category>/', views.home_teacher, name='home_teacher'),  # home_teacher
    path('uploat_course/', views.uploat_course, name='uploat_course'),  # uploat_course
    path('edit_course/<int:id>/', views.edit_course, name='edit_course'),  # edit_course
    path('delete_course/<int:id>/', views.delete_course, name='delete_course'),  # delete_course
    path('sub_examination/<int:id>/', views.sub_examination, name='sub_examination'),  # sub_examination
    path('teacher_course_detail/<int:id>/', views.teacher_course_detail, name='teacher_course_detail'),  # teacher_course_detail
    path('logout_teacher/', views.logout_teacher, name='logout_teacher'),  # logout_teacher
]