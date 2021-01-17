from django.contrib import admin
from .models import User, Company, JobHunter
# Register your models here.

admin.site.register(User)
admin.site.register(JobHunter)
admin.site.register(Company)
