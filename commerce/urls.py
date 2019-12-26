"""commerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from commerce.settings import MEDIA_ROOT
from goods.view_base import GoodsListView
from goods.views import GoodsListViewSet, CategoryViewSet

router = DefaultRouter()

#配置goods的url
router.register(r'goods', GoodsListViewSet,basename='goods')
# 配置Category的url
router.register(r'categorys', CategoryViewSet, basename="categorys")
# # 配置codes的url
# router.register(r'code', SmsCodeViewset, basename="code")
# #配置用户的url
# router.register(r'users', UserViewset, basename="users")
# # 配置用户收藏的url
# router.register(r'userfavs', UserFavViewset, basename="userfavs")
# # 配置用户留言的url
# router.register(r'messages', LeavingMessageViewset, basename="messages")
# # 配置收货地址
# router.register(r'address',AddressViewset , basename="address")
# # 配置购物车的url
# router.register(r'shopcarts', ShoppingCartViewset, basename="shopcarts")
# # 配置订单的url
# router.register(r'orders', OrderViewset, basename="orders")
# # 配置首页轮播图的url
# router.register(r'banners', BannerViewset, basename="banners")
# # 热搜词
# router.register(r'hotsearchs', HotSearchsViewset, basename="hotsearchs")
# # 首页系列商品展示url
# router.register(r'indexgoods', IndexCategoryViewset, basename="indexgoods")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    # path('', include('user_operation.urls')),
    path('xadmin/', xadmin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    path('docs',include_docs_urls(title='仙剑奇侠传')),
    re_path('^', include(router.urls)),
    path('jwt-auth/', obtain_jwt_token ),
    path('login/', obtain_jwt_token )
]
