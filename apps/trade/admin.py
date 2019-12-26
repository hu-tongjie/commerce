from django.contrib import admin

# Register your models here.

# import xadmin
#
# from .models import ShoppingCart,OrderGoods,OrderInfo
#
# #xadmin中这里是继承object，不再是继承admin
# class tradeAdmin(object):
#     pass
#
# xadmin.site.register(ShoppingCart,tradeAdmin)
# xadmin.site.register(OrderInfo,tradeAdmin)
# xadmin.site.register(OrderGoods,tradeAdmin)

import xadmin
from .models import ShoppingCart, OrderInfo, OrderGoods


class ShoppingCartAdmin(object):
    list_display = ["user", "goods", "nums", ]


class OrderInfoAdmin(object):
    list_display = ["user", "order_sn",  "trade_no", "pay_status", "post_script", "order_mount",
                    "order_mount", "pay_time", "add_time"]

    class OrderGoodsInline(object):
        model = OrderGoods
        exclude = ['add_time', ]
        extra = 1
        style = 'tab'

    inlines = [OrderGoodsInline, ]


xadmin.site.register(ShoppingCart, ShoppingCartAdmin)
xadmin.site.register(OrderInfo, OrderInfoAdmin)