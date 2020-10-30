from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Area(models.Model):
    areaname=models.CharField(max_length=50,verbose_name='地区名')

    class Meta:
        verbose_name = "地区"
        verbose_name_plural = verbose_name

    def __str__(self):
        return  self.areaname



class Version(models.Model):
    versionname=models.CharField(max_length=50,verbose_name='版本名')

    class Meta:
        verbose_name = "版本"
        verbose_name_plural = verbose_name

    def __str__(self):
        return  self.versionname

class Language(models.Model):
    language=models.CharField(max_length=50,verbose_name='语言名')

    class Meta:
        verbose_name = "语言"
        verbose_name_plural = verbose_name

    def __str__(self):
        return  self.language

class MovieInfo(models.Model):
    name=models.CharField(max_length=255,verbose_name='电影名')
    introduce=models.TextField(default="还没有任何介绍",verbose_name='电影简介')
    dubbing=models.ForeignKey(Language,on_delete=models.CASCADE,related_name='dubbing',verbose_name='配音')
    subtitle=models.ForeignKey(Language,on_delete=models.CASCADE,related_name='subtitle',verbose_name='字幕')
    area=models.ForeignKey(Area,on_delete=models.CASCADE,verbose_name='地区')
    time=models.CharField(max_length=50,verbose_name='时长')
    version=models.ForeignKey(Version,on_delete=models.CASCADE,verbose_name='版本')

    class Meta:
        verbose_name = "电影信息"
        verbose_name_plural = verbose_name

class RightInfo(models.Model):
    name=models.CharField(max_length=50,verbose_name="权限名")
    description=models.TextField(verbose_name="权利描述")
    bankruptcy=models.TextField(verbose_name="破产条例描述")
    class Meta:
        verbose_name = "权利信息"
        verbose_name_plural = verbose_name

class Orderinfo(models.Model):
    price=models.DecimalField(max_digits=6,decimal_places=2,verbose_name="价格")
    userid=models.ForeignKey(User,related_name="buyuser",on_delete=models.CASCADE,verbose_name="买家")
    sellid=models.ForeignKey(User,related_name='selluser',on_delete=models.CASCADE,verbose_name="卖家")
    paystyle=models.CharField(max_length=255,verbose_name="支付方式")
    class Meta:
        verbose_name = "订单信息"
        verbose_name_plural = verbose_name

class CopyRightinfo(models.Model):
    name=models.CharField(max_length=50,verbose_name="版权名称")
    chain=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,verbose_name="版权链")
    movies_info=models.ForeignKey(MovieInfo,on_delete=models.CASCADE,verbose_name="电影信息")
    right=models.ForeignKey(RightInfo,on_delete=models.CASCADE,verbose_name="权限")
    oder=models.ForeignKey(Orderinfo,on_delete=models.CASCADE,verbose_name="订单信息")
    star_time=models.DateTimeField(verbose_name="开始时间")
    end_time=models.DateTimeField(verbose_name="结束时间")
    warning=models.BooleanField(verbose_name="是否开启预警")
    warning_time=models.IntegerField(verbose_name="预警时间")
    remark=models.CharField(max_length=255,verbose_name="备注",null=True)
    class Meta:
        verbose_name = "版权信息管理"
        verbose_name_plural = verbose_name


# class GroupConcat(models.Aggregate):
#     """自定义实现聚合功能，实现GROUP_CONCAT功能"""
#
#     function = 'GROUP_CONCAT'
#     template = '%(function)s(%(distinct)s%(expressions)s%(ordering)s%(separator)s)'
#     allow_distinct = True
#     def __init__(self, expression, distinct=False, ordering=None, separator=',', **extra):
#         super(GroupConcat, self).__init__(expression,
#                                           distinct='DISTINCT ' if distinct else '',
#                                           ordering=' ORDER BY %s' % ordering if ordering is not None else '',
#                                           separator=' SEPARATOR "%s"' % separator,
#                                           output_field=models.CharField(), **extra)

