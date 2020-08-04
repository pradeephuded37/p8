from django.urls import path
from profileapp import views
app_name="profileapp"

urlpatterns = [
    path('trail/',views.trial,name="Trial"),
    path('profile/',views.profile,name="profile"),
]