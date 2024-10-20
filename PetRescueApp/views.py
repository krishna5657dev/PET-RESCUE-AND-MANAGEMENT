from django.shortcuts import render,redirect,HttpResponse
from PetRescueApp.models import login, user_register, adoption_center_register,country,state,district,place,pets,feedback,complaint,Rescue_info,adoption_info,boarding_service,grooming_service,booking_boarding,booking_grooming
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import logout
from django.db import connection
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,'index.html')
def signin(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'register.html')
def action_save_user(request):
    tbl1=login()
    username=request.POST.get("username")
    tbl1.username=request.POST.get("username")
    password=request.POST.get("password")
    tbl1.password=password
    tbl1.Usertype="User"
    tbl1.status="Approved"
    tbl1.save()
    obj=login.objects.get(username=username,password=password)

    u=user_register()
    u.login_id = obj.login_id
    u.firstname=request.POST.get("firstname")
    u.lastname=request.POST.get("lastname")
    u.phone_number =request.POST.get("phone")
    u.address=request.POST.get("address")
    u.mail_id=request.POST.get("mail_id")
    u.save()
    messages.add_message(request, messages.INFO, 'Registered successfully.')
    return redirect('/Customer_register')
def save_agency(request):
    tbl1=login()
    username=request.POST.get("username")
    tbl1.username=request.POST.get("username")
    password=request.POST.get("password")
    tbl1.password=password
    tbl1.Usertype="Adoption Center"
    tbl1.status="Not Approved"
    tbl1.save()
    obj=login.objects.get(username=username,password=password)


    u=adoption_center_register()
    u.login_id = obj.login_id
    u.agency_name=request.POST.get("aname")
    u.phone_number =request.POST.get("phone")
    u.address=request.POST.get("address")
    u.mail_id=request.POST.get("mail_id")
    u.place_id=request.POST.get("place")
    u.save()
    messages.add_message(request, messages.INFO, 'Registered successfully.')
    return redirect('/Adoption_center_register')
def check_username(request):
    username = request.GET.get("username")
    data = {
       'username_exists':      login.objects.filter(username=username).exists(),
        'error':"Username Already Exist"
    }
    if(data["username_exists"]==False):
        data["success"]="Available"

    return JsonResponse(data)

def sign_in_process(request):
    u=request.POST.get("username")
    p=request.POST.get("password")
    obj=authenticate(username=u,password=p)
    if obj is not None:
        if obj.is_superuser == 1:
            request.session['suname'] = u
            request.session['slogid'] = obj.id
            return redirect('/admin_home')
        else:
          messages.add_message(request, messages.INFO, 'Invalid User.')
          return redirect('/login')
    else:
        newp=p
        try:
            obj1=login.objects.get(username=u,password=newp)
            if(obj1.Usertype=="User"):
                 request.session['suname'] = u
                 request.session['slogid'] = obj1.login_id
                 return redirect('/User_home')
            elif obj1.Usertype=="Adoption Center":
                if(obj1.status=="Approved"):
                    request.session['suname'] = u
                    request.session['slogid'] = obj1.login_id
                    return redirect('/Adoption_center_home')
                elif(obj1.status=="Not Approved"):
                  messages.add_message(request, messages.INFO, 'Waiting For Approval.')
                  return redirect('/login')
                else:
                  messages.add_message(request, messages.INFO, 'Invalid User.')
                  return redirect('/login')

            else:
                 messages.add_message(request, messages.INFO, 'Invalid User.')
                 return redirect('/login')
        except login.DoesNotExist:
         messages.add_message(request, messages.INFO, 'Invalid User.')
         return redirect('/login')

def Adoption_center_register(request):
    data1 = country.objects.all()
    return render(request,'adoption_center_register.html',{'data1':data1})
# Admin
def admin_home(request):
    if 'suname' in request.session:
     return render(request,'User1/index.html')
    else:
      return redirect('/login')
#User
def User_home(request):
 if 'suname' in request.session:
    return render(request,'User2/index.html')
 else:
      return redirect('/login')

#Adoption Center
def Adoption_center_home(request):
 if 'suname' in request.session:
     id= request.session['slogid']
     obj1=adoption_center_register.objects.get(login_id=id)

     return render(request,'User3/index.html',{'udata':obj1})
 else:
      return redirect('/login')
#logout

def admin_logout(request):
    logout(request)
    return redirect('/login')
#Location
def country_frm(request):
    if 'suname' in request.session:
     data=country.objects.all()
     return render(request,'User1/country.html',{'data':data})
    else:
      return redirect('/login')
def add_country(request):
    if 'suname' in request.session:
        tbl=country()
        tbl.country=request.POST.get("country")
        tbl.save()
        messages.add_message(request, messages.INFO, 'Registered successfully.')
        return redirect('/country')
    else:
       return redirect('/login')
def edit_country(request,id):
    if 'suname' in request.session:
        data=country.objects.get(country_id=id)
        return render(request,'User1/edit_country_details.html',{'data':data})
    else:
       return redirect('/login')
def update_country(request,id):
    if 'suname' in request.session:
        tbl=country.objects.get(country_id=id)
        tbl.country=request.POST.get("country")
        tbl.save()
        messages.add_message(request, messages.INFO, 'Updated successfully.')
        return redirect('/country')
    else:
       return redirect('/login')
def delete_country(request,id):
    if 'suname' in request.session:
        tbl=country.objects.get(country_id=id)
        tbl.delete()
        messages.add_message(request, messages.INFO, 'Deleted successfully.')
        return redirect('/country')
    else:
       return redirect('/login')
def state_frm(request):
    if 'suname' in request.session:
        data1 = country.objects.all()
        cursor=connection.cursor()
        cursor.execute("select tbl_country.country,tbl_state.state,tbl_state.state_id from tbl_country inner join tbl_state on tbl_country.country_id=tbl_state.country_id_id")
        data=cursor.fetchall()
        return render(request,'User1/state.html',{'data':data,'data1':data1})
    else:
       return redirect('/login')
def add_state(request):
    if 'suname' in request.session:
        a=request.POST.get("country")
        b=request.POST.get("state")
        obj = state(state=b, country_id_id=a)
        obj.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/state')
    else:
       return redirect('/login')
def edit_state_frm(request,id):
    if 'suname' in request.session:
        data1 = country.objects.all()
        data=state.objects.filter(state_id=id).select_related("country_id")
        return render(request,'User1/edit_state_details.html',{'data':data,'data1':data1})
    else:
       return redirect('/login')
