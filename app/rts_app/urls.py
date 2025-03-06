# rts_app/urls.py
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app.rts_app.views.login_view import user_login, user_logout  # Correcte import voor home view
from app.rts_app.views.article_create_view import article_create_view, article_success_view  # Correcte import voor create_article view
from rts_app.views.register_view import user_register  # Correcte import voor register view
import rts_app.authentication.urls  # Correcte import voor authentication urls
from app.rts_app.views.home_view import home
from app.rts_app.views.stock_view import stock_view

urlpatterns = [
    path('', user_login, name='login'),  # De loginpagina is de rootpagina
    path('home/', home, name='home'),
    path('create_article', article_create_view, name='create_article'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    path('create_article/', article_create_view, name='create_article'),
    path('stock/', stock_view, name='stock_page'),
    path("article_success/<int:articlenr>/", article_success_view, name="article_success"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)