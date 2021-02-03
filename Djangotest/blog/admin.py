from django.contrib import admin
from.models import Post,postImages,PostTemplates
# Register your models here.

admin.site.register(Post)
admin.site.register(postImages)
admin.site.register(PostTemplates)