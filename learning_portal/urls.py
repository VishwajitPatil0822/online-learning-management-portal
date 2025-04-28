from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',home_view,name='home_view_urls'),
    path('about/',about_view,name='about_view_urls'),
    path('contact/',contact_us_view,name='contact_us_view_urls'),
    path('login/',login_view,name='login_view_urls'),
    path('create/',create_account_view,name='create_account_view_urls'),

    path('app_home/',app_home_view,name='app_home_view_urls'),
    path('app_my_learning/',my_learning_view,name='my_learning_view_urls'),
    path('delete_course/<int:course_id>/',delete_course_view,name='delete_course_view_urls'),
    path('app_about/',app_about_view,name='app_about_view_urls'),
    path('app_contact/',app_contact_us_view,name='app_contact_us_view_urls'),
    path('app_logout/',app_logout_view,name='app_logout_view_urls'),
    path('courses_details/<int:course_id>/', app_courses_details_view, name='app_courses_details_view_urls'),
    path('course/<int:course_id>/', app_course_view, name='app_course_view_urls'),
    path('course_categories/<int:category_id>/', app_course_categories_view, name='app_course_categories_view_urls'),
    path('account/', app_account_view, name='app_account_view_urls'),
    path("update-account/<int:account_id>/", app_update_account_view, name="app_update_account_view_urls"),
    path("delete-account/<int:account_id>/", app_delete_account_view, name="app_delete_account_view_urls"),

    path('quiz/<int:course_id>/', quiz_view, name='quiz_view_urls'),
    path('quiz_result/<int:course_id>/', quiz_result_view, name='quiz_result_view_urls'),
    path('certificate/<int:course_id>/', certificate_view, name='certificate_view_urls'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
