from django.contrib import admin


from . import models
admin.site.register(models.place)

admin.site.register(models.self)


admin.site.register(models.myuser)