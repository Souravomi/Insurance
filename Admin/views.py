from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from User.models import Health_Applications,Applicants,Account,Address,Bank,Nominee,Health_Insurance,Life_Childrens_Applications,Life_Childrens_Insurance,Life_Employees_Applications,Employee,Life_Employees_Insurance,Appliances_Applications,Appliances_Insurance,Vehicle_Applications,Vehicle_Insurance,Vehicle
from .models import Policies
from django.contrib.auth.models import User, auth
from datetime import datetime
from User.utils import render_to_pdf 
from django.http import HttpResponse
import xlwt

# Create your views here.


def Admin_Home(request):
    if request.method == "POST":
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Insurance Report.xls"'

        wb = xlwt.Workbook(encoding='utf-8')

        ws = wb.add_sheet('Health Insurance') # this will make a sheet named Users Data

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        bordered = 'border: top thick, right thick, bottom thick, left thick;',

        columns = ['Insurance Id','Applicant Name' ,'Category', 'Scheme', 'Scheme Amount' ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = Health_Insurance.objects.all().values_list('Insurance_Id', 'Auth_Id__Name', 'Category', 'Scheme','Scheme_Amount')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)


        ws = wb.add_sheet('General Insurance') # this will make a sheet named Users Data

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Insurance Id','Applicant Name' ,'Category', 'Scheme', 'Scheme Amount' ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = Appliances_Insurance.objects.all().values_list('Insurance_Id', 'Auth_Id__Name', 'Category', 'Scheme','Scheme_Amount')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        rows = Vehicle_Insurance.objects.all().values_list('Insurance_Id', 'Auth_Id__Name', 'Category', 'Scheme','Scheme_Amount')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

      
        ws = wb.add_sheet('Life Insurance') # this will make a sheet named Users Data

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Insurance Id','Applicant Name' ,'Category', 'Scheme', 'Scheme Amount' ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = Life_Childrens_Insurance.objects.all().values_list('Insurance_Id', 'Auth_Id__Name', 'Category', 'Scheme','Scheme_Amount')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        rows = Life_Employees_Insurance.objects.all().values_list('Insurance_Id', 'Auth_Id__Name', 'Category', 'Scheme','Scheme_Amount')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        #Save the data
        wb.save(response)

        return response
    else:
        username = request.session['username']
        health_Pen = Health_Applications.objects.filter(App_Status='Submitted')
        health = Health_Applications.objects.all()
        child_Pen = Life_Childrens_Applications.objects.filter(App_Status='Submitted')
        child = Life_Childrens_Applications.objects.all()
        emp_Pen = Life_Employees_Applications.objects.filter(App_Status='Submitted')
        emp = Life_Employees_Applications.objects.all()
        app_pen = Appliances_Applications.objects.filter(App_Status='Submitted')
        app = Appliances_Applications.objects.all()
        veh_pen = Vehicle_Applications.objects.filter(App_Status='Submitted')
        veh = Vehicle_Applications.objects.all()
        return render(request,'Admin/Home.html',{'username':username,'health':health,
        'health_Pen':health_Pen,'child_Pen':child_Pen,'child':child,'emp_Pen':emp_Pen,'emp':emp,'app_pen':app_pen,
        'app':app,'veh_pen':veh_pen,'veh':veh})


