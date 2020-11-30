from django.contrib import admin
from django.contrib.auth.models import User

#Model
from posts.models import Post

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    """PostsAdmin. """
    list_display = ('pk', 'user','title','photo',)
    list_display_links = ('pk','user',)
    list_editable = ('title','photo',)
    readonly_fields = ('crated','modified')
    # fieldsets = (
    #     ('Metada',{
    #         'fields':('created','modified')
    #     }),
    # )