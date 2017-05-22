
from django.contrib import admin
from .models import Shopping_list
from .models import Purchased_goods
from .models import GiftGoods

admin.site.register(Shopping_list)
admin.site.register(Purchased_goods)
admin.site.register(GiftGoods)