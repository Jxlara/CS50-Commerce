from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("home", views.home, name="home"),
    path("active_listing", views.active_listing, name="active_listing"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("view_listing/<int:product_id>", views.view_listing, name="view_listing"),
    path("categories", views.categories, name="categories"),
    path("add_to_watchlist/<int:product_id>", views.add_to_watchlist, name="add_to_watchlist"),
    path("add_comment/<int:product_id>", views.add_comment, name="add_comment"),
    path("category/<str:categ>", views.category, name="category"),
    path("close_bid/<int:product_id>", views.close_bid, name="close_bid"),
    path("closed_listing", views.closed_listing, name="closed_listing")
]