def update_state(request,id):
    if 'suname' in request.session:

        c=request.POST.get("country")
        s=request.POST.get("state")

        state.objects.filter(state_id=id).update(country_id=c,state=s)
        messages.add_message(request, messages.INFO, 'Updated successfully.')
        return redirect('/state')
    else:
       return redirect('/login')
def delete_state(request,id):
    if 'suname' in request.session:
        tbl=state.objects.get(state_id=id)
        tbl.delete()
        messages.add_message(request, messages.INFO, 'Deleted successfully.')
        return redirect('/state')
    else:
       return redirect('/login')
def district_frm(request):
    if 'suname' in request.session:
        data1 = country.objects.all()
        cursor=connection.cursor()
        cursor.execute("select tbl_country.country,tbl_state.state,tbl_district.* from tbl_district inner join tbl_state on tbl_district.state_id_id=tbl_state.state_id inner join tbl_country on tbl_state.country_id_id=tbl_country.country_id")
        data=cursor.fetchall()
        return render(request,'User1/district.html',{'data':data,'data1':data1})
    else:
       return redirect('/login')
def delete_district(request,id):
    if 'suname' in request.session:
        tbl=district.objects.get(district_id=id)
        tbl.delete()
        messages.add_message(request, messages.INFO, 'Deleted successfully.')
        return redirect('/district')
    else:
       return redirect('/login')
def display_state(request):

    country_id = request.GET.get("country_id")
    try:
        country_id = country.objects.filter(country_id = country_id).first()
        ste = state.objects.filter(country_id_id = country_id)
    except Exception:
        data=[]
        data['error_message'] = 'error'
        return JsonResponse(data)
    return JsonResponse(list(ste.values('state_id', 'state')), safe = False)
def save_district(request):
    if 'suname' in request.session:
        a=request.POST.get("country")
        b=request.POST.get("state")
        c=request.POST.get("district")
        obj = district(state_id_id=b,district=c)
        obj.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/district')
    else:
       return redirect('/login')
def edit_district_frm(request,id):
     if 'suname' in request.session:
        data1 = country.objects.all()
        data2 = state.objects.all()
        cursor=connection.cursor()
        cursor.execute("select tbl_country.country, tbl_country.country_id,tbl_state.state,tbl_state.state_id,tbl_district.* from tbl_district inner join tbl_state on tbl_district.state_id_id=tbl_state.state_id inner join tbl_country on tbl_state.country_id_id=tbl_country.country_id where district_id="+str(id))
        data=cursor.fetchall()
        return render(request,'User1/edit_district_details.html',{'data':data,'data1':data1,'date2':data2})
     else:
       return redirect('/login')

def update_district(request,id):
    if 'suname' in request.session:
        a=request.POST.get("state")
        c=request.POST.get("district")
        district.objects.filter(district=id).update(state_id=a,district=c)
        messages.add_message(request, messages.INFO, 'Updated successfully.')
        return redirect('/district')
    else:
       return redirect('/login')
def place_frm(request):
    if 'suname' in request.session:
        data1 = country.objects.all()
        cursor=connection.cursor()
        cursor.execute("select tbl_country.country,tbl_state.state,tbl_district.district,tbl_place.* from tbl_place inner join  tbl_district on tbl_place.district_id_id =tbl_district.district_id inner join tbl_state on tbl_district.state_id_id=tbl_state.state_id inner join tbl_country on tbl_state.country_id_id=tbl_country.country_id")
        data=cursor.fetchall()
        return render(request,'User1/place.html',{'data':data,'data1':data1})
    else:
       return redirect('/login')

def display_district(request):
    state_id = request.GET.get("state_id")
    try:
        state_id = state.objects.filter(state_id = state_id).first()
        dist = district.objects.filter(state_id_id = state_id)
    except Exception:
        data=[]
        data['error_message'] = 'error'
        return JsonResponse(data)
    return JsonResponse(list(dist.values('district_id', 'district')), safe = False)
def save_place(request):
     if 'suname' in request.session:
        a=request.POST.get("district")
        b=request.POST.get("place")
        obj = place(district_id_id=a,place=b)
        obj.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/place')
     else:
       return redirect('/login')
def update_place(request,id):
    if 'suname' in request.session:

        c=request.POST.get("district")
        a=request.POST.get("place")
        place.objects.filter(place_id=id).update(district_id_id=c,place=a)
        messages.add_message(request, messages.INFO, 'Updated successfully.')
        return redirect('/place')
    else:
       return redirect('/login')
def edit_place_frm(request,id):
     if 'suname' in request.session:
        data1 = country.objects.all()

        cursor=connection.cursor()
        cursor.execute("select tbl_country.country, tbl_country.country_id,tbl_state.state,tbl_state.state_id,tbl_district.district,tbl_district.district_id, tbl_place.* from tbl_place inner join   tbl_district on tbl_place.district_id_id=tbl_district.district_id inner join tbl_state on tbl_district.state_id_id=tbl_state.state_id inner join tbl_country on tbl_state.country_id_id=tbl_country.country_id where place_id="+str(id))
        data=cursor.fetchall()
        return render(request,'User1/edit_place_details.html',{'data':data,'data1':data1})
     else:
       return redirect('/login')

def display_place(request):
    district_id = request.GET.get("district_id")
    try:
        district_id = district.objects.filter(district_id = district_id).first()
        pl = place.objects.filter(district_id_id = district_id)
    except Exception:
        data=[]
        data['error_message'] = 'error'
        return JsonResponse(data)
    return JsonResponse(list(pl.values('place_id', 'place')), safe = False)
def delete_place(request,id):
    if 'suname' in request.session:
        tbl=place.objects.get(place_id=id)
        tbl.delete()
        messages.add_message(request, messages.INFO, 'Deleted successfully.')
        return redirect('/place')
    else:
       return redirect('/login')
def approve_ac(request):
   if 'suname' in request.session:
        cursor=connection.cursor()
        cursor.execute("select a.*, c.country,s.state,d.district,p.place from  tbl_agency_register as a inner join tbl_place as p on a.place_id=p.place_id inner join  tbl_district as d on p.district_id_id =d.district_id inner join tbl_state as s on d.state_id_id=s.state_id inner join tbl_country  as c on s.country_id_id=c.country_id where a.login_id in (select login_id from tbl_login where Usertype='Adoption Center' and status='Not Approved')")
        data=cursor.fetchall()
        return render(request,'User1/approve_agency.html',{'data':data})
   else:
       return redirect('/login')
