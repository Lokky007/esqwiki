from django.contrib import admin
from .models import CategoryBlock, Category, AccessRight, Answer, Topic

# Register your models here.


admin.site.register(CategoryBlock)
admin.site.register(Category)
admin.site.register(AccessRight)
admin.site.register(Answer)
admin.site.register(Topic)
