from django.contrib import admin

# Register your models here.

import xadmin

from .models import  UserFav,UserAddress,UserLeavingMessage

#xadmin中这里是继承object，不再是继承admin
# class user_operationAdmin(object):
#     pass
#
# xadmin.site.register(UserFav,user_operationAdmin)
# xadmin.site.register(UserAddress,user_operationAdmin)
# xadmin.site.register(UserLeavingMessage,user_operationAdmin)

class UserFavAdmin(object):
    list_display = ['user', 'goods', "add_time"]


class UserLeavingMessageAdmin(object):
    list_display = ['user', 'message_type', "message", "add_time"]


class UserAddressAdmin(object):
    list_display = ["signer_name", "signer_mobile", "district", "address"]

xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserAddress, UserAddressAdmin)
xadmin.site.register(UserLeavingMessage, UserLeavingMessageAdmin)