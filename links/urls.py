from django.urls import path, include

from . import views

app_name="links"

urlpatterns = [
    path('', views.AllLinks.as_view(), name='all'),
    path('category/<slug>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path("by/<username>/", views.UserAccount.as_view(), name="user_account"),
    path(
        "create/",
        views.LinkCreate.as_view(),
        name="create"
    ),
    path(
        "<slug>/update/",
        views.LinkUpdate.as_view(),
        name="update"
    ),
    path(
        "<slug>/delete/",
        views.LinkDelete.as_view(),
        name="delete"
    ),
    path(
        "<slug>/review/",
        views.ReviewCreate.as_view(),
        name="review"
    ),
    path('<slug>/', views.LinkDetailView.as_view(), name='detail'),

]
