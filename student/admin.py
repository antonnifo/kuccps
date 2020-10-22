import csv
import datetime

from django.contrib import admin
from django.http import HttpResponse

from .models import Student, Programme, Institution, ProgrammeChoice, Enrollment

def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;'\
        'filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many
              and not field.one_to_many]

    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response


export_to_csv.short_description = 'Export to CSV'


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):

    list_display = ['id','name','key','typ','city','category']
    list_filter = ['typ', 'category', 'city']
    list_editable = ['typ','category']
    list_per_page = 10



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = ['id','user','index','school','location','points']
    list_filter = ['school', 'location']
    # list_editable = ['index','location']
    list_per_page = 10
    
@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):

    list_display = ['id','name','category']
    list_filter = ['category',]
    list_editable = ['category',]
    list_per_page = 10

@admin.register(ProgrammeChoice)
class ProgrammeChoiceAdmin(admin.ModelAdmin):

    list_display = ['id','programme','institution', 'cutoff_points']
    list_filter = ['programme', 'institution']
    # list_editable = ['category',]
    list_per_page = 10

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):

    # list_display = ['id','programme','date_enrolled']
    # list_filter = ['programme',]

    # list_editable = ['category',]
    list_per_page = 10
    fields = ('programme', 'institution')
    def save_model(self, request, obj, form, change):
        if not change:
            obj.Student = request.user
        obj.save()

        
admin.site.site_header = "KUCCPS" 