def approve_agency(request,id):
    if 'suname' in request.session:
        tbl=login.objects.get(login_id=id)
        tbl.status="Approved"
        tbl.save()
        messages.add_message(request, messages.INFO, 'Updated successfully.')
        return redirect('/approve_ac')
    else:
       return redirect('/login')
def reject_agency(request,id):
    if 'suname' in request.session:
        tbl=login.objects.get(login_id=id)
        tbl.status="Rejected"
        tbl.save()
        messages.add_message(request, messages.INFO, 'Rejected successfully.')
        return redirect('/approve_ac')
    else:
        return redirect('/login')

def ac_list(request):
   if 'suname' in request.session:
            cursor=connection.cursor()
            cursor.execute("select a.*, c.country,s.state,d.district,p.place from  tbl_agency_register as a inner join tbl_place as p on a.place_id=p.place_id inner join  tbl_district as d on p.district_id_id =d.district_id inner join tbl_state as s on d.state_id_id=s.state_id inner join tbl_country  as c on s.country_id_id=c.country_id where a.login_id in (select login_id from tbl_login where Usertype='Adoption Center' and status='Approved')")
            data=cursor.fetchall()
            return render(request,'User1/approved_agency.html',{'data':data})
   else:
        return redirect('/login')
#user
def pets_frm(request):
    if 'suname' in request.session:

        return render(request,'User2/pets.html')
    else:
       return redirect('/login')
def save_pets(request):
     if 'suname' in request.session:
        id=request.session['slogid']
        a=request.POST.get("pname")
        b=request.POST.get("breed")
        c=request.POST.get("gender")
        d=request.POST.get("description")
        e=request.POST.get("age")
        f=request.POST.get("animal_name")
        photo=request.FILES['photo']
        split_tup = os.path.splitext(photo.name)
        file_extension = split_tup[1]
        # folder path
        dir_path = settings.MEDIA_ROOT
        count = 0
        # Iterate directory
        for path in os.listdir(dir_path):
        # check if current path is a file
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
        filecount=count+1
        filename=str(filecount)+"."+file_extension
        obj=FileSystemStorage()
        file=obj.save(filename,photo)
        url1=obj.url(file)
        obj = pets(pname=a,breed=b,gender=c,description=d,age=e,image=url1,user_login_id=id,type=f)
        obj.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/Pets')
     else:
       return redirect('/login')
def Pets_List(request):
    if 'suname' in request.session:
        id=request.session['slogid']
        data1 = pets.objects.filter(user_login_id=id)
        return render(request,'User2/petslist.html',{'data1':data1})
    else:
       return redirect('/login')

def User_Logout(request):
    logout(request)
    request.session.delete()
    return redirect('/login')
def edit_pets(request,id):
    if 'suname' in request.session:
        data=pets.objects.filter(id=id)
        return render(request,'User2/edit_pets.html',{'data':data})
    else:
       return redirect('/login')
def update_pets(request,id):
    if 'suname' in request.session:
        if len(request.FILES) != 0:
            a=request.POST.get("pname")
            b=request.POST.get("breed")
            c=request.POST.get("gender")
            d=request.POST.get("description")
            e=request.POST.get("age")
            f=request.POST.get("animal_name")
            photo=request.FILES['photo']
            split_tup = os.path.splitext(photo.name)
            file_extension = split_tup[1]
            # folder path
            dir_path = settings.MEDIA_ROOT
            count = 0
            # Iterate directory
            for path in os.listdir(dir_path):
            # check if current path is a file
                if os.path.isfile(os.path.join(dir_path, path)):
                    count += 1
            filecount=count+1
            filename=str(filecount)+"."+file_extension
            obj=FileSystemStorage()
            file=obj.save(filename,photo)
            url1=obj.url(file)

            pets.objects.filter(id=id).update(pname=a,breed=b,gender=c,description=d,age=e,image=url1,type=f)
            messages.add_message(request, messages.INFO, 'Updated successfully.')
            return redirect('/Pets_List')
        else:
            a=request.POST.get("pname")
            b=request.POST.get("breed")
            c=request.POST.get("gender")
            d=request.POST.get("description")
            e=request.POST.get("age")
            f=request.POST.get("animal_name")
            pets.objects.filter(id=id).update(pname=a,breed=b,gender=c,description=d,age=e,type=f)
            messages.add_message(request, messages.INFO, 'Updated successfully.')
            return redirect('/Pets_List')
    else:
       return redirect('/login')
def delete_pets(request,id):
    if 'suname' in request.session:
        tbl=pets.objects.get(id=id)
        tbl.delete()
        messages.add_message(request, messages.INFO, 'Deleted successfully.')
        return redirect('/Pets_List')
    else:
       return redirect('/login')
def Feedback_frm(request):
    if 'suname' in request.session:
        data1 = country.objects.all()
        return render(request,'User2/feedback.html',{'data':data1})
    else:
       return redirect('/login')
def display_ad(request):
    place_id = request.GET.get("place_id")
    try:
        logQuerry = login.objects.filter(status='Approved').only('login_id').all()
        ste = adoption_center_register.objects.filter(place_id = place_id,login_id__in=logQuerry)
    except Exception:
        data=[]
        data['error_message'] = 'error'
        return JsonResponse(data)
    return JsonResponse(list(ste.values('login_id', 'agency_name')), safe = False)
def save_feedback(request):
     if 'suname' in request.session:
        id=request.session['slogid']
        a=request.POST.get("subject")
        b=request.POST.get("feedback")
        c=request.POST.get("ad")
        d="No"
        obj = feedback(feedback_subject=a,feedback=b,Ac_login_id=c,reply=d,user_login_id=id)
        obj.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/Feedback')
     else:
       return redirect('/login')
def Feedback_list(request):
    if 'suname' in request.session:
        id=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select f.*,a.agency_name,c.country,s.state,d.district,p.place from tbl_feedback as f inner join  tbl_agency_register  as a on f.Ac_login_id =a.login_id  inner join tbl_place as p on a.place_id=p.place_id inner join  tbl_district as d on p.district_id_id =d.district_id inner join tbl_state as s on d.state_id_id=s.state_id inner join tbl_country  as c on s.country_id_id=c.country_id where f.user_login_id="+str(id))
        data=cursor.fetchall()

        return render(request,'User2/feedbacklist.html',{'data1':data})
    else:
       return redirect('/login')
