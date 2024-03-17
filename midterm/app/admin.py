from django.contrib import admin
from .models import User, Company, Skill, Vacancy, Resume, Response

admin.site.register(User)
admin.site.register(Company)
admin.site.register(Skill)
admin.site.register(Vacancy)
admin.site.register(Resume)
admin.site.register(Response)