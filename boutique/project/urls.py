from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from shop.views import CategoryViewSet, ProductViewSet, ArticleViewSet, AdminCategoryViewSet, AdminProductViewSet, AdminArticleViewSet

router = routers.SimpleRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('product', ProductViewSet, basename='product')
router.register('article', ArticleViewSet, basename='article')
router.register('admin/category', AdminCategoryViewSet, basename='admin-category')
router.register('admin/product', AdminProductViewSet, basename='admin-product')
router.register('admin/article', AdminArticleViewSet, basename='admin-article')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]
