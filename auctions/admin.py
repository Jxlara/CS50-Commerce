from django.contrib import admin

from auctions.models import *
from django.contrib import admin

# Register your models here.
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Watchlist)
admin.site.register(Comment)
admin.site.register(Winner)