def delete_feedback(request,id):
    if 'suname' in request.session:
        tbl=feedback.objects.get(feedback_id=id)
        tbl.delete()
        messages.add_message(request, messages.INFO, 'Deleted successfully.')
        return redirect('/Feedback_list')
    else:
       return redirect('/login')
def Complaint_frm(request):
    if 'suname' in request.session:

        return render(request,'User2/complaint.html')
    else:
       return redirect('/login')
def save_complaint(request):
    if 'suname' in request.session:
        tbl=complaint()
        tbl.user_login_id=request.session['slogid']
        tbl.complaint_subject=request.POST.get("subject")
        tbl.complaint=request.POST.get("complaint")
        tbl.reply="No"
        tbl.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/Complaint')
    else:
       return redirect('/login')
def Complaint_list(request):
     if 'suname' in request.session:
        id=request.session['slogid']
        data1 = complaint.objects.filter(user_login_id=id)
        return render(request,'User2/Complaint_list.html',{'data1':data1})
     else:
       return redirect('/login')
def delete_complaint(request,id):
    if 'suname' in request.session:
        tbl=complaint.objects.get(complaint_id=id)
        tbl.delete()
        messages.add_message(request, messages.INFO, 'Deleted successfully.')
        return redirect('/Complaint_list')
    else:
       return redirect('/login')
def profile(request):
     if 'suname' in request.session:
        id=request.session['slogid']
        data1 = user_register.objects.filter(login_id=id)
        return render(request,'User2/profile.html',{'data1':data1})
     else:
       return redirect('/login')
def edit_profile(request):
     if 'suname' in request.session:
        id=request.session['slogid']
        data1 = user_register.objects.filter(login_id=id)
        return render(request,'User2/edit_profile.html',{'data1':data1})
     else:
       return redirect('/login')
def update_user(request):
    id=request.session['slogid']


    u=user_register.objects.get(login_id=id)
    u.firstname=request.POST.get("firstname")
    u.lastname=request.POST.get("lastname")
    u.phone_number =request.POST.get("phone")
    u.address=request.POST.get("address")
    u.mail_id=request.POST.get("mail_id")

    u.save()
    messages.add_message(request, messages.INFO, 'Updated successfully.')
    return redirect('/edit_profile')
def change_password(request):
    if 'suname' in request.session:

        return render(request,'User2/change_password.html')
    else:
       return redirect('/login')
def update_password(request):
    if 'suname' in request.session:
        id=request.session['slogid']
        opass=request.POST.get("opassword")
        npass=request.POST.get("password")
        obj1=login.objects.filter(login_id=id,password=opass)
        if(obj1):
            tbl1=login.objects.get(login_id=id)
            tbl1.password=npass
            tbl1.save()
            messages.add_message(request, messages.INFO, 'Updated Please Login Using new Password.')
            return redirect('/login')
        else:
            messages.add_message(request, messages.INFO, 'Invalid Data')
            return redirect('/change_password')
    else:
       return redirect('/login')
def Rescue_Info(request):
     if 'suname' in request.session:
        data1 = country.objects.all()
        return render(request,'User2/Rescue_info.html',{'data':data1})
     else:
       return redirect('/login')
def save_rescue_info(request):
    if 'suname' in request.session:
        id=request.session['slogid']
        a=request.POST.get("subject")
        b=request.POST.get("description")
        c=request.POST.get("date")
        d=request.POST.get("ad")
        f="Submitted"
        e="Nil"
        photo=request.FILES['photo']
        #set up for file name
        split_tup = os.path.splitext(photo.name)
        file_extension = split_tup[1]
        dir_path = settings.MEDIA_ROOT
        count = 0
        for path in os.listdir(dir_path):

            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
        filecount=count+1
        filename=str(filecount)+"."+file_extension
        #end
        #upload
        obj=FileSystemStorage()
        file=obj.save(filename,photo)
        #end
        url1=obj.url(file)
        obj = Rescue_info(subject=a,description=b,date=c,Ac_login_id=d,photo=url1,user_login_id=id,reply=e,status=f)
        obj.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/Rescue_Info')
    else:
       return redirect('/login')
def Rescue_Info_Reply(request):
     if 'suname' in request.session:
        id=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select r.*,a.agency_name,c.country,s.state,d.district,p.place from tbl_rescue as r inner join  tbl_agency_register  as a on r.Ac_login_id =a.login_id  inner join tbl_place as p on a.place_id=p.place_id inner join  tbl_district as d on p.district_id_id =d.district_id inner join tbl_state as s on d.state_id_id=s.state_id inner join tbl_country  as c on s.country_id_id=c.country_id where r.user_login_id="+str(id))
        data=cursor.fetchall()
        return render(request,'User2/Rescue_Info_Reply.html',{'data':data})
     else:
       return redirect('/login')
def delete_rescue(request,id):
    if 'suname' in request.session:
        tbl=Rescue_info.objects.get(rescue_id=id)
        tbl.delete()
        messages.add_message(request, messages.INFO, 'Deleted successfully.')
        return redirect('/Rescue_Info_Reply')
    else:
       return redirect('/login')

def ad_Rescue_Info(request):
    if 'suname' in request.session:
        id=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select r.*,u.* from tbl_rescue as r inner join  tbl_user_register as u  on r.user_login_id =u.login_id where r.reply='Nil' and r.status='Submitted' and r.Ac_login_id="+str(id))
        data=cursor.fetchall()
        return render(request,'User3/Rescue_info_list.html',{'data':data})
    else:
       return redirect('/login')
def adopt_from_street(request,id):
    if 'suname' in request.session:
        tbl=Rescue_info.objects.get(rescue_id=id)
        tbl.status="Adopted to Shelter"
        tbl.save()
        messages.add_message(request, messages.INFO, 'Adopted to Shelter successfully.')
        return redirect('/ad_adopted_list')
    else:
       return redirect('/login')
def ad_adopted_list(request):
    if 'suname' in request.session:
        id=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select r.*,u.* from tbl_rescue as r inner join  tbl_user_register as u  on r.user_login_id =u.login_id where r.status='Adopted to Shelter' and r.Ac_login_id="+str(id))
        data=cursor.fetchall()
        return render(request,'User3/Rescue_adopted_list.html',{'data':data})
    else:
       return redirect('/login')
def reply_rescue(request,id):
    if 'suname' in request.session:
      data=Rescue_info.objects.get(rescue_id=id)
      return render(request,'User3/Reply_rescue.html',{'data':data})
    else:
     return redirect('/login')

