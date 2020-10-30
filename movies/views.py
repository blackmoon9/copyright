from django.shortcuts import render
from .models import MovieInfo,Area,Language,Version,CopyRightinfo
from django.views.generic import View
from django.http import JsonResponse
# Create your views here.
def movies_list(request):
    context={}
    moviesinfolist = MovieInfo.objects.all()
    context['moviesinfolist']=moviesinfolist
    are=Area.objects.all()
    context['are']=are
    return render(request,"moviesinfo.html",context)

class AddressAPI(View):
    """地址信息"""

    def get(self, request, area_id):  # 接收一个参数的id, 指modde中的pid属性对应的字段,即表中的pid_id
        if int(area_id) == 0:  # 为0时表示为查询省 , 省的pid_id为null
            area_data = Area.objects.filter(pid__isnull=True).values('id', 'areaname')
        else:  # 查询市或者区县
            area_data = Area.objects.filter(pid_id=int(area_id)).values('id', 'address')
        area_list = []  # 转成list后json序列化
        for a in area_data:
            area_list.append({'id': a['id'], 'areaname': a['arename']})
        # 然后通过jsonResponse返回给请求方, 这里是list而不是dict, 所以safe需要传入False.
        return JsonResponse(area_list, content_type='application/json', safe=False)

def addmoviesinfo(request):
    if request.method == "GET":
        context={}
        context['area']=Area.objects.all()
        context['language']=Language.objects.all()
        context['version']=Version.objects.all()
        return render(request,"addmovies.html",context)
    else:
        indrudce=request.POST.get("indrudce")
        are=request.POST.get("b")
        print(indrudce,are)
        return render(request,"moviesinfo.html")

def copyright(request):
    context={}
    context['copyrightinfo']=CopyRightinfo.objects.all()
    return render(request,"copyrightinfo.html",context)

def searchcrinfo(request):
    serach=request.GET.get('search')
    if serach:
        serachreault=CopyRightinfo.objects.filter(name=serach)
    else:
        serachreault=''
    context={}
    context['serach']=serachreault
    return render(request,"search.html",context)