def Admin_Appliances_Applications(request):
    if 'app' in request.GET:
        val = request.GET['childid']
        data = Appliances_Applications.objects.get(Appl_Id=val)
        app = Appliances_Applications.objects.filter(App_Status='Submitted')
        return render(request,'Admin/Appliances_Applications.html',{'data':data,'app':app})
    elif request.method == 'POST':
        val = request.POST['Status']
        Email = request.POST['email']

        try:
            count = Applicants.objects.all().count()
        except:
            count = 0

        Appl_Id = int(count) + 1

        health = Appliances_Applications.objects.get(App_Status='Submitted',App_Email=Email)
        user = User.objects.get(username=Email)
            
        applicant = Applicants(Appl_Id=Appl_Id,User=user,Name=health.App_Name,Father="NA",Mother="NA",DOB=health.App_DOB,
        Gender=health.App_Gender,Qual="NA",Mobile=health.App_Mobile,Aadhar=health.App_Aadhar,Blood="NA",Email=Email)
        applicant.save()

        address = Address(Auth_Id=applicant,Addr1=health.Addr1,Addr2=health.Addr2,
        Addr3=health.Addr3,Pin=health.Pin)
        address.save()

        #Auto Id Generation
   
        myDate = datetime.now() 
        D = myDate.strftime("%d")  
        M = myDate.strftime("%m")  
        Y = myDate.strftime("%Y")  
        X = "1004" + Y + M + D  

        count = Appliances_Insurance.objects.filter(Insurance_Id__contains=X).count()  #Get total number of records

        if count == 0:
            n = "01"
            X = X + str(n)
        else:
            n = count + 1
            if len(str(n)) == 1:
                n = "0" + str(n)
            X = X + n
        print (X)

        account = Account(Auth_Id=applicant,Category=health.Category,Scheme=health.Scheme,
        Scheme_Amount=health.Scheme_Amount,Balance_Amount=health.Scheme_Amount,last_Paid=myDate)
        account.save()

        insurance = Appliances_Insurance(Auth_Id=applicant,Insurance_Id=X,Category=health.Category,Scheme=health.Scheme,
        Scheme_Amount=health.Scheme_Amount,App_Aadhar_Id=health.App_Aadhar_Id,Addr_Id=health.Addr_Id,App_Status=val,Policy_Date=myDate)
        insurance.save()

        health.App_Status = val
        health.save()

        return redirect('Admin_Appliances_Applications')
    else:
        app = Appliances_Applications.objects.filter(App_Status='Submitted')
        return render(request,'Admin/Appliances_Applications.html',{'app':app})


def Admin_Vehicle_Applications(request):
    if 'app' in request.GET:
        val = request.GET['vehid']
        data = Vehicle_Applications.objects.get(Appl_Id=val)
        veh = Vehicle_Applications.objects.filter(App_Status='Submitted')
        return render(request,'Admin/Vehicle_Applications.html',{'data':data,'veh':veh})
    elif request.method == 'POST':
        val = request.POST['Status']
        Email = request.POST['email']

        try:
            count = Applicants.objects.all().count()
        except:
            count = 0

        Appl_Id = int(count) + 1

        health = Vehicle_Applications.objects.get(App_Status='Submitted',App_Email=Email)
        user = User.objects.get(username=Email)
            
        applicant = Applicants(Appl_Id=Appl_Id,User=user,Name=health.App_Name,Father="NA",Mother="NA",DOB=health.App_DOB,
        Gender=health.App_Gender,Qual="NA",Mobile=health.App_Mobile,Aadhar=health.App_Aadhar,Blood="NA",Email=Email)
        applicant.save()

        address = Address(Auth_Id=applicant,Addr1=health.Addr1,Addr2=health.Addr2,
        Addr3=health.Addr3,Pin=health.Pin)
        address.save()

        Veh = Vehicle(Auth_Id=applicant,Vehicle_Class=health.Vehicle_Class,Mnf_Date=health.Mnf_Date,
        Chassis=health.Chassis,Engine=health.Engine)
        Veh.save()

        #Auto Id Generation
   
        myDate = datetime.now() 
        D = myDate.strftime("%d")  
        M = myDate.strftime("%m")  
        Y = myDate.strftime("%Y")  
        X = "1005" + Y + M + D  

        count = Vehicle_Insurance.objects.filter(Insurance_Id__contains=X).count()  #Get total number of records

        if count == 0:
            n = "01"
            X = X + str(n)
        else:
            n = count + 1
            if len(str(n)) == 1:
                n = "0" + str(n)
            X = X + n
        print (X)

        account = Account(Auth_Id=applicant,Category=health.Category,Scheme=health.Scheme,
        Scheme_Amount=health.Scheme_Amount,Balance_Amount=health.Scheme_Amount,last_Paid=myDate)
        account.save()

        insurance = Vehicle_Insurance(Auth_Id=applicant,Insurance_Id=X,Category=health.Category,Scheme=health.Scheme,
        Scheme_Amount=health.Scheme_Amount,App_Aadhar_Id=health.App_Aadhar_Id,Rc_Id=health.Rc_Id,image=health.image,App_Status=val,Policy_Date=myDate)
        insurance.save()

        health.App_Status = val
        health.save()

        return redirect('Admin_Vehicle_Applications')
    else:
        veh = Vehicle_Applications.objects.filter(App_Status='Submitted')
        return render(request,'Admin/Vehicle_Applications.html',{'veh':veh})


