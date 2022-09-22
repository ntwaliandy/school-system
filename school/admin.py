from django.contrib import admin
from .models import Attendance,StudentExtra,TeacherExtra,Notice,Notes,Grading,Help,Test,Question,Answer
# Register your models here. (by sumit.luv)
class StudentExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentExtra, StudentExtraAdmin)

class TeacherExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(TeacherExtra, TeacherExtraAdmin)

class AttendanceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Attendance, AttendanceAdmin)

class NoticeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Notice, NoticeAdmin)

class NotesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Notes, NotesAdmin)

class GradingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Grading, GradingAdmin)

class HelpAdmin(admin.ModelAdmin):
    pass
admin.site.register(Help, HelpAdmin)

class TestAdmin(admin.ModelAdmin):
    pass
admin.site.register(Test, TestAdmin)

class QuestionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Answer, AnswerAdmin)