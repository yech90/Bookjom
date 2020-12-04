from django.contrib import admin
from .models import *
from tof.admin import TofAdmin, TranslationTabularInline
from tof.decorators import tof_prefetch

@admin.register(Portfolio)
class PortfolioAdmin(TofAdmin):
    list_display = ('title', 'label','main_detail','second_detail')
    search_fields = ('title', 'label','main_detail','second_detail')
    inlines = (TranslationTabularInline,)