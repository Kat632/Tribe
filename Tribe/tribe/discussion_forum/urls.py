from django.urls import path
from discussion_forum.views import *


urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('forumHome/', forumHome, name='forumHome'),
    path('', views.discussion_forum, name='forumHome'),
    path('addInForum/', addInForum, name='addInForum'),
    path('addInDiscussion/', addInDiscussion, name='addInDiscussion'),
]
