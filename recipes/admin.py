from django.contrib import admin

from .models import Recipe, Ingredient, RecipeIngredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    list_display = ('title', 'created_at')

    search_fields = ('title', 'description')

    list_filter = ('created_at',)

    fields = ('title', 'description', 'instructions')

    inlines = [RecipeIngredientInline]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):

    list_display = ('name',)

    search_fields = ('name',)


    