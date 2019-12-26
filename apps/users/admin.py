from django.contrib import admin

# Register your models here.


import xadmin

from .models import  UserProfile,VerifyCode


import xadmin
from xadmin import views
from .models import VerifyCode


class BaseSetting(object):
    #添加主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    #全局配置，后台管理标题和页脚
    site_title = "仙剑奇侠传"
    site_footer = "http://www.cnblogs.com/derek1184405959/"
    #菜单收缩
    menu_style = "accordion"


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', "add_time"]
# #xadmin中这里是继承object，不再是继承admin
# class userAdmin(object):
#     pass

# xadmin.site.register(UserProfile,userAdmin)
xadmin.site.register(VerifyCode,VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)