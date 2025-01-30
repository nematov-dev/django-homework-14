from django.contrib import admin


from .models import (
    ProductCategoryModel, 
    ProductTagModel, 
    ProductSizeModel, 
    ProductManufactureModel, 
    ProductColorModel, 
    ProductModel, 
    ProductCommentModel, 
    ProductImageModel
)

@admin.register(ProductCategoryModel)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent')
    search_fields = ('title',)
    list_filter = ('parent',)

@admin.register(ProductTagModel)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)

@admin.register(ProductSizeModel)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)

@admin.register(ProductManufactureModel)
class ProductManufactureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo')
    search_fields = ('name',)

@admin.register(ProductColorModel)
class ProductColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'code')
    search_fields = ('title', 'code')

class ProductImageAdmin(admin.StackedInline):
    model = ProductImageModel
   
    
@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sku', 'price', 'in_stock', 'quantity', 'discount', 'discount_price', 'brands')
    search_fields = ('title', 'sku')
    list_filter = ('in_stock', 'categories', 'brands')
    filter_horizontal = ('colors', 'sizes', 'tags', 'categories')
    inlines = [ProductImageAdmin]
    readonly_fields = ['discount_price']

@admin.register(ProductCommentModel)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'comment')
    search_fields = ('comment', 'user__username', 'product__title')

