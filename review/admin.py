from django.contrib import admin
from .models import Review, ReviewComment, Photo

admin.site.register(Review)
admin.site.register(ReviewComment)
admin.site.register(Photo)