def save_reply(request,id):
    if 'suname' in request.session:
        tbl=Rescue_info.objects.get(rescue_id=id)
        tbl.reply=request.POST.get("reply")
        tbl.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/ad_Rescue_Info_Reply')
    else:
       return redirect('/login')

def ad_Rescue_Info_Reply(request):
    if 'suname' in request.session:
        id=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select r.*,u.* from tbl_rescue as r inner join  tbl_user_register as u  on r.user_login_id =u.login_id where r.reply!='Nil'and status!='for adoption to user' and  r.Ac_login_id="+str(id))
        data=cursor.fetchall()
        return render(request,'User3/Rescue_replied_list.html',{'data':data})

    else:
        return redirect('/login')
def add_user_adoption(request,id):
    if 'suname' in request.session:
        return render(request,'User3/ad_user_adopted_frm.html',{'rescue_id':id})
    else:
       return redirect('/login')

def save_send_to_adopton(request,id):
    if 'suname' in request.session:
        rescue_id=id
        tbl=Rescue_info.objects.get(rescue_id=rescue_id)
        tbl.status="User Adoption"
        tbl.save()
        id=request.session['slogid']
        a=request.POST.get("animal_name")
        b=request.POST.get("tagname")
        c=request.POST.get("breed")
        d=request.POST.get("age")
        e=request.POST.get("gender")
        f=request.POST.get("date")
        photo=request.FILES['photo']
        #set up for file name
        split_tup = os.path.splitext(photo.name)
        file_extension = split_tup[1]
        dir_path = settings.MEDIA_ROOT
        count = 0
        for path in os.listdir(dir_path):

            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
        filecount=count+1
        filename=str(filecount)+"."+file_extension
        #end
        #upload
        obj=FileSystemStorage()
        file=obj.save(filename,photo)
        #end
        url1=obj.url(file)
        obj = adoption_info(pet_type=a,tag_name=b,breed=c,age=d,gender=e,date=f,photo=url1,Ac_login_id=id,rescue_id=rescue_id)
        obj.save()
        messages.add_message(request, messages.INFO, 'Added successfully.')
        return redirect('/ad_Adoption')
    else:
       return redirect('/login')
def ad_Adoption(request):
    if 'suname' in request.session:
        id=request.session['slogid']
        data=adoption_info.objects.filter(Ac_login_id=id, status='Not Adopted')
        return render(request,'User3/ad_user_adoption_list.html',{'data':data})
    else:
       return redirect('/login')
def view_rescue_details(request,id):
    if 'suname' in request.session:
        id=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select r.*,u.* from tbl_rescue as r inner join  tbl_user_register as u  on r.user_login_id =u.login_id where r.rescue_id="+str(id))
        data=cursor.fetchall()
        return render(request,'User3/Rescue_info_details.html',{'data':data})
    else:
       return redirect('/login')

#user Adoption
def Adoption(request):
    if 'suname' in request.session:
        data = country.objects.all()
        data1=adoption_info.objects.filter(status='Not Adopted')
        return render(request,'User2/adoption.html',{'data':data,'data1':data1})
    else:
       return redirect('/login')
def book_adoption(request,id):
     if 'suname' in request.session:
        user_id=request.session['slogid']
        tbl=adoption_info.objects.get(adoption_id=id)
        tbl.status="Booked"
        tbl.adopted_user_login_id=user_id
        tbl.save()
        return redirect('/Adoption')
     else:
       return redirect('/login')
def Booked_list(request):
    if 'suname' in request.session:
        id=request.session['slogid']

        data1=adoption_info.objects.filter(status='Booked',adopted_user_login_id=id)
        return render(request,'User2/adoption_booked_list.html',{'data1':data1})
    else:
       return redirect('/login')
def adoption_request(request):
     if 'suname' in request.session:
        id=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select r.*,u.* from tbl_adoption as r inner join  tbl_user_register as u  on r.adopted_user_login_id =u.login_id where r.status='Booked' and r.Ac_login_id="+str(id))
        data=cursor.fetchall()
        return render(request,'User3/adoption_booked_list.html',{'data':data})
     else:
       return redirect('/login')
def adopt_user_pet(request,id):
        tbl=adoption_info.objects.get(adoption_id=id)
        tbl.status="Adopted"
        tbl.save()
        return redirect('/adopted_list')
def adopted_list(request):
    if 'suname' in request.session:
        id=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select r.*,u.* from tbl_adoption as r inner join  tbl_user_register as u  on r.adopted_user_login_id =u.login_id where r.status='Adopted' and r.Ac_login_id="+str(id))
        data=cursor.fetchall()
        return render(request,'User3/adopted_list.html',{'data':data})
    else:
       return redirect('/login')
def ad_Feedback(request):
    if 'suname' in request.session:
        id=request.session['slogid']

        cursor=connection.cursor()
        cursor.execute("select f.*,u.* from tbl_feedback as f inner join  tbl_user_register as u  on f.user_login_id =u.login_id where f.reply='No' and  f.Ac_login_id="+str(id))
        data=cursor.fetchall()
        return render(request,'User3/feedback.html',{'data1':data})
    else:
       return redirect('/login')
def reply_feedback(request,id):
    if 'suname' in request.session:
        return render(request,'User3/reply_feedback.html',{'id':id})
    else:
       return redirect('/login')
def save_reply_feedback(request,id):
    if 'suname' in request.session:
        tbl=feedback.objects.get(feedback_id=id)
        tbl.reply=request.POST.get("reply")
        tbl.save()
        return redirect('/ad_replied_feedback')
    else:
       return redirect('/login')
def ad_replied_feedback(request):
    if 'suname' in request.session:
        id=request.session['slogid']

        cursor=connection.cursor()
        cursor.execute("select f.*,u.* from tbl_feedback as f inner join  tbl_user_register as u  on f.user_login_id =u.login_id where f.reply!='No' and  f.Ac_login_id="+str(id))
        data=cursor.fetchall()
        return render(request,'User3/replied_feedback.html',{'data1':data})
    else:
       return redirect('/login')
def ad_Profile(request):
    if 'suname' in request.session:
        id=request.session['slogid']
        data=adoption_center_register.objects.filter(login_id=id)
        return render(request,'User3/profile.html',{'data':data})
    else:
       return redirect('/login')
def ad_edit_profile(request):
    if 'suname' in request.session:
        id=request.session['slogid']
        data=adoption_center_register.objects.filter(login_id=id)
        return render(request,'User3/edit_profile.html',{'data':data})
    else:
       return redirect('/login')
