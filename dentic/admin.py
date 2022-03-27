from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from dentic import models
from django import forms


# Register your models here.


class ProcedureAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = models.Procedure
        fields = "__all__"


class ProcedureInline(admin.StackedInline):
    model = models.Procedure
    form = ProcedureAdminForm
    extra = 0


@admin.register(models.BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ["full_name", "phone",
                    "create_time", "update_time"]
    list_filter = ["create_time", "update_time"]
    inlines = [ProcedureInline, ]


@admin.register(models.Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ["user", "create_time", "update_time"]
    list_filter = ["user", "create_time", "update_time"]
    form = ProcedureAdminForm

admin.site.register(models.Diagnosis)
admin.site.register(models.Treatment)
admin.site.register(models.DentalFilling)