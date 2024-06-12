from django.contrib import admin
from .models import Question, Choice

classes = ["collapse", "wide", "extrapretty"]

class ChoiceInline(admin.TabularInline):
    model = Choice
    # Provide fields for # extra choices
    extra = 1


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
    # Which field are displayed con the change lsita page of admin, if not specified it will display a single columns with __str__()
    list_display = ["question_text", "pub_date", "was_published_recently"]
    # Add a Filter sidebar
    list_filter = ["pub_date"]
    # Search Box at the top of the list
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)