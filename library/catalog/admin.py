from django.contrib import admin

from catalog.models import *

admin.site.register(Reader)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(HistoryBook)