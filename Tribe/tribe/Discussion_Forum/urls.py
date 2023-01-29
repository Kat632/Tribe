from django.contrib import admin
from django.urls import path
from Discussion_Forum.views import *
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('forumHome/', forumHome, name='forumHome'),
    path('addInForum/', addInForum, name='addInForum'),
    path('addInDiscussion/', addInDiscussion, name='addInDiscussion'),
]
