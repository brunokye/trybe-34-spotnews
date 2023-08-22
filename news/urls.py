from django.urls import path, include
from news.views import home, news_details, categories_form, news_form
from rest_framework import routers
from news_rest.views import categories_view, users_view

router = routers.DefaultRouter()
router.register(r'categories', categories_view.CategoriesViewSet)
router.register(r'users', users_view.UsersViewSet)

urlpatterns = [
    path('', home, name='home-page'),
    path('news/<int:id>', news_details, name="news-details-page"),
    path('categories/', categories_form, name="categories-form"),
    path('news/', news_form, name="news-form"),
    path('api/', include(router.urls))
]
