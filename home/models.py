from django.db import models


# 用户数据表
class User(models.Model):
    class Meta:
        verbose_name = "普通用户"
        verbose_name_plural = "普通用户"
    username = models.CharField(max_length=32, unique=True, verbose_name="用户名")#不可以重复
    password = models.CharField(max_length=32, verbose_name="密码")
    nick_name = models.CharField(max_length=32, blank=True, null=True)
    gender = models.BooleanField(default=1, verbose_name="性别")
    phone = models.CharField(max_length=32, blank=True, null=True, unique=True, verbose_name="手机号")
    email = models.EmailField(blank=True, null=True, unique=True, verbose_name="邮箱")
    address = models.TextField(blank=True, null=True, verbose_name="地质")
    image = models.ImageField(upload_to='upload/user', default='upload/user/!happy-face.png', verbose_name="用户头像")



# 站台表
class City(models.Model):
    class Meta:
        verbose_name = "城市"
        verbose_name_plural = "城市"

    city_name = models.CharField("城市名称", max_length=30, unique=True)
    city_number = models.IntegerField(verbose_name="城市编号", unique=True)

    def __str__(self):
        return self.city_name



# 站台表
class Site(models.Model):
    class Meta:
        verbose_name = "站台"
        verbose_name_plural = "站台"

    site_name = models.CharField("站台名称", max_length=30,unique=True)
    site_number = models.IntegerField(unique=True, verbose_name = "站台编号")
    city = models.ForeignKey("City", on_delete=models.CASCADE)

    def __str__(self):
        return self.site_name


# 公交类别
class BusType(models.Model):
    class Meta:
        verbose_name = "公交类型"
        verbose_name_plural = "公交类型"

    type_name = models.CharField(verbose_name="类型名称", max_length=30, unique=True)
    add_time = models.DateTimeField(verbose_name="添加时间", auto_now=True)
    def __str__(self):
        return self.type_name


# 公交表
class Bus(models.Model):
    class Meta:
        verbose_name = "公交"
        verbose_name_plural = "公交"

    bus_name = models.CharField(verbose_name="公交名称", max_length=30, unique=True)
    start_time = models.TimeField(verbose_name="发车时间")
    end_time = models.TimeField(verbose_name="停运时间")
    money =  models.FloatField(verbose_name="价钱")
    status = models.BooleanField(verbose_name="运营状态",default=1)
    add_time = models.DateTimeField(verbose_name="发车时间", auto_now=True)
    city = models.ForeignKey("City", on_delete=models.CASCADE, default=1, verbose_name="城市")
    type = models.ForeignKey("BusType", on_delete=models.CASCADE, default=1, verbose_name="公交类型")
    def __str__(self):
        return self.bus_name



# 公交-站台
class BusSite(models.Model):
    class Meta:
        verbose_name = "公交-站台"
        verbose_name_plural = "公交-站台"

    bus = models.ForeignKey("Bus", on_delete=models.CASCADE, verbose_name="公交")
    site = models.ForeignKey("Site", on_delete=models.CASCADE, verbose_name="站台")
    level = models.IntegerField("等级")
    station_time = models.IntegerField("距上一站时间", default=5)


# 站台搜索历史
class SiteHistory(models.Model):
    class Meta:
        verbose_name = "站台浏览历史"
        verbose_name_plural = "站台浏览历史"

    site = models.ForeignKey("Site", on_delete=models.CASCADE, verbose_name="站台")
    count = models.IntegerField(verbose_name="查询次数")
    user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="用户")


# 公交浏览记录
class BusHistory(models.Model):
    class Meta:
        verbose_name = "公交浏览历史"
        verbose_name_plural = "公交浏览历史"

    bus = models.ForeignKey("Bus", on_delete=models.CASCADE,verbose_name="公交")
    count = models.IntegerField(verbose_name="查询次数")
    user = models.ForeignKey("User", on_delete=models.CASCADE,verbose_name="用户")
