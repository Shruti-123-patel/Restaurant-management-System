from django.contrib import admin
from basic.models import mannualOrder, orderood, table, tableReservation
from basic.models import dealsAndOffers
from basic.models import orders
from basic.models import feedback
from basic.models import worker
from basic.models import customer
from basic.models import foodItems

admin.site.register(foodItems)
admin.site.register(customer)
admin.site.register(worker)
admin.site.register(feedback)
admin.site.register(orders)
admin.site.register(dealsAndOffers)
admin.site.register(mannualOrder)
admin.site.register(orderood)
admin.site.register(table)
admin.site.register(tableReservation)