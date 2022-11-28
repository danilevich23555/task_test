from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from demo.models import Item, Order, OrderPosition

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'price']



class PositionInlineFormset(BaseInlineFormSet):
    def clean(self):
        real_forms = [f for f in self.forms if not f.cleaned_data['DELETE']]
        products_id = set([form.cleaned_data['item'].id for form in self.forms])
        if len(products_id) != len(real_forms):
            raise ValidationError('В заказе есть повторяющиеся продукты, уберите один и измените количество!')
        # for form in self.forms:
        #
        #     form.cleaned_data['item']
        #     form.cleaned_data['qty']
        #     form.cleaned_data['DELETE']
        #     raise ValidationError('В заказе есть повторяющиеся продукты, уберите один и измените количество!')
        return super().clean()  # вызываем базовый код переопределяемого метода



class PositionsInline(admin.TabularInline):
    model = OrderPosition
    formset = PositionInlineFormset
    extra = 0




@admin.register(Order)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = [PositionsInline]