def save_profile_agency(request,id):
        if 'suname' in request.session:
            id=request.session['slogid']
            u=adoption_center_register.objects.get(login_id=id)
            u.agency_name=request.POST.get("aname")
            u.phone_number =request.POST.get("phone")
            u.address=request.POST.get("address")
            u.mail_id=request.POST.get("mail_id")

            u.save()
            messages.add_message(request, messages.INFO, 'Updated successfully.')
            return redirect('/ad_Profile')
        else:
          return redirect('/login')
def ad_change_password(request):
    if 'suname' in request.session:

        return render(request,'User3/change_password.html')
    else:
       return redirect('/login')
def ad_update_password(request):
    if 'suname' in request.session:
        id=request.session['slogid']
        opass=request.POST.get("opassword")
        npass=request.POST.get("password")
        obj1=login.objects.filter(login_id=id,password=opass)
        if(obj1):
            tbl1=login.objects.get(login_id=id)
            tbl1.password=npass
            tbl1.save()
            messages.add_message(request, messages.INFO, 'Updated Please Login Using new Password.')
            return redirect('/login')
        else:
            messages.add_message(request, messages.INFO, 'Invalid Data')
            return redirect('/ad_change_password')
    else:
       return redirect('/login')
def view_complaints(request):
    if 'suname' in request.session:
        cursor=connection.cursor()
        cursor.execute("select c.*,u.* from  tbl_complaint  as c inner join  tbl_user_register as u  on c.user_login_id =u.login_id where c.reply='No'  order by c.complaint_id desc")
        data=cursor.fetchall()
        return render(request,'User1/view_complaints.html',{'data':data})
    else:
       return redirect('/login')
def replied_list(request):
    if 'suname' in request.session:
        cursor=connection.cursor()
        cursor.execute("select c.*,u.* from  tbl_complaint  as c inner join  tbl_user_register as u  on c.user_login_id =u.login_id where c.reply!='No' order by c.complaint_id desc")
        data=cursor.fetchall()
        return render(request,'User1/replied_complaints.html',{'data':data})
    else:
       return redirect('/login')
def adm_reply_complaint(request,id):
    if 'suname' in request.session:

        return render(request,'User1/reply_complaint.html',{'id':id})
    else:
       return redirect('/login')
def add_reply(request,id):
    tbl=complaint.objects.get(complaint_id=id)
    tbl.reply=request.POST.get("reply")
    tbl.save()
    return redirect('/replied_list')
def stray_dogs(request):
    if 'suname' in request.session:

        cursor=connection.cursor()
        cursor.execute("select r.*,a.agency_name,c.country,s.state,d.district,p.place from tbl_rescue as r inner join  tbl_agency_register  as a on r.Ac_login_id =a.login_id  inner join tbl_place as p on a.place_id=p.place_id inner join  tbl_district as d on p.district_id_id =d.district_id inner join tbl_state as s on d.state_id_id=s.state_id inner join tbl_country  as c on s.country_id_id=c.country_id")
        data=cursor.fetchall()
        return render(request,'User1/Stray_animals_Rescue_Info.html',{'data':data})
    else:
       return redirect('/login')
def adoption(request):
    if 'suname' in request.session:
        id=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select r.*,u.*,a.agency_name,c.country,s.state,d.district,p.place,a.phone_number,a.mail_id,a.address  from tbl_adoption as r inner join  tbl_user_register as u  on r.adopted_user_login_id =u.login_id inner join   tbl_agency_register  as a on r.Ac_login_id =a.login_id  inner join tbl_place as p on a.place_id=p.place_id inner join  tbl_district as d on p.district_id_id =d.district_id inner join tbl_state as s on d.state_id_id=s.state_id inner join tbl_country  as c on s.country_id_id=c.country_id where r.status='Adopted'")
        data=cursor.fetchall()
        return render(request,'User1/adopted_list.html',{'data':data})
    else:
       return redirect('/login')

def users(request):
    if 'suname' in request.session:
        id=request.session['slogid']
        data=user_register.objects.all()
        return render(request,'User1/users.html',{'data':data})
    else:
       return redirect('/login')
def feedback_adm(request):
    if 'suname' in request.session:
        cursor=connection.cursor()
        cursor.execute("select f.*,u.*,a.agency_name,c.country,s.state,d.district,p.place,a.phone_number,a.mail_id,a.address  from tbl_feedback as f inner join  tbl_user_register as u  on f.user_login_id =u.login_id inner join   tbl_agency_register  as a on f.Ac_login_id =a.login_id  inner join tbl_place as p on a.place_id=p.place_id inner join  tbl_district as d on p.district_id_id =d.district_id inner join tbl_state as s on d.state_id_id=s.state_id inner join tbl_country  as c on s.country_id_id=c.country_id")
        data=cursor.fetchall()

        return render(request,'User1/feedback.html',{'data':data})
    else:
       return redirect('/login')

# ad_Boarding
def ad_Boarding(request):
    if 'suname' in request.session:
        id=request.session['slogid']
        data=boarding_service.objects.filter(Ac_login_id=id)
        return render(request,'User3/ad_Boarding.html',{'data':data})
    else:
       return redirect('/login')
def save_boarding_services(request):
    if 'suname' in request.session:
        id=request.session['slogid']
        t=request.POST.get("animal_name")
        c=request.POST.get("cost")
        tbl=boarding_service.objects.filter(Ac_login_id=id,pet_type=t)
        if tbl:
            messages.add_message(request, messages.INFO, 'Already Added. Pleace Edit services')
            return redirect('/ad_Boarding')
        else:
            u=boarding_service()
            u.pet_type=t
            u.cost =c
            u.Ac_login_id =id
            u.save()
            messages.add_message(request, messages.INFO, 'Added successfully.')
            return redirect('/ad_Boarding')
    else:
        return redirect('/login')
def edit_boarding_services(request,id):
    if 'suname' in request.session:

            data=boarding_service.objects.filter(b_service_id=id)
            return render(request,'User3/ad_Boarding_edit.html',{'data':data})
    else:
        return redirect('/login')
def update_boarding_services(request,id):
    if 'suname' in request.session:
            u=boarding_service.objects.get(b_service_id=id)
            u.pet_type=request.POST.get("animal_name")
            u.cost=request.POST.get("cost")
            u.save()
            messages.add_message(request, messages.INFO, 'Updated successfully.')
            return redirect('/ad_Boarding')
    else:
        return redirect('/login')
