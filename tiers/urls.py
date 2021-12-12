from django.urls import path,re_path

from . import views

app_name = 'tiers'
urlpatterns = [

    path('tier/<int:level>/', views.tier, name='tier'),
    path('tier_submit/', views.tier_submit, name='tier_submit'),
    re_path(r'^tierM/(?P<id>\d+)/(?P<num>-?\d+)/$', views.tierMView.as_view(), name='tierM'),
    # path('tierM/<int:level>/<int:num>/', views.tierMView.as_view(), name='tierM'),
    # path('tierM/<int:level>/<int:num>/', views.tierM, name='tierM'),
    # path('tierA/<int:level>/<int:num>/', views.levelA, name='tierA'),
    # path('tier/', views.WordView.as_view(), name='tier'),
]