def Admin_Life(request):
    child = Life_Childrens_Insurance.objects.all()
    emp = Life_Employees_Insurance.objects.all()
    return render(request,'Admin/Life_Insurance.html',{'child':child,'emp':emp})


def Admin_Life_Children_Application(request):
    if 'child' in request.GET:
        val = request.GET['childid']
        data = Life_Childrens_Applications.objects.get(Appl_Id=val)
        child = Life_Childrens_Applications.objects.filter(App_Status='Submitted')
        return render(request,'Admin/Admin_Life_Children_Application.html',{'child':child,'data':data})
    elif request.method == "POST":
        val = request.POST['Status']
        Email = request.POST.get('email')

        try:
            count = Applicants.objects.all().count()
        except:
            count = 0

        Appl_Id = int(count) + 1

        health = Life_Childrens_Applications.objects.get(App_Status='Submitted',App_Email=Email)
        user = User.objects.get(username=Email)
            
        applicant = Applicants(Appl_Id=Appl_Id,User=user,Name=health.App_Name,Father=health.App_Father,Mother=health.App_Mother,DOB=health.App_DOB,
        Gender=health.App_Gender,Mobile=health.App_Mobile,Email=Email)
        applicant.save()

        address = Address(Auth_Id=applicant,Addr1=health.Addr1,Addr2=health.Addr2,
        Addr3=health.Addr3,Pin=health.Pin)
        address.save()

        nominee = Nominee(Auth_Id=applicant,Name=health.Nom_Name,DOB=health.Nom_DOB,Relation=health.Relation,
        Gender=health.Nom_Gender,Aadhar=health.Nom_Aadhar,Mobile=health.Nom_Mobile,Email=health.Nom_Email)
        nominee.save()

        #Auto Id Generation
   
        myDate = datetime.now() 
        D = myDate.strftime("%d")  
        M = myDate.strftime("%m")  
        Y = myDate.strftime("%Y")  
        X = "1002" + Y + M + D  

        count = Life_Childrens_Insurance.objects.filter(Insurance_Id__contains=X).count()  #Get total number of records
   
        if count == 0:
            n = "01"
            X = X + str(n)
        else:
            n = count + 1
            if len(str(n)) == 1:
                n = "0" + str(n)
            X = X + n
        print (X)

        account = Account(Auth_Id=applicant,Category=health.Category,Scheme=health.Scheme,
        Scheme_Amount=health.Scheme_Amount,Balance_Amount=health.Scheme_Amount,last_Paid=myDate)
        account.save()

        insurance = Life_Childrens_Insurance(Auth_Id=applicant,Insurance_Id=X,Category=health.Category,Scheme=health.Scheme,
        Scheme_Amount=health.Scheme_Amount,Nom_Aadhar_Id=health.Nom_Aadhar_Id,Birth_Id=health.Birth_Id,App_Status=val,Policy_Date=myDate)
        insurance.save()

        health.App_Status = val
        health.save()
            
        return redirect('Admin_Life_Children_Application')
    else:
        child = Life_Childrens_Applications.objects.filter(App_Status='Submitted')
        return render(request,'Admin/Admin_Life_Children_Application.html',{'child':child})


