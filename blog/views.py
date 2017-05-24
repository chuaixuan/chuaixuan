from django.shortcuts import render
from .models import Shopping_list
from .models import Purchased_goods
from .models import GiftGoods
from django.http import HttpResponse
from django.http import JsonResponse
import math
import datetime
def homepage(request):

    return render(request, 'blog/homepage.html',{'total_count':Purchased_goods.changed_count()})
def shop_list(request):
    if request.method=='POST':
        goods_id= request.POST['id']
        choosed_gift_goods=Purchased_goods.objects.filter(id=goods_id)
        if choosed_gift_goods:
            choosed_gift_goods[0].count +=1
            choosed_gift_goods[0].original_price=choosed_gift_goods[0].count*choosed_gift_goods[0].price
            choosed_gift_goods[0].sumtotal = (choosed_gift_goods[0].count - choosed_gift_goods[0].gift_count) * choosed_gift_goods[0].price
            choosed_gift_goods[0].gift_price = choosed_gift_goods[0].gift_count * choosed_gift_goods[0].price
            choosed_gift_goods[0].save()
        else:
            choosed_post_goods = Shopping_list.objects.filter(id=goods_id)
            Purchased_goods.objects.create(id=goods_id,unit=choosed_post_goods[0].unit,price=choosed_post_goods[0].price,
                                           name=choosed_post_goods[0].name,count=choosed_post_goods[0].count,
                                           classname=choosed_post_goods[0].classname)
        selected_goods = Purchased_goods.objects.filter(id=goods_id)
        selected_gift_goods = GiftGoods.objects.filter(id=goods_id)
        if selected_goods:
            if selected_gift_goods:
                selected_goods[0].gift_count = math.floor(selected_goods[0].count / 3)
                selected_goods[0].sumtotal = (selected_goods[0].count - selected_goods[0].gift_count) * float(
                    selected_goods[0].price)
                selected_goods[0].save()
            selected_goods[0].original_price = selected_goods[0].count * float(selected_goods[0].price)
            selected_goods[0].save()
        return HttpResponse(Purchased_goods.changed_count())
    shopping_list = Shopping_list.objects.all()
    return render(request,'blog/shop_list.html',{'shopping_list':shopping_list,'total_count':Purchased_goods.changed_count()})
def pay_list(request):
    if request.method=='POST':
        goods_id=request.POST['id']
        goods_number=int(request.POST['count'])
        selected_goods=Purchased_goods.objects.filter(id=goods_id)
        selected_gift_goods=GiftGoods.objects.filter(id=goods_id)
        if selected_goods:
            selected_goods[0].count += goods_number
            if selected_gift_goods:
                selected_goods[0].gift_count=math.floor(selected_goods[0].count/3)
                selected_goods[0].sumtotal = (selected_goods[0].count - selected_goods[0].gift_count) * selected_goods[0].price
                selected_goods[0].save()
            selected_goods[0].original_price = selected_goods[0].count * selected_goods[0].price
            selected_goods[0].gift_price=selected_goods[0].gift_count*selected_goods[0].price
            selected_goods[0].save()
        if selected_goods[0].count==0:
            selected_goods[0].delete()
        else:
            selected_goods[0].save()
        return JsonResponse({'total_count':Purchased_goods.changed_count(),'number':selected_goods[0].count,'original_price':selected_goods[0].original_price,
                             'sumtotal':selected_goods[0].sumtotal,'total_price':Purchased_goods.total_price(),'gift_count':selected_goods[0].gift_count})
        print(selected_goods[0].gift_count)
    purchased_goods_list = Purchased_goods.objects.all()
    return render(request,'blog/pay_list.html',{'total_count':Purchased_goods.changed_count(),'purchased':purchased_goods_list,'total_price':Purchased_goods.total_price()})
def payment_page(request):
    now = datetime.datetime.now()
    otherStyleTime = now.strftime("%Y年%m月%d日 %H:%M:%S")
    if request.method == ('POST'):
        purchased_goods_list = Purchased_goods.objects.all()
        purchased_goods_list.delete()
        return HttpResponse()
    purchased_goods_list = Purchased_goods.objects.all()
    return render(request,'blog/payment_page.html',{'purchased':purchased_goods_list,'total_count':Purchased_goods.changed_count(),'total_price':Purchased_goods.total_price(),
                                                    'total_gift_price':Purchased_goods.total_gift_price(),'otherStyleTime':otherStyleTime})