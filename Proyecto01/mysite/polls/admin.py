from django.contrib import admin
from .models import Question, Choice

classes = ["collapse", "wide", "extrapretty"]

class ChoiceInline(admin.StackedInline):
    model = Choice
    # Provide fields for 3 choices
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        # (name, field_options)
        (None, {
            "fields": ["question_text"]
            }),
        ("Date information", {
            "fields": ["pub_date"], 
            "classes": classes
            }),
    ]
    # Objects of the model "Choice" are edited on the Question admin page
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

# Esto no se utiliza porque se ponen los objetos de Choice dentro de Question con el INLINE

# class ChoiceAdmin(admin.ModelAdmin):
#     fieldsets = [
#         # Foreign Keys are in a Select box always
#         (None, {"fields": ["question"]}),
#         (None, {"classes": ["collapse"],"fields": ["choice_text"]}),
#         (None, {"fields": ["votes"]}),
#     ]

# admin.site.register(Choice, ChoiceAdmin)

