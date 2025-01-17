from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.handle_signup, name="signup"),
    path("home", views.home, name='home'),
    path("login", views.handle_login, name="login"),
    path("logout", views.handle_logout, name="logout"),
    path("add_expenses", views.add_expenses, name="add_expenses"),
    path("history", views.history, name="history"),
    path("delete_expense", views.delete_expense, name="delete_expense"),
    path("thirty_days", views.thirty_days_summary, name="thirty_days"),
    path("one_week", views.one_week_summary, name="one_week"),
    path("year_to_date", views.year_to_date_summary, name="year_to_date"),
    path("update_profile", views.update_profile, name="update_profile"),
]