from django.urls import path

from .views import (
    CreateNoticeView, 
    CommentReactionAPIView, 
    AllNoticesView, 
    CommentDeleteAPIView, 
    NoticeDeleteAPIView, 
    EditNoticeAPIView, 
    RetrieveNoticeCommentsView, 
   
    ReactionList,
    ReactionDetail
)

from .views import CreateNoticeView, CommentReactionAPIView, AllNoticesView, CommentDeleteAPIView, NoticeDeleteAPIView, EditNoticeAPIView, RetrieveNoticeCommentsView, CommentCreateAPIView, UserNoticesView,CreateReactionAPIView


#add url routes here

urlpatterns = [

    path('notices/', CreateNoticeView.as_view()),

    path('all-notices', AllNoticesView.as_view()),

    path('user-notices/<int:user_id>', UserNoticesView.as_view()),

    path('comment/reaction/update', CommentReactionAPIView.as_view()),
    
    path('notice/update', EditNoticeAPIView.as_view()),

    path('comment/delete', CommentDeleteAPIView.as_view()),
    
    path('notice/delete', NoticeDeleteAPIView.as_view()),

    path('comment/get', RetrieveNoticeCommentsView.as_view()),

    
    
    path('reaction/', ReactionList.as_view()),
    path('reaction/<int:pk>/', ReactionDetail.as_view()),


    path('comment/create', CommentCreateAPIView.as_view()),

    path('react/', CreateReactionAPIView.as_view(), name='react')  # Enables the user to react to a comment

]

