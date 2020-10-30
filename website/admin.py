from django.contrib import admin
from website.models import Categories, Apps, Blog_Post, comment_put, author
# Register your models here.

admin.site.register(Categories)
admin.site.register(Apps)
admin.site.register(Blog_Post)
admin.site.register(comment_put)
admin.site.register(author)