def delete_boarding_services(request,id):
    if 'suname' in request.session:
        tbl=boarding_service.objects.get(b_service_id=id)
        tbl.delete()
        messages.add_message(request, messages.INFO, 'Deleted successfully.')
        return redirect('/ad_Boarding')
    else:
       return redirect('/login')

#grooming
def ad_Grooming(request):
    if 'suname' in request.session:
        id=request.session['slogid']
        data=grooming_service.objects.filter(Ac_login_id=id)
        return render(request,'User3/ad_Grooming.html',{'data':data})
    else:
       return redirect('/login')

def save_grooming_services(request):
    if 'suname' in request.session:
        id=request.session['slogid']
        sname=request.POST.get("servicename")
        type=request.POST.get("animal_name")
        cost=request.POST.get("cost")
        description=request.POST.get("description")
        tbl=grooming_service.objects.filter(Ac_login_id=id,service_name =sname,pet_type=type)
        if tbl:
            messages.add_message(request, messages.INFO, 'Already Added. Pleace Edit services')
            return redirect('/ad_Grooming')
        else:
            u=grooming_service()
            u.service_name =sname
            u.pet_type =type
            u.description =description
            u.cost=cost
            u.Ac_login_id =id
            u.save()
            messages.add_message(request, messages.INFO, 'Added successfully.')
            return redirect('/ad_Grooming')
    else:
        return redirect('/login')

def edit_grooming_services(request,id):
    if 'suname' in request.session:

            data=grooming_service.objects.filter(g_service_id=id)
            return render(request,'User3/ad_grooming_edit.html',{'data':data})
    else:
        return redirect('/login')
def update_grooming_services(request,id):
    if 'suname' in request.session:


        logid=request.session['slogid']
        sname=request.POST.get("servicename")
        type=request.POST.get("animal_name")
        cost=request.POST.get("cost")
        description=request.POST.get("description")
        u=grooming_service.objects.get(g_service_id=id)
        u.service_name =sname
        u.pet_type =type
        u.description =description
        u.cost=cost
        u.Ac_login_id =logid
        u.save()
        messages.add_message(request, messages.INFO, 'Updated successfully.')
        return redirect('/ad_Grooming')
    else:
        return redirect('/login')

def delete_grooming_services(request,id):
    if 'suname' in request.session:
        tbl=grooming_service.objects.get(g_service_id=id)
        tbl.delete()
        messages.add_message(request, messages.INFO, 'Deleted successfully.')
        return redirect('/ad_Grooming')
    else:
       return redirect('/login')
def Boarding(request):
    if 'suname' in request.session:
      data = country.objects.all()
      return render(request,'User2/boarding.html',{'data':data})
    else:
       return redirect('/login')
def display_boarding(request):
    ad = request.GET.get("ad")
    try:

        res = boarding_service.objects.filter(Ac_login_id = ad)
    except Exception:
        data=[]
        data['error_message'] = 'error'
        return JsonResponse(data)
    return JsonResponse(list(res.values('b_service_id', 'pet_type', 'cost')), safe = False)
def book_boarding_services(request,id):
    if 'suname' in request.session:
            login_id=request.session['slogid']
            data=pets.objects.filter(user_login_id=login_id)
            return render(request,'User2/book_boarding_service.html',{'id':id,'data':data})
    else:
        return redirect('/login')
def save_boarding_booking(request,id):
    if 'suname' in request.session:
            user_login_id=request.session['slogid']
            sdate=request.POST.get("sdate")
            edate=request.POST.get("edate")
            pet_id=request.POST.get("pets")
            b_service_id=id
            u=booking_boarding()
            u.starting_date =sdate
            u.ending_date =edate
            u.pet_id =pet_id
            u.b_service_id=b_service_id
            u.user_login_id =user_login_id
            u.save()
            messages.add_message(request, messages.INFO, 'Booked successfully. Check Status ')
            return redirect('/Boarding')
    else:
        return redirect('/login')
def Boarding_status(request):
 if 'suname' in request.session:
    user_login_id=request.session['slogid']
    cursor=connection.cursor()
    cursor.execute("select b.*,pt.*,bs.*,a.agency_name,c.country,s.state,d.district,p.place,a.phone_number,a.mail_id,a.address  from tbl_booking_boarding as b inner join tbl_pets as pt on pt.id=b.pet_id inner join tbl_boarding_service as bs on b.b_service_id=bs.b_service_id inner join  tbl_agency_register  as a on bs.Ac_login_id =a.login_id  inner join tbl_place as p on a.place_id=p.place_id inner join  tbl_district as d on p.district_id_id =d.district_id inner join tbl_state as s on d.state_id_id=s.state_id inner join tbl_country  as c on s.country_id_id=c.country_id where b.user_login_id="+str(user_login_id))
    data=cursor.fetchall()

    return render(request,'User2/Boarding_status.html',{'data':data})
 else:
        return redirect('/login')
def boarding_booking_list(request):
    if 'suname' in request.session:
        a_login_id=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select b.*,pt.*,bs.*,u.*  from tbl_booking_boarding as b inner join tbl_pets as pt on pt.id=b.pet_id inner join tbl_boarding_service as bs on b.b_service_id=bs.b_service_id inner join  tbl_user_register as u  on b.user_login_id =u.login_id where bs.Ac_login_id="+str(a_login_id)+" and b.status='Not Accepted'")
        data=cursor.fetchall()

        return render(request,'User3/boarding_booking_list.html',{'data':data})
    else:
        return redirect('/login')

def booking_approvel(request,id):
    if 'suname' in request.session:
        tbl=booking_boarding.objects.get(boarding_booking_id=id)
        tbl.status="Accepted"
        tbl.save()
        messages.add_message(request, messages.INFO, 'Accepted Booking successfully.')
        return redirect('/boarding_booking_list')
    else:
       return redirect('/login')
def booking_reject(request,id):
    if 'suname' in request.session:
        tbl=booking_boarding.objects.get(boarding_booking_id=id)
        tbl.status="Rejected"
        tbl.save()
        messages.add_message(request, messages.INFO, 'Rejected Booking .')
        return redirect('/boarding_booking_list')
    else:
       return redirect('/login')
def boarding_booking_accepted_list(request):
    if 'suname' in request.session:
        a_login_id=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select b.*,pt.*,bs.*,u.*  from tbl_booking_boarding as b inner join tbl_pets as pt on pt.id=b.pet_id inner join tbl_boarding_service as bs on b.b_service_id=bs.b_service_id inner join  tbl_user_register as u  on b.user_login_id =u.login_id where bs.Ac_login_id="+str(a_login_id)+" and b.status='Accepted'")
        data=cursor.fetchall()

        return render(request,'User3/boarding_booked_list.html',{'data':data})
    else:
        return redirect('/login')
