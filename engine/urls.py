from django.urls import path

from . import views

urlpatterns = [
    path('', views.start_page, name='start'),

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.create_user, name='register'),

    path('intro/', views.intro1, name='intro'),
    path('intro/start/', views.intro2, name='intro2'),

    path('laboratory/', views.lab, name='laboratory3d'),
    path('laboratory3D/', views.lab_3d, name='laboratory'),
    path('laboratory/table/', views.lab_table, name='table'),
    path('laboratory/table/', views.lab_table, {'watch': True}, name='table+'),
    path('laboratory/table/video/', views.lab_table_video, name='table_v'),
    path('laboratory/table/paper/', views.lab_table_paper, name='table_p'),
    path('laboratory/table/news/', views.lab_table_news, name='table_n'),
    path('laboratory/table/news/solve', views.lab_table_news_check, name='check_news'),


    path('laboratory/tv/', views.lab_tv, name='tv'),
    path('laboratory/tv/video/animals', views.lab_tv_video, {'video': 1}, name='tv_v1'),
    path('laboratory/tv/video/mutations', views.lab_tv_video, {'video': 2}, name='tv_v2'),
    path('laboratory/tv/puzzle/', views.lab_tv_puzzle, name='tv_puzzle'),

    path('laboratory/probes/', views.lab_probes, name='probes'),
    path('laboratory/probes/solve', views.lab_probes_check, name='check_probes'),

    path('laboratory/reagents/', views.lab_reagents, name='reagents'),

    path('laboratory/suites/', views.lab_suites, name='suites'),



    # path('main/', views.main, name='main'),
]