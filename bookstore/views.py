from django.shortcuts import render
from .models import Sach, TacGia
from django.shortcuts import get_object_or_404
# Create your views here.

def danh_sach(request):
    sach = Sach.objects.all()
    context = {
        'sach':sach
    }
    return render(request, "bookstore/index.html",context)

def capnhat_sach(request, sach_id):
    sach = get_object_or_404(Sach, id = sach_id)
    tacgia = TacGia.objects.all()
    context = {
        'sach' : sach,
        'tacgia':tacgia
    }
    return render(request,"bookstore/capnhat-sach.html",context) 

def xu_ly_capnhat(request):
    if request.method == "POST":
        rq_sach_id = request.POST.get("sach_id")
        rq_ten_sach = request.POST.get("ten_sach")
        rq_gia = request.POST.get("gia")
        rq_tacgia = request.POST.get("tacgia")
        Sach.objects.filter(id=rq_sach_id).update(tenSach = rq_ten_sach, gia = rq_gia, tacGia = rq_tacgia)
        sach = Sach.objects.all()
        context = {
            'sach':sach
        }
        return render(request, "bookstore/index.html",context)

def timsach(request):        
    if request.method == 'POST': # this will be GET now      
        ten_sach =  request.POST.get('ten') # do some research what it does       
        sach = Sach.objects.filter(tenSach__icontains=ten_sach) # filter returns a list so you might consider skip except part
        context = {
            'sach':sach
         }
        return render(request, "bookstore/index.html",context)
    else:
        context = {
        'sach':""
         }
        return render(request,"bookstore/index.html",context)