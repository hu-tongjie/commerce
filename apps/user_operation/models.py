from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
from datetime import datetime
from django.db import models
from goods.models import Goods
from django.contrib.auth import get_user_model
User = get_user_model()


class UserFav(models.Model):
    """
    用户收藏操作
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品", help_text="商品id")
    add_time = models.DateTimeField("添加时间",default=datetime.now)

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return self.user.username


class UserAddress(models.Model):
    """
    用户收货地址
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户" )
    province = models.CharField("省份",max_length=100, default="")
    city = models.CharField("城市",max_length=100, default="")
    district = models.CharField("区域",max_length=100, default="")
    address = models.CharField("详细地址",max_length=100, default="")
    signer_name = models.CharField("签收人",max_length=100, default="")
    signer_mobile = models.CharField("电话",max_length=11, default="")
    add_time = models.DateTimeField("添加时间",default=datetime.now)

    class Meta:
        verbose_name = "收货地址"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address


class UserLeavingMessage(models.Model):
    """
    用户留言
    """
    MESSAGE_CHOICES = (
        (1, "留言"),
        (2, "投诉"),
        (3, "询问"),
        (4, "售后"),
        (5, "求购")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    message_type = models.IntegerField(default=1, choices=MESSAGE_CHOICES, verbose_name="留言类型",
                                      help_text=u"留言类型: 1(留言),2(投诉),3(询问),4(售后),5(求购)")
    subject = models.CharField("主题",max_length=100, default="")
    message = models.TextField("留言内容",default="",help_text="留言内容")
    file = models.FileField(upload_to="message/images/", verbose_name="上传的文件", help_text="上传的文件")
    add_time = models.DateTimeField("添加时间",default=datetime.now)

    class Meta:
        verbose_name = "用户留言"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject













# class user(AbstractUser):
#     GENDER_CHOICES = (
#         ("male", u"男"),
#         ("female", u"女")
#     )
#     gender = models.CharField("性别", max_length=6, choices=GENDER_CHOICES, default="female")
#     # id = models.AutoField(primary_key=True)
#     # username = models.CharField(max_length=16,unique=True)
#     # email = models.EmailField()
#     # is_active = models.BooleanField(default=False)   # 是否激活
#     # # is_superuser = models.BooleanField(default=False) # 是否管理员
#
#     # objects = UserMangerOne()
#     # USERNAME_FIELD = 'username'
#     # REQUIRED_FIELDS = ['email']
#     class Meta():
#         db_tablespace = '用户'
#
# class address(models.Model):
#     id = models.AutoField(primary_key=True)
#     addressee = models.CharField("收件人",max_length=16)  # 收件人
#     address = models.CharField('收件地址',max_length=60)  # 收件地址
#     postcode = models.IntegerField('邮编')  # 邮编
#     contact_way = models.IntegerField('联系方式') # 联系方式
#     is_default = models.BooleanField('是否默认')  #   是否默认
#     users = models.ForeignKey('user',models.CASCADE,)  # 和用户一对多
#
#     class Meta():
#         db_tablespace = '地址'