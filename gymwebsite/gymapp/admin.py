from django.contrib import admin

from .models import  Member,Membershiptype,No_of_people,Contact

class Membershiptypeadmin(admin.ModelAdmin):
    list_display = ('type','image','plan_validity','price')
admin.site.register(Membershiptype,Membershiptypeadmin)



class Memberadmin(admin.ModelAdmin):
    list_display = ('user','name','email','phone','dob','address','membershipname','timeslot','validity','price','join_date','expire_date')
admin.site.register(Member,Memberadmin)



class No_of_people_admin(admin.ModelAdmin):
    list_display = ('user','membershiptype','time','noofpeople')
admin.site.register(No_of_people,No_of_people_admin)

class Contactadmin(admin.ModelAdmin):
    list_display = ('user','name','phone','message')
admin.site.register(Contact,Contactadmin)