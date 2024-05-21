from django.contrib import admin
from .models import Tag, Question, Answer, Vote, Comment


admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Vote)
admin.site.register(Comment)
