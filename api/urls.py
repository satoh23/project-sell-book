from django.urls import path

from api.views.accounts import (LoginView, LogoutView, get_refresh_view,
                                EditUserView, EditUserNotIconView,
                                GetEmailView)

from api.views.article import (CreateView, CreateNotThumbnailView,
                               ListCategoryView, ListDetailView, GetDetailArticleView,
                               GetBodyView, BuyArticleView,
                               IsBoughtView)

from api.views.point import save_stripe_info

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('token-refresh/', get_refresh_view().as_view()),
    path('edit-user/', EditUserView.as_view()),
    path('edit-user-not-icon/', EditUserNotIconView.as_view()),
    path('get-email/', GetEmailView.as_view()),

    path('create-article/', CreateView.as_view()),
    path('create-article-not-thumbnail/', CreateNotThumbnailView.as_view()),
    path('get-list-article/', ListDetailView.as_view()),
    path('get-list-category/', ListCategoryView.as_view()),
    path('get-detail-article/<str:pk>/', GetDetailArticleView.as_view()),
    path('get-body/<str:pk>/', GetBodyView.as_view()),
    path('buy-article/', BuyArticleView.as_view()),
    path('is-bought-article/', IsBoughtView.as_view()),

    path('save-stripe-info/', save_stripe_info),
]