def Grooming(request):
    if 'suname' in request.session:
      data = country.objects.all()
      return render(request,'User2/grooming.html',{'data':data})
    else:
       return redirect('/login')
def display_grooming(request):
    ad = request.GET.get("ad")
    try:

        res = grooming_service.objects.filter(Ac_login_id = ad)
    except Exception:
        data=[]
        data['error_message'] = 'error'
        return JsonResponse(data)
    return JsonResponse(list(res.values('g_service_id','service_name', 'pet_type', 'description',  'cost')), safe = False)
def book_grooming_services(request,id):
    if 'suname' in request.session:
            login_id=request.session['slogid']
            data=pets.objects.filter(user_login_id=login_id)
            return render(request,'User2/book_grooming_service.html',{'id':id,'data':data})
    else:
        return redirect('/login')
def save_grooming_booking(request,id):
    if 'suname' in request.session:
            user_login_id=request.session['slogid']
            date=request.POST.get("date")
            pet_id=request.POST.get("pets")
            g_service_id=id
            u=booking_grooming()
            u.date =date
            u.pet_id =pet_id
            u.g_service_id=g_service_id
            u.user_login_id =user_login_id
            u.save()
            messages.add_message(request, messages.INFO, 'Booked successfully. Check Status ')
            return redirect('/Grooming')
    else:
        return redirect('/login')
def Grooming_status(request):
    if 'suname' in request.session:
        user_login_id=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select b.*,pt.*,bs.*,a.agency_name,c.country,s.state,d.district,p.place,a.phone_number,a.mail_id,a.address  from tbl_booking_grooming as b inner join tbl_pets as pt on pt.id=b.pet_id inner join tbl_grooming_service as bs on b.g_service_id=bs.g_service_id inner join  tbl_agency_register  as a on bs.Ac_login_id =a.login_id  inner join tbl_place as p on a.place_id=p.place_id inner join  tbl_district as d on p.district_id_id =d.district_id inner join tbl_state as s on d.state_id_id=s.state_id inner join tbl_country  as c on s.country_id_id=c.country_id where b.user_login_id="+str(user_login_id))
        data=cursor.fetchall()

        return render(request,'User2/Grooming_status.html',{'data':data})
    else:
        return redirect('/login')
def grooming_booking_list(request):
    if 'suname' in request.session:
        a_login_id=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select b.*,pt.*,bs.*,u.*  from tbl_booking_grooming as b inner join tbl_pets as pt on pt.id=b.pet_id inner join tbl_grooming_service as bs on b.g_service_id=bs.g_service_id inner join  tbl_user_register as u  on b.user_login_id =u.login_id where bs.Ac_login_id="+str(a_login_id)+" and b.status='Not Accepted'")
        data=cursor.fetchall()

        return render(request,'User3/grooming_booking_list.html',{'data':data})
    else:
        return redirect('/login')
def Grooming_booking_accepted_list(request):
    if 'suname' in request.session:
        a_login_id=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select b.*,pt.*,bs.*,u.*  from tbl_booking_grooming as b inner join tbl_pets as pt on pt.id=b.pet_id inner join tbl_grooming_service as bs on b.g_service_id=bs.g_service_id inner join  tbl_user_register as u  on b.user_login_id =u.login_id where bs.Ac_login_id="+str(a_login_id)+" and b.status='Accepted'")
        data=cursor.fetchall()

        return render(request,'User3/Grooming_booking_accepted_list.html',{'data':data})
    else:
        return redirect('/login')
def booking_grooming_approvel(request,id):
    if 'suname' in request.session:
        tbl=booking_grooming.objects.get(grroming_booking_id=id)
        tbl.status="Accepted"
        tbl.save()
        messages.add_message(request, messages.INFO, 'Accepted Booking successfully.')
        return redirect('/grooming_booking_list')
    else:
       return redirect('/login')
def booking_grooming_reject(request,id):
    if 'suname' in request.session:
        tbl=booking_grooming.objects.get(grroming_booking_id=id)
        tbl.status="Rejected"
        tbl.save()
        messages.add_message(request, messages.INFO, 'Rejected Booking .')
        return redirect('/grooming_booking_list')
    else:
       return redirect('/login')
def boarding_admin(request):
    if 'suname' in request.session:

        cursor=connection.cursor()
        cursor.execute("select b.*,pt.*,bs.*,u.*,a.agency_name,c.country,s.state,d.district,p.place,a.phone_number,a.mail_id,a.address  from tbl_booking_boarding as b inner join tbl_pets as pt on pt.id=b.pet_id inner join tbl_boarding_service as bs on b.b_service_id=bs.b_service_id inner join  tbl_user_register as u  on b.user_login_id =u.login_id inner join tbl_agency_register as a  on bs.Ac_login_id = a.login_id  inner join tbl_place as p on a.place_id=p.place_id inner join  tbl_district as d on p.district_id_id =d.district_id inner join tbl_state as s on d.state_id_id=s.state_id inner join tbl_country  as c on s.country_id_id=c.country_id where b.status='Accepted'")
        data=cursor.fetchall()

        return render(request,'User1/boarding_booked_list.html',{'data':data})
    else:
        return redirect('/login')
def grooming_admin(request):
    if 'suname' in request.session:
        a_login_id=request.session['slogid']
        cursor=connection.cursor()
        cursor.execute("select b.*,pt.*,bs.*,u.*,a.agency_name,c.country,s.state,d.district,p.place,a.phone_number,a.mail_id,a.address  from tbl_booking_grooming as b inner join tbl_pets as pt on pt.id=b.pet_id inner join tbl_grooming_service as bs on b.g_service_id=bs.g_service_id inner join  tbl_user_register as u  on b.user_login_id =u.login_id inner join tbl_agency_register as a  on bs.Ac_login_id = a.login_id  inner join tbl_place as p on a.place_id=p.place_id inner join  tbl_district as d on p.district_id_id =d.district_id inner join tbl_state as s on d.state_id_id=s.state_id inner join tbl_country  as c on s.country_id_id=c.country_id where  b.status='Accepted'")
        data=cursor.fetchall()

        return render(request,'User1/Grooming_booking_accepted_list.html',{'data':data})
    else:
        return redirect('/login')
    
    
