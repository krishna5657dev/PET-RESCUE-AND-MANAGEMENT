# admin.py

from django.contrib import admin
from .models import (
    login, user_register, adoption_center_register, country, state,
    district, place, pets, feedback, complaint, Rescue_info,
    adoption_info, boarding_service, grooming_service,
    booking_boarding, booking_grooming
)

# Register your models here.
@admin.register(login)
class LoginAdmin(admin.ModelAdmin):
    list_display = ('login_id', 'username', 'Usertype', 'status')
    search_fields = ('username', 'Usertype')

@admin.register(user_register)
class UserRegisterAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'login_id', 'firstname', 'lastname', 'mail_id')
    search_fields = ('firstname', 'lastname', 'mail_id')
    list_filter = ('firstname', 'lastname')

@admin.register(adoption_center_register)
class AdoptionCenterRegisterAdmin(admin.ModelAdmin):
    list_display = ('aid_id', 'login_id', 'agency_name', 'mail_id')
    search_fields = ('agency_name', 'mail_id')
    list_filter = ('agency_name',)

@admin.register(country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_id', 'country')
    search_fields = ('country',)

@admin.register(state)
class StateAdmin(admin.ModelAdmin):
    list_display = ('state_id', 'country_id', 'state')
    search_fields = ('state',)
    list_filter = ('country_id',)

@admin.register(district)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('district_id', 'state_id', 'district')
    search_fields = ('district',)
    list_filter = ('state_id',)

@admin.register(place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('place_id', 'district_id', 'place')
    search_fields = ('place',)
    list_filter = ('district_id',)

@admin.register(pets)
class PetsAdmin(admin.ModelAdmin):
    list_display = ('pname', 'breed', 'type', 'gender', 'age', 'user_login_id')
    search_fields = ('pname', 'breed', 'type', 'gender')
    list_filter = ('breed', 'type', 'gender')

@admin.register(feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('feedback_id', 'feedback_subject', 'Ac_login_id', 'user_login_id')
    search_fields = ('feedback_subject', 'Ac_login_id', 'user_login_id')
    list_filter = ('Ac_login_id', 'user_login_id')

@admin.register(complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('complaint_id', 'complaint_subject', 'user_login_id')
    search_fields = ('complaint_subject', 'user_login_id')
    list_filter = ('user_login_id',)

@admin.register(Rescue_info)
class RescueInfoAdmin(admin.ModelAdmin):
    list_display = ('rescue_id', 'subject', 'date', 'Ac_login_id', 'user_login_id', 'status')
    search_fields = ('subject', 'Ac_login_id', 'user_login_id', 'status')
    list_filter = ('status', 'date')

@admin.register(adoption_info)
class AdoptionInfoAdmin(admin.ModelAdmin):
    list_display = ('adoption_id', 'pet_type', 'tag_name', 'breed', 'age', 'gender', 'date', 'status')
    search_fields = ('pet_type', 'tag_name', 'breed', 'gender', 'status')
    list_filter = ('pet_type', 'breed', 'gender', 'status', 'date')

@admin.register(boarding_service)
class BoardingServiceAdmin(admin.ModelAdmin):
    list_display = ('b_service_id', 'pet_type', 'cost', 'Ac_login_id')
    search_fields = ('pet_type', 'Ac_login_id')
    list_filter = ('pet_type',)

@admin.register(grooming_service)
class GroomingServiceAdmin(admin.ModelAdmin):
    list_display = ('g_service_id', 'service_name', 'pet_type', 'cost', 'Ac_login_id')
    search_fields = ('service_name', 'pet_type', 'Ac_login_id')
    list_filter = ('service_name', 'pet_type')

@admin.register(booking_boarding)
class BookingBoardingAdmin(admin.ModelAdmin):
    list_display = ('boarding_booking_id', 'starting_date', 'ending_date', 'pet_id', 'b_service_id', 'user_login_id', 'status')
    search_fields = ('starting_date', 'ending_date', 'pet_id', 'user_login_id', 'status')
    list_filter = ('status', 'starting_date', 'ending_date')

@admin.register(booking_grooming)
class BookingGroomingAdmin(admin.ModelAdmin):
    list_display = ('grroming_booking_id', 'date', 'pet_id', 'g_service_id', 'user_login_id', 'status')
    search_fields = ('date', 'pet_id', 'user_login_id', 'status')
    list_filter = ('status', 'date')
