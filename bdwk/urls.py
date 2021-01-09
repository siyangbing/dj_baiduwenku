from django.urls import path,re_path

from bdwk import views

urlpatterns = [
    path('file_down/', views.file_down, name='file_down'),
    # path('wait_html/', views.wait_html,name = "wait_html"),
    path('download_doc/', views.download_doc, name='download_doc'),

]