def Admin_Life_Employee_Application(request):
    if 'emp' in request.GET:
        val = request.GET['empid']
        data = Life_Employees_Applications.objects.get(Appl_Id=val)
        emp = Life_Employees_Applications.objects.filter(App_Status='Submitted')
        return render(request,'Admin/Admin_Life_Employee_Application.html',{'emp':emp,'data':data})
    elif request.method == 'POST':
        val = request.POST['Status']
        Email = request.POST.get('email')

        try:
            count = Applicants.objects.all().count()
        except:
            count = 0

        Appl_Id = int(count) + 1

        health = Life_Employees_Applications.objects.get(App_Status='Submitted',App_Email=Email)
        user = User.objects.get(username=Email)
            
        applicant = Applicants(Appl_Id=Appl_Id,User=user,Name=health.App_Name,Father=health.App_Father,Mother=health.App_Mother,DOB=health.App_DOB,
        Gender=health.App_Gender,Qual=health.App_Qual,Mobile=health.App_Mobile,Aadhar=health.App_Aadhar,Blood=health.App_Blood,Email=Email)
        applicant.save()

        address = Address(Auth_Id=applicant,Addr1=health.Addr1,Addr2=health.Addr2,
        Addr3=health.Addr3,Pin=health.Pin)
        address.save()

        emp = Employee(Auth_Id=applicant,Job_Type=health.Job_Type,Company=health.Company,Company_Address=health.Company_Address,
        Company_Pincode=health.Company_Pincode)
        emp.save()

        bank = Bank(Auth_Id=applicant,Bank_Account=health.Bank_Account,Bank_Name=health.Bank_Name,
        Account_Number=health.Account_Number,IFSC=health.IFSC,Branch=health.Branch)
        bank.save()

        nominee = Nominee(Auth_Id=applicant,Name=health.Nom_Name,DOB=health.Nom_DOB,Relation=health.Relation,
        Gender=health.Nom_Gender,Aadhar=health.Nom_Aadhar,Mobile=health.Nom_Mobile,Email=health.Nom_Email)
        nominee.save()

        #Auto Id Generation
   
        myDate = datetime.now() 
        D = myDate.strftime("%d")  
        M = myDate.strftime("%m")  
        Y = myDate.strftime("%Y")  
        X = "1003" + Y + M + D  

        count = Life_Employees_Insurance.objects.filter(Insurance_Id__contains=X).count()  #Get total number of records

        
        if count == 0:
            n = "01"
            X = X + str(n)
        else:
            n = count + 1
            if len(str(n)) == 1:
                n = "0" + str(n)
            X = X + n
        print (X)

        account = Account(Auth_Id=applicant,Category=health.Category,Scheme=health.Scheme,
        Scheme_Amount=health.Scheme_Amount,Balance_Amount=health.Scheme_Amount,last_Paid=myDate)
        account.save()

        insurance = Life_Employees_Insurance(Auth_Id=applicant,Insurance_Id=X,Category=health.Category,Scheme=health.Scheme,
        Scheme_Amount=health.Scheme_Amount,App_Aadhar_Id=health.App_Aadhar_Id,Nom_Aadhar_Id=health.Nom_Aadhar_Id,
        Employement_Id=health.Employement_Id,image=health.image,App_Status=val,Policy_Date=myDate)
        insurance.save()

        health.App_Status = val
        health.save()

        return redirect('Admin_Life_Employee_Application')
    else:
        emp = Life_Employees_Applications.objects.filter(App_Status='Submitted')
        return render(request,'Admin/Admin_Life_Employee_Application.html',{'emp':emp})


def Admin_General(request):
    vehicle = Vehicle_Insurance.objects.all()
    app = Appliances_Insurance.objects.all()
    return render(request,'Admin/General_Insurance.html',{'vehicle':vehicle,'app':app})
    

