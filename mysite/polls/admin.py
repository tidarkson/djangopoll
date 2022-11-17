from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = "Tee's Poll App"
admin.site.site_title = "Poll App Admin"
admin.site.index_title = "Welcome To Tee's Poll App"


admin.site.register(Question)
admin.site.register(Choice)

