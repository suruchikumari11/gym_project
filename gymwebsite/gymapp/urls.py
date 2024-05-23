from django.urls import path
from .  import views
urlpatterns = [
    path('',views.home,name="home"),
    path('admin/',views.admin,name="admin"),
    path('login/', views.login_page, name='login_page'), 
    path('logout/',views.logout_view,name="logout"),    
    path('register/', views.register_page, name='register'),
    path('gallery/',views.gallery,name="gallery"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('wellness/',views.wellness,name='wellness'),
    path('personal/',views.personal,name='personal'),
    path('group/',views.group,name='group'),
    path('buymembershipform/',views.buymembershipform,name='buymembershipform'),
    path('showplan/',views.showplan,name='showplan'),
    path('profile/',views.profile,name='profile'),
]
