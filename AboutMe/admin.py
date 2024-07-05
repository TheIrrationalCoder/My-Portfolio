from django.contrib import admin
from .models import Person, Skill, Experience, Education, Certification, Visitor
# Register your models here.
pkg_list = [Person, Skill, Experience, Education, Certification,Visitor]

[admin.site.register(pkg) for pkg in pkg_list]