def Admin_Health(request):
    if request.method == 'GET':
        val = request.GET.get('id')
        if val is not None:
            print(val)
            data = Health_Applications.objects.get(Appl_Id=val)
            health = Health_Applications.objects.filter(App_Status='Submitted')
            return render(request,'Admin/Health_Insurance.html',{'data':data,'health':health})
        else:
            health = Health_Applications.objects.filter(App_Status='Submitted')
            return render(request,'Admin/Health_Insurance.html',{'health':health})
    elif request.method == 'POST':
        val = request.POST['Status']
        Email = request.POST.get('email')

        try:
            count = Applicants.objects.all().count()
        except:
            count = 0

        Appl_Id = int(count) + 1

        health = Health_Applications.objects.get(App_Status='Submitted',App_Email=Email)
        user = User.objects.get(username=Email)
            
        applicant = Applicants(Appl_Id=Appl_Id,User=user,Name=health.App_Name,Father=health.App_Father,Mother=health.App_Mother,DOB=health.App_DOB,
        Gender=health.App_Gender,Qual=health.App_Qual,Mobile=health.App_Mobile,Aadhar=health.App_Aadhar,Blood=health.App_Blood,Email=Email)
        applicant.save()

        address = Address(Auth_Id=applicant,Addr1=health.Addr1,Addr2=health.Addr2,
        Addr3=health.Addr3,Pin=health.Pin)
        address.save()

        bank = Bank(Auth_Id=applicant,Bank_Account=health.Bank_Account,Bank_Name=health.Bank_Name,
        Account_Number=health.Account_Number,IFSC=health.IFSC,Branch=health.Branch)
        bank.save()

        nominee = Nominee(Auth_Id=applicant,Name=health.Nom_Name,DOB=health.Nom_DOB,Relation=health.Relation,
        Gender=health.Nom_Gender,Aadhar=health.Nom_Aadhar,Mobile=health.Nom_Mobile,Email=health.Nom_Email)
        nominee.save()

        #Auto Id Generation
   
        myDate = datetime.now() 
        D = myDate.strftime("%d")  
        M = myDate.strftime("%m")  
        Y = myDate.strftime("%Y")  
        X = "1001" + Y + M + D  

        count = Health_Insurance.objects.filter(Insurance_Id__contains=X).count()  #Get total number of records

        
        if count == 0:
            n = "01"
            X = X + str(n)
        else:
            n = count + 1
            if len(str(n)) == 1:
                n = "0" + str(n)
            X = X + n
        print (X)

        account = Account(Auth_Id=applicant,Category=health.Category,Scheme=health.Scheme,
        Scheme_Amount=health.Scheme_Amount,Balance_Amount=health.Scheme_Amount,last_Paid=myDate)
        account.save()

        insurance = Health_Insurance(Auth_Id=applicant,Insurance_Id=X,Category=health.Category,Scheme=health.Scheme,
        Scheme_Amount=health.Scheme_Amount,App_Aadhar_Id=health.App_Aadhar_Id,Nom_Aadhar_Id=health.Nom_Aadhar_Id,
        Birth_Id=health.Birth_Id,image=health.image,App_Status=val,Policy_Date=myDate)
        insurance.save()

        health.App_Status = val
        health.save()

        health = Health_Applications.objects.filter(App_Status='Submitted')
        return render(request,'Admin/Health_Insurance.html',{'health':health})  
    else:    
        health = Health_Applications.objects.filter(App_Status='Submitted')
        return render(request,'Admin/Health_Insurance.html',{'health':health})


def Admin_Health_Insurance(request):
    health = Health_Insurance.objects.all()
    return render(request,'Admin/Health.html',{'health':health})


def Users(request):
    if request.method == "POST":
        val = request.POST['username']
        try:
            user = User.objects.get(is_staff='0',username=val)
        except:
            user = None

        if user is not None:
            user = User.objects.filter(is_staff='0',username=val)
            return render(request,'Admin/Users.html',{'user':user})
        else:
            messages.success(request,'Current Password Entered Incorrect!')
            user = User.objects.filter(is_staff='0')
            return render(request,'Admin/Users.html',{'user':user})
    else:
        user = User.objects.filter(is_staff='0')
        return render(request,'Admin/Users.html',{'user':user})


def Search(request):
    if request.method == "POST":
        val = request.POST['username']
        try:
            user = User.objects.get(is_staff='0',username=val)
        except:
            user = None

        if user is not None:
            user = User.objects.filter(is_staff='0',username=val)
            try:
                applicant = Applicants.objects.filter(Email=val)
            except:
                applicant = None

            print(applicant)
            health = []
            child = []
            emp = []
            app = []
            veh = []
            for data in applicant:
                try:
                    H = Health_Insurance.objects.get(Auth_Id=data)
                except:
                    H = None
                try:
                    C = Life_Childrens_Insurance.objects.get(Auth_Id=data)
                except:
                    C = None
                try:
                    E = Life_Employees_Insurance.objects.get(Auth_Id=data)
                except:
                    E = None
                try:
                    A = Appliances_Insurance.objects.get(Auth_Id=data)
                except:
                    A = None
                try:
                    V = Vehicle_Insurance.objects.get(Auth_Id=data)
                except:
                    V = None
                
                if H is not None:
                    health.append(H)
                if C is not None:
                    child.append(C)
                if E is not None:
                    emp.append(E)
                if A is not None:
                    app.append(A)
                if V is not None:
                    veh.append(V)
                
                

            return render(request,'Admin/Search.html',{'user':user,'health':health,'child':child,
            'emp':emp,'app':app,'veh':veh})
        else:
            messages.success(request,'Current Password Entered Incorrect!')
            user = User.objects.filter(is_staff='0',is_superuser='1')
            return render(request,'Admin/Search.html',{'user':user})
    else:
        user = User.objects.filter(is_staff='0',is_superuser='1')
        return render(request,'Admin/Search.html',{'user':user})


