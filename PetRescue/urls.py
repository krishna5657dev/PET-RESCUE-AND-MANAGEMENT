"""PetRescue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PetRescueApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('login/',views.signin),
    path('Customer_register/',views.signup),
    path('save_user/', views.action_save_user),
    path('Adoption_center_register/', views.Adoption_center_register),
    path('login_action/', views.sign_in_process),
    path('save_agency/', views.save_agency),
    path('check_username/', views.check_username, name='check_username'),
    # admin
    path('admin_home/', views.admin_home),
    #User
    path('User_home/', views.User_home),
    #User
    path('Adoption_center_home/', views.Adoption_center_home),
    #logout
    path('admin_logout/', views.admin_logout),
    #country
    path('country/', views.country_frm),
    path('add_country/', views.add_country),
    path('edit_country/<int:id>', views.edit_country),
    path('update_country/<int:id>', views.update_country),
    path('delete_country/<int:id>', views.delete_country),
     #state
    path('state/', views.state_frm),
    path('add_state/', views.add_state),
    path('edit_state/<int:id>', views.edit_state_frm),
    path('update_state/<int:id>', views.update_state),
    path('delete_state/<int:id>', views.delete_state),
     #district
    path('district/', views.district_frm),
    path('display_state/', views.display_state, name='display_state'),
    path('add_district/', views.save_district),
    path('edit_district/<int:id>', views.edit_district_frm),
    path('update_district/<int:id>', views.update_district),
    path('delete_district/<int:id>', views.delete_district),
    #place
    path('place/', views.place_frm),
    path('display_district/', views.display_district, name='display_district'),
    path('add_place/', views.save_place),
    path('display_place/', views.display_place, name='display_place'),
    path('delete_place/<int:id>', views.delete_place),
    path('edit_place/<int:id>', views.edit_place_frm),
    path('update_place/<int:id>', views.update_place),

#Admin - Approve AC
 path('approve_ac/', views.approve_ac),
 path('approve_agency/<int:id>', views.approve_agency),
 path('reject_agency/<int:id>', views.reject_agency),
 path('ac_list/', views.ac_list),

#admin
path('boarding_admin/', views.boarding_admin),
path('grooming_admin/', views.grooming_admin),



 #Profile

#Pets
path('Pets/', views.pets_frm),
path('save_pets/', views.save_pets),
path('Pets_List/', views.Pets_List),
path('edit_pets/<int:id>', views.edit_pets),
path('update_pets/<int:id>', views.update_pets),
path('delete_pets/<int:id>', views.delete_pets),

 #feedback
path('Feedback/', views.Feedback_frm),
path('display_ad/', views.display_ad, name='display_ad'),
path('save_feedback/', views.save_feedback),
path('Feedback_list/', views.Feedback_list),
path('delete_feedback/<int:id>', views.delete_feedback),
#Complaint
path('Complaint/', views.Complaint_frm),
path('save_complaint/', views.save_complaint),
path('Complaint_list/', views.Complaint_list),
path('delete_complaint/<int:id>', views.delete_complaint),

# //Profile
path('Profile/', views.profile),
path('edit_profile/', views.edit_profile),
path('update_user/', views.update_user),
path('change_password/', views.change_password),
path('update_password/', views.update_password),

# rescue Info
path('Rescue_Info/', views.Rescue_Info),
path('save_rescue_info/', views.save_rescue_info),
path('Rescue_Info_Reply/', views.Rescue_Info_Reply),
path('delete_rescue/<int:id>', views.delete_rescue),

# Adoption Center
path('ad_Rescue_Info/', views.ad_Rescue_Info),
path('adopt_from_street/<int:id>', views.adopt_from_street),
path('ad_adopted_list', views.ad_adopted_list),
path('reply_rescue/<int:id>', views.reply_rescue),
path('save_reply/<int:id>', views.save_reply),
path('ad_Rescue_Info_Reply', views.ad_Rescue_Info_Reply),
path('add_user_adoption/<int:id>', views.add_user_adoption),
path('save_send_to_adopton/<int:id>', views.save_send_to_adopton),
path('ad_Adoption', views.ad_Adoption),
path('view_rescue_details/<int:id>', views.view_rescue_details),

# User - aoption
path('Adoption/', views.Adoption),
path('book_adoption/<int:id>', views.book_adoption),
path('Booked_list/', views.Booked_list),
path('adoption_request/', views.adoption_request),
path('adopt_user_pet/<int:id>', views.adopt_user_pet),
path('adopted_list/', views.adopted_list),

#user ad_Feedback
path('ad_Feedback/', views.ad_Feedback),
path('reply_feedback/<int:id>', views.reply_feedback),
path('save_reply_feedback/<int:id>', views.save_reply_feedback),
path('ad_replied_feedback/', views.ad_replied_feedback),

#profile
path('ad_Profile/', views.ad_Profile),
path('ad_edit_profile/', views.ad_edit_profile),
path('save_profile_agency/<int:id>', views.save_profile_agency),
path('ad_change_password/', views.ad_change_password),
path('ad_update_password/', views.ad_update_password),
path('User_Logout/', views.User_Logout),
#admin - Complaint
path('view_complaints/', views.view_complaints),
path('replied_list/', views.replied_list),
path('adm_reply_complaint/<int:id>', views.adm_reply_complaint),
path('add_reply/<int:id>', views.add_reply),
# admin stray_dogs

path('stray_dogs/', views.stray_dogs),
path('adoption/', views.adoption),
path('users/', views.users),
path('feedback_adm/', views.feedback_adm),
#ad_Boarding
path('ad_Boarding/', views.ad_Boarding),
path('save_boarding_services/', views.save_boarding_services),
path('edit_boarding_services/<int:id>', views.edit_boarding_services),
path('update_boarding_services/<int:id>', views.update_boarding_services),
path('delete_boarding_services/<int:id>', views.delete_boarding_services),
path('boarding_booking_list/', views.boarding_booking_list),
path('booking_approvel/<int:id>', views.booking_approvel),
path('booking_reject/<int:id>', views.booking_reject),
path('boarding_booking_accepted_list/', views.boarding_booking_accepted_list),


#ad_Grooming
path('ad_Grooming/', views.ad_Grooming),
path('save_grooming_services/', views.save_grooming_services),
path('edit_grooming_services/<int:id>', views.edit_grooming_services),
path('update_grooming_services/<int:id>', views.update_grooming_services),
path('delete_grooming_services/<int:id>', views.delete_grooming_services),
path('grooming_booking_list/', views.grooming_booking_list),
path('Grooming_booking_accepted_list/', views.Grooming_booking_accepted_list),
path('booking_grooming_approvel/<int:id>', views.booking_grooming_approvel),
path('booking_grooming_reject/<int:id>', views.booking_grooming_reject),


#Boarding
path('Boarding/', views.Boarding),
path('display_boarding/', views.display_boarding, name='display_boarding'),
path('book_boarding_services/<int:id>', views.book_boarding_services),
path('save_boarding_booking/<int:id>', views.save_boarding_booking),
path('Boarding_status/', views.Boarding_status, name='Boarding_status'),

# Grooming Using
path('Grooming/', views.Grooming),
path('display_grooming/', views.display_grooming, name='display_grooming'),
path('book_grooming_services/<int:id>', views.book_grooming_services),
path('save_grooming_booking/<int:id>', views.save_grooming_booking),
path('Grooming_status/', views.Grooming_status),


]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)