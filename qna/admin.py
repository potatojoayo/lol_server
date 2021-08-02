from django.contrib import admin
from .models import QnaStatus,QnaCategory,Qna,QnaComment


admin.site.register(QnaStatus)
admin.site.register(QnaComment)
admin.site.register(Qna)
admin.site.register(QnaCategory)
