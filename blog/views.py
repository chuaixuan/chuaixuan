from django.shortcuts import render
from .models import Shopping_list
from .models import Purchased_goods
from django.http import HttpResponse
from django.http import JsonResponse
def homepage(request):
    return render(request, 'blog/homepage.html',{'total_count':Purchased_goods.changed_count()})
def shop_list(request):
    if request.method=='POST':
        goods_id= request.POST['id']
        choosed_gift_goods=Purchased_goods.objects.filter(id=goods_id)
        if choosed_gift_goods:
            choosed_gift_goods[0].count +=1
            choosed_gift_goods[0].save()
        else:
            choosed_post_goods = Shopping_list.objects.filter(id=goods_id)
            Purchased_goods.objects.create(id=goods_id,unit=choosed_post_goods[0].unit,price=choosed_post_goods[0].price,
                                           name=choosed_post_goods[0].name,count=choosed_post_goods[0].count,
                                           classname=choosed_post_goods[0].classname)
        return HttpResponse(Purchased_goods.changed_count())
    shopping_list = Shopping_list.objects.all()
    return render(request,'blog/shop_list.html',{'shopping_list':shopping_list,'total_count':Purchased_goods.changed_count()})
def pay_list(request):
    if request.method=='POST':
        good_id=request.POST['id']
        goods_number=int(request.POST['co'])
        selected_goods=Purchased_goods.objects.filter(id=good_id)
        if selected_goods:
            selected_goods[0].count+=goods_number
            selected_goods[0].save()
            selected_goods[0].original_price=selected_goods[0].count*selected_goods[0].price
        if selected_goods[0].count==0:
            selected_goods[0].delete()
        else:
            selected_goods[0].save()
        return JsonResponse({'total_count':Purchased_goods.changed_count(),'number':selected_goods[0].count,'original_price':selected_goods[0].original_price})
        print("4444")
    purchased_goods_list = Purchased_goods.objects.all()
    return render(request,'blog/pay_list.html',{'total_count':Purchased_goods.changed_count(),'purchased':purchased_goods_list})