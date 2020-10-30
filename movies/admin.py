from django.contrib import admin
from .models import MovieInfo,Area,Language,Version,CopyRightinfo,RightInfo,Orderinfo

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display =('id','areaname')

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id','versionname')

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id','language')

@admin.register(MovieInfo)
class MovieInfoAdmin(admin.ModelAdmin):
    list_display = ('id','introduce','dubbing','subtitle','area','time','version')

@admin.register(RightInfo)
class RightInfoAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','bankruptcy')
@admin.register(Orderinfo)
class OrderinfoAdmin(admin.ModelAdmin):
    list_display = ('id','price','userid','sellid','paystyle')
@admin.register(CopyRightinfo)
class CopyRightinfo(admin.ModelAdmin):
    list_display = ('id','name','chain','movies_info','right','oder','star_time','end_time','warning','warning_time','remark')