def Policy(request):
    if request.method == "POST":
        Policy = request.POST['Policy']
        Category = request.POST['Category']
        Scheme = request.POST['Scheme']
        Scheme_Amount = request.POST['Samount']
        Maturity_Amount = request.POST['Mamount']
        Maturity_Period = request.POST['Period']

        policy = Policies(Policy=Policy,Category=Category,Scheme=Scheme,Scheme_Amount=Scheme_Amount,
        Maturity_Amount=Maturity_Amount,Maturity_Period=Maturity_Period)
        policy.save()

        return redirect('Policy')
    else:
        policy = Policies.objects.all()
        return render(request,'Admin/Policy.html',{'policy':policy})


def Download_Life(request):
    if 'emp' in request.GET:
        num = request.GET['polnum']

        try:
            fetch = Life_Employees_Insurance.objects.get(Insurance_Id=num)
            check = not None
        except:       
            messages.success(request,'Invalid Details')
            check = None

        if check is not None :
            data = Life_Employees_Insurance.objects.get(Insurance_Id=num)
            time =  datetime.now()
            pdf = render_to_pdf('pdf/Health.html', {'data':data,'time':time})
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "Document_%s.pdf" %(data.Insurance_Id)
                content = "attachment; filename=%s" %(filename)
                response['Content-Disposition'] = content
                return response
            else:
                return HttpResponse("Not found")
    elif 'child' in request.GET:
        num = request.GET['polnum']

        try:
            fetch = Life_Childrens_Insurance.objects.get(Insurance_Id=num)
            check = not None
        except:       
            messages.success(request,'Invalid Details')
            check = None

        if check is not None :
            data = Life_Childrens_Insurance.objects.get(Insurance_Id=num)
            time =  datetime.now()
            pdf = render_to_pdf('pdf/Health.html', {'data':data,'time':time})
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "Document_%s.pdf" %(data.Insurance_Id)
                content = "attachment; filename=%s" %(filename)
                response['Content-Disposition'] = content
                return response
            else:
                return HttpResponse("Not found")



def Download_General(request):
    if 'app' in request.GET:
        num = request.GET['polnum']

        try:
            fetch = Appliances_Insurance.objects.get(Insurance_Id=num)
            check = not None
        except:       
            messages.success(request,'Invalid Details')
            check = None

        if check is not None :
            data = Appliances_Insurance.objects.get(Insurance_Id=num)
            time =  datetime.now()
            pdf = render_to_pdf('pdf/Health.html', {'data':data,'time':time})
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "Document_%s.pdf" %(data.Insurance_Id)
                content = "attachment; filename=%s" %(filename)
                response['Content-Disposition'] = content
                return response
            else:
                return HttpResponse("Not found")
    elif 'vehicle' in request.GET:
        num = request.GET['polnum']

        try:
            fetch = Vehicle_Insurance.objects.get(Insurance_Id=num)
            check = not None
        except:       
            messages.success(request,'Invalid Details')
            check = None

        if check is not None :
            data = Vehicle_Insurance.objects.get(Insurance_Id=num)
            time =  datetime.now()
            pdf = render_to_pdf('pdf/Health.html', {'data':data,'time':time})
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "Document_%s.pdf" %(data.Insurance_Id)
                content = "attachment; filename=%s" %(filename)
                response['Content-Disposition'] = content
                return response
            else:
                return HttpResponse("Not found")


def Download_Health(request):
    if 'health' in request.GET:
        num = request.GET['polnum']

        try:
            fetch = Health_Insurance.objects.get(Insurance_Id=num)
            check = not None
        except:       
            messages.success(request,'Invalid Details')
            check = None

        if check is not None :
            data = Health_Insurance.objects.get(Insurance_Id=num)
            time =  datetime.now()
            pdf = render_to_pdf('pdf/Health.html', {'data':data,'time':time})
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "Document_%s.pdf" %(data.Insurance_Id)
                content = "attachment; filename=%s" %(filename)
                response['Content-Disposition'] = content
                return response
            else:
                return HttpResponse("Not found")


def Logout(request):
    logout(request)
    return redirect('/')