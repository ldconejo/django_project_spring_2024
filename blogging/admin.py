from django.contrib import admin

from blogging.models import Post, Category

# admin.site.register(Post)
# admin.site.register(Category)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
