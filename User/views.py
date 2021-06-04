from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from datetime import datetime
from .utils import Calculate
from .models import Health_Applications,Applicants,Account,Address,Bank,Nominee,Health_Insurance,Life_Childrens_Applications,Life_Employees_Applications,Appliances_Applications,Appliances_Insurance,Life_Childrens_Insurance,Life_Employees_Insurance,Vehicle_Applications,Vehicle_Insurance
from django.http import HttpResponse
from .utils import render_to_pdf 

# Create your views here.

@login_required(login_url='/Login')
def Home(request):
    username = request.session['username']
    return render(request,'User/Home.html',{'username':username})


@login_required(login_url='/Login')
def Life_Children(request):
    if request.method == "POST":
        Category = "Children's"
        App_Name = request.POST['Name']
        App_Father = request.POST['Father']
        App_Mother = request.POST['Mother']
        App_DOB = request.POST['Dob']
        App_Gender = request.POST['Gender']
        App_Mobile = request.POST['Mobile']
        App_Email = request.POST['Email']
        Addr1 = request.POST['Ad1']
        Addr2 = request.POST['Ad2']
        Addr3 = request.POST['Ad3']
        Pin = request.POST['Pin']
        Nom_Name = request.POST['Nominee']
        Nom_DOB = request.POST['nomdob']
        Relation = request.POST['Relation']
        Nom_Gender = request.POST['nomgender']
        Nom_Aadhar = request.POST['nomaadhar']
        Nom_Mobile = request.POST['nommob']
        Nom_Email = request.POST['nomemail']
        Scheme = request.POST['plan']
        Scheme_Amount = request.POST['paid']
        Nom_Aadhar_Id = request.FILES['nom_Aadhr']
        Birth_Id = request.FILES['birth']
        Payment_Card = request.POST['cardno']
        Name_Card = request.POST['namecard']
        Paid_Amount = request.POST['paid']

        #Auto Id Generation
   
        myDate = datetime.now() 
        D = myDate.strftime("%d")  
        M = myDate.strftime("%m")  
        Y = myDate.strftime("%Y")  
        X = "APLC" + Y + M + D  

        #result = table.objects.filter(string__contains='pattern')
        count = Life_Childrens_Applications.objects.filter(Appl_Id__contains=X).count()  #Get total number of records

        
        if count == 0:
            n = "01"
            X = X + str(n)
        else:
            n = count + 1
            if len(str(n)) == 1:
                n = "0" + str(n)
            X = X + n
            print (X)

        app = Life_Childrens_Applications(Appl_Id=X,Category=Category,App_Name=App_Name,App_Father=App_Father,App_Mother=App_Mother,
        App_DOB=App_DOB,App_Gender=App_Gender,App_Mobile=App_Mobile,App_Email=App_Email,Addr1=Addr1,Addr2=Addr2,Addr3=Addr3,Pin=Pin,Nom_Name=Nom_Name,
        Nom_DOB=Nom_DOB,Relation=Relation,Nom_Gender=Nom_Gender,Nom_Aadhar = Nom_Aadhar,Nom_Mobile=Nom_Mobile,Nom_Email=Nom_Email,Scheme=Scheme,
        Scheme_Amount=Scheme_Amount,Nom_Aadhar_Id=Nom_Aadhar_Id,Birth_Id=Birth_Id,Payment_Card=Payment_Card,Name_Card=Name_Card,Paid_Amount=Paid_Amount)

        app.save()
        print("Saved====================================")
        return redirect('Home')
    else:
        username = request.session['username']
        return render(request,'User/Lifeinsurance.html',{'username':username})


@login_required(login_url='/Login')
def Life_Employ(request):
    if request.method == "POST":
        Category = "Employees"
        App_Name = request.POST['Name']
        App_Father = request.POST['Father']
        App_Mother = request.POST['Mother']
        App_DOB = request.POST['Dob']
        App_Gender = request.POST['Gender']
        App_Qual = request.POST['Qualification']
        App_Mobile = request.POST['Mobile']
        App_Aadhar = request.POST['Aadhar']
        App_Blood = request.POST['Blood']
        App_Email = request.POST['Email']
        Addr1 = request.POST['Ad1']
        Addr2 = request.POST['Ad2']
        Addr3 = request.POST['Ad3']
        Pin = request.POST['Pin']
        Job_Type = request.POST['Job_Type']
        Company = request.POST['Company']
        Company_Address = request.POST['Company_Address']
        Company_Pincode = request.POST['Company_Pincode']
        Nom_Name = request.POST['Nominee']
        Nom_DOB = request.POST['nomdob']
        Relation = request.POST['Relation']
        Nom_Gender = request.POST['nomgender']
        Nom_Aadhar = request.POST['nomaadhar']
        Nom_Mobile = request.POST['nommob']
        Nom_Email = request.POST['nomemail']
        Bank_Account = request.POST['account']
        Bank_Name = request.POST['Bankname']
        Account_Number = request.POST['accountnumber']
        IFSC = request.POST['ifsc']
        Branch = request.POST['branch']
        Scheme = request.POST['plan']
        Scheme_Amount = request.POST['paid']
        App_Aadhar_Id = request.FILES['Ap_Aadhr_Id']
        Nom_Aadhar_Id = request.FILES['nom_Aadhr_Id']
        Employement_Id = request.FILES['Employement_Id']
        image = request.FILES['img']
        Payment_Card = request.POST['cardno']
        Name_Card = request.POST['namecard']
        Paid_Amount = request.POST['paid']

        #Auto Id Generation
   
        myDate = datetime.now() 
        D = myDate.strftime("%d")  
        M = myDate.strftime("%m")  
        Y = myDate.strftime("%Y")  
        X = "APLE" + Y + M + D  

        #result = table.objects.filter(string__contains='pattern')
        count = Life_Employees_Applications.objects.filter(Appl_Id__contains=X).count()  #Get total number of records

        
        if count == 0:
            n = "01"
            X = X + str(n)
        else:
            n = count + 1
            if len(str(n)) == 1:
                n = "0" + str(n)
            X = X + n
            print (X)

        app = Life_Employees_Applications(Appl_Id=X,Category=Category,App_Name=App_Name,App_Father=App_Father,App_Mother=App_Mother,
        App_DOB=App_DOB,App_Gender=App_Gender,App_Qual=App_Qual,App_Mobile=App_Mobile,App_Aadhar=App_Aadhar,
        App_Blood=App_Blood,App_Email=App_Email,Addr1=Addr1,Addr2=Addr2,Addr3=Addr3,Pin=Pin,Job_Type=Job_Type,
        Company=Company,Company_Address=Company_Address,Company_Pincode=Company_Pincode,Nom_Name=Nom_Name,
        Nom_DOB=Nom_DOB,Relation=Relation,Nom_Gender=Nom_Gender,Nom_Aadhar = Nom_Aadhar,Nom_Mobile=Nom_Mobile,Nom_Email=Nom_Email,Bank_Account=Bank_Account,
        Bank_Name=Bank_Name,Account_Number=Account_Number,IFSC=IFSC,Branch=Branch,Scheme=Scheme,
        Scheme_Amount=Scheme_Amount,App_Aadhar_Id=App_Aadhar_Id,Nom_Aadhar_Id=Nom_Aadhar_Id,Employement_Id=Employement_Id,
        image=image,Payment_Card=Payment_Card,Name_Card=Name_Card,Paid_Amount=Paid_Amount)
        
        app.save()
        print("Saved====================================")
        return redirect('Home')
    else:
        username = request.session['username']
        return render(request,'User/LifeEmployees.html',{'username':username})


@login_required(login_url='/Login')
def Health(request):
    if request.method == "POST":
        Category = "Health"
        App_Name = request.POST['Name']
        App_Father = request.POST['Father']
        App_Mother = request.POST['Mother']
        App_DOB = request.POST['Dob']
        App_Gender = request.POST['Gender']
        App_Qual = request.POST['Qualification']
        App_Mobile = request.POST['Mobile']
        App_Aadhar = request.POST['Aadhar']
        App_Blood = request.POST['Blood']
        App_Email = request.POST['Email']
        Addr1 = request.POST['Ad1']
        Addr2 = request.POST['Ad2']
        Addr3 = request.POST['Ad3']
        Pin = request.POST['Pin']
        Nom_Name = request.POST['Nominee']
        Nom_DOB = request.POST['nomdob']
        Relation = request.POST['Relation']
        Nom_Gender = request.POST['nomgender']
        Nom_Aadhar = request.POST['nomaadhar']
        Nom_Mobile = request.POST['nommob']
        Nom_Email = request.POST['nomemail']
        Bank_Account = request.POST['account']
        Bank_Name = request.POST['Bankname']
        Account_Number = request.POST['accountnumber']
        IFSC = request.POST['ifsc']
        Branch = request.POST['branch']
        Scheme = request.POST['scheme']
        Scheme_Amount = request.POST['paid']
        App_Aadhar_Id = request.FILES['Ap_Aadhr_Id']
        Nom_Aadhar_Id = request.FILES['nom_Aadhr_Id']
        Birth_Id = request.FILES['birth']
        image = request.FILES['img']
        Payment_Card = request.POST['cardno']
        Name_Card = request.POST['namecard']
        Paid_Amount = request.POST['paid']

        #Auto Id Generation
   
        myDate = datetime.now() 
        D = myDate.strftime("%d")  
        M = myDate.strftime("%m")  
        Y = myDate.strftime("%Y")  
        X = "APH" + Y + M + D  

        #result = table.objects.filter(string__contains='pattern')
        count = Health_Applications.objects.filter(Appl_Id__contains=X).count()  #Get total number of records

        
        if count == 0:
            n = "01"
            X = X + str(n)
        else:
            n = count + 1
            if len(str(n)) == 1:
                n = "0" + str(n)
            X = X + n
            print (X)

        app = Health_Applications(Appl_Id=X,Category=Category,App_Name=App_Name,App_Father=App_Father,App_Mother=App_Mother,
        App_DOB=App_DOB,App_Gender=App_Gender,App_Qual=App_Qual,App_Mobile=App_Mobile,App_Aadhar=App_Aadhar,
        App_Blood=App_Blood,App_Email=App_Email,Addr1=Addr1,Addr2=Addr2,Addr3=Addr3,Pin=Pin,Nom_Name=Nom_Name,
        Nom_DOB=Nom_DOB,Relation=Relation,Nom_Gender=Nom_Gender,Nom_Aadhar = Nom_Aadhar,Nom_Mobile=Nom_Mobile,Nom_Email=Nom_Email,Bank_Account=Bank_Account,
        Bank_Name=Bank_Name,Account_Number=Account_Number,IFSC=IFSC,Branch=Branch,Scheme=Scheme,
        Scheme_Amount=Scheme_Amount,App_Aadhar_Id=App_Aadhar_Id,Nom_Aadhar_Id=Nom_Aadhar_Id,Birth_Id=Birth_Id,
        image=image,Payment_Card=Payment_Card,Name_Card=Name_Card,Paid_Amount=Paid_Amount)
        
        app.save()
        print("Saved====================================")
        return redirect('Home')
    else:
        username = request.session['username']
        return render(request,'User/HealthInsurance.html',{'username':username})


@login_required(login_url='/Login')
def Vehicle(request):
    if request.method == "POST":
        Category = "Vehicle"
        App_Name = request.POST['Name']
        App_DOB = request.POST['Dob']
        App_Gender = request.POST['Gender']
        App_Mobile = request.POST['Mobile']
        App_Aadhar = request.POST['Aadhar']
        App_Email = request.POST['Email']
        Addr1 = request.POST['Ad1']
        Addr2 = request.POST['Ad2']
        Addr3 = request.POST['Ad3']
        Pin = request.POST['Pin']
        Vehicle_Class = request.POST['class']
        Mnf_Date = request.POST['Mnf']
        Chassis = request.POST['Chas']
        Engine = request.POST['Eng']
        Scheme = request.POST['plan']
        Scheme_Amount = request.POST['paid']
        App_Aadhar_Id = request.FILES['Ap_Aadhr_Id']
        Rc_Id = request.FILES['Rc_Id']
        image = request.FILES['myimg']
        Payment_Card = request.POST['cardno']
        Name_Card = request.POST['namecard']
        Paid_Amount = request.POST['paid']

        #Auto Id Generation
   
        myDate = datetime.now() 
        D = myDate.strftime("%d")  
        M = myDate.strftime("%m")  
        Y = myDate.strftime("%Y")  
        X = "APGV" + Y + M + D  

        #result = table.objects.filter(string__contains='pattern')
        count = Vehicle_Applications.objects.filter(Appl_Id__contains=X).count()  #Get total number of records

        
        if count == 0:
            n = "01"
            X = X + str(n)
        else:
            n = count + 1
            if len(str(n)) == 1:
                n = "0" + str(n)
            X = X + n
            print (X)


        app = Vehicle_Applications(Appl_Id=X,Category=Category,App_Name=App_Name,App_DOB=App_DOB,
        App_Gender=App_Gender,App_Mobile=App_Mobile,App_Aadhar=App_Aadhar,App_Email=App_Email,Addr1=Addr1,
        Addr2=Addr2,Addr3=Addr3,Pin=Pin,Vehicle_Class=Vehicle_Class,Mnf_Date=Mnf_Date,
        Scheme=Scheme,Scheme_Amount=Scheme_Amount,App_Aadhar_Id=App_Aadhar_Id,Chassis=Chassis,Engine=Engine,
        Rc_Id=Rc_Id,image=image,Payment_Card=Payment_Card,Name_Card=Name_Card,Paid_Amount=Paid_Amount)
        
        app.save()
        print("Saved====================================")
        return redirect('Home')
    else:
        username = request.session['username']
        return render(request,'User/General_Vehicle.html',{'username':username})


@login_required(login_url='/Login')
def Appliances(request):
    if request.method == "POST":
        Category = "Appliances"
        App_Name = request.POST['Name']
        App_DOB = request.POST['Dob']
        App_Gender = request.POST['Gender']
        App_Mobile = request.POST['Mobile']
        App_Aadhar = request.POST['Aadhar']
        App_Email = request.POST['Email']
        Addr1 = request.POST['Ad1']
        Addr2 = request.POST['Ad2']
        Addr3 = request.POST['Ad3']
        Pin = request.POST['Pin']
        Scheme = request.POST['plan']
        Scheme_Amount = request.POST['paid']
        App_Aadhar_Id = request.FILES['Ap_Aadhr_Id']
        Addr_Id = request.FILES['Address_Id']
        Payment_Card = request.POST['cardno']
        Name_Card = request.POST['namecard']
        Paid_Amount = request.POST['paid']

        #Auto Id Generation
   
        myDate = datetime.now() 
        D = myDate.strftime("%d")  
        M = myDate.strftime("%m")  
        Y = myDate.strftime("%Y")  
        X = "APGA" + Y + M + D  

        #result = table.objects.filter(string__contains='pattern')
        count = Appliances_Applications.objects.filter(Appl_Id__contains=X).count()  #Get total number of records

        
        if count == 0:
            n = "01"
            X = X + str(n)
        else:
            n = count + 1
            if len(str(n)) == 1:
                n = "0" + str(n)
            X = X + n
            print (X)

        app = Appliances_Applications(Appl_Id=X,Category=Category,App_Name=App_Name,App_DOB=App_DOB,
        App_Gender=App_Gender,App_Mobile=App_Mobile,App_Aadhar=App_Aadhar,App_Email=App_Email,Addr1=Addr1,
        Addr2=Addr2,Addr3=Addr3,Pin=Pin,Scheme=Scheme,Scheme_Amount=Scheme_Amount,App_Aadhar_Id=App_Aadhar_Id,
        Addr_Id=Addr_Id,Payment_Card=Payment_Card,Name_Card=Name_Card,Paid_Amount=Paid_Amount)
        
        app.save()
        print("Saved====================================")
        return redirect('Home')
    else:
        username = request.session['username']
        return render(request,'User/GeneralInsurance.html',{'username':username})


@login_required(login_url='/Login')
def Download(request):
    if request.method == "GET":
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
                


@login_required(login_url='/Login')
def Mypolicy(request):
    username = request.session['username']
    user = User.objects.get(username=username)
    health_app = Health_Applications.objects.filter(App_Email=username)
    child_app = Life_Childrens_Applications.objects.filter(App_Email=username)
    emp_app = Life_Employees_Applications.objects.filter(App_Email=username)
    veh_app = Vehicle_Applications.objects.filter(App_Email=username)
    app_app = Appliances_Applications.objects.filter(App_Email=username)
    try:
        applicant = Applicants.objects.filter(Email=username)
    except:
        applicant = None
    
    health = []
    child = []
    emp = []
    app = []
    veh = []
    if applicant is not None:
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

    return render(request,'User/Mypolicy.html',{'username':username,'user':user,'app':app,
    'health':health,'child':child,'emp':emp,'health_app':health_app,'child_app':child_app,
    'emp_app':emp_app,'veh_app':veh_app,'app_app':app_app,'veh':veh})


@login_required(login_url='/Login')
def Passwordupdate(request):
    if request.method == "POST":
        username = request.session['username']
        current = request.POST['oldpsw']
        New = request.POST['psw']

        try:
            user = auth.authenticate(username=username,password=current)
           
        except:
            
            user = None
        
        if user is not None :
            user.set_password(New)
            user.save()
            return redirect('/')
        else:
            messages.success(request,'Current Password Entered Incorrect!')
            return render(request, 'User/Passwordchange.html',{'username':username})
        
    else:
        username = request.session['username']
        return render(request, 'User/Passwordchange.html',{'username':username})



@login_required(login_url='/Login')
def Payment(request):
    if 'pay' in request.POST:

        Amount = request.POST['paid']
        Ins = request.POST['insurance']

        x = Ins.split("#")

        if x[0] == "Health":
            ins = Health_Insurance.objects.get(Insurance_Id=x[1])
            account = Account.objects.get(Auth_Id=ins.Auth_Id)
        elif x[0] == "Children's":
            ins = Life_Childrens_Insurance.objects.get(Insurance_Id=x[1])
            account = Account.objects.get(Auth_Id=ins.Auth_Id)
        elif x[0] == "Employees":
            ins = Life_Employees_Insurance.objects.get(Insurance_Id=x[1])
            account = Account.objects.get(Auth_Id=ins.Auth_Id)
        elif x[0] == "Appliances":
            ins = Appliances_Insurance.objects.get(Insurance_Id=x[1])
            account = Account.objects.get(Auth_Id=ins.Auth_Id)
        elif x[0] == "Vehicle":
            ins = Vehicle_Insurance.objects.get(Insurance_Id=x[1])
            account = Account.objects.get(Auth_Id=ins.Auth_Id)

        prev_amount = account.Balance_Amount
        Total = int(prev_amount) + int(Amount)
        account.Balance_Amount = Total
        account.last_Paid = datetime.now().date()
        account.save()

        return redirect('Payment')
    elif 'search' in request.POST:
        policy = request.POST['policy']
        
        x = policy.split("#")
        
        if x[0] == "Health":
            ins = Health_Insurance.objects.get(Insurance_Id=x[1])
            account = Account.objects.get(Auth_Id=ins.Auth_Id)
        elif x[0] == "Children's":
            ins = Life_Childrens_Insurance.objects.get(Insurance_Id=x[1])
            account = Account.objects.get(Auth_Id=ins.Auth_Id)
        elif x[0] == "Employees":
            ins = Life_Employees_Insurance.objects.get(Insurance_Id=x[1])
            account = Account.objects.get(Auth_Id=ins.Auth_Id)
        elif x[0] == "Appliances":
            ins = Appliances_Insurance.objects.get(Insurance_Id=x[1])
            account = Account.objects.get(Auth_Id=ins.Auth_Id)
        elif x[0] == "Vehicle":
            ins = Vehicle_Insurance.objects.get(Insurance_Id=x[1])
            account = Account.objects.get(Auth_Id=ins.Auth_Id)


        #Perform Calculations
        Amount = ins.Scheme_Amount
        last = account.last_Paid
        X = Calculate(x[0],Amount,last)

        print(X)

        ###Get Data username = request.session['username']
        username = request.session['username']
        try:
            applicant = Applicants.objects.filter(Email=username)
        except:
            applicant = None

        health = []
        child = []
        emp = []
        app = []
        veh = []
        if applicant is not None:
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

        return render(request,'User/Payment.html',{'username':username,'app':app,
        'health':health,'child':child,'emp':emp,'ins':ins,'veh':veh,'amount':X,'account':account})
    else:    
        username = request.session['username']
        try:
            applicant = Applicants.objects.filter(Email=username)
        except:
            applicant = None

        health = []
        child = []
        emp = []
        app = []
        veh = []
        if applicant is not None:
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

        return render(request,'User/Payment.html',{'username':username,'app':app,
        'health':health,'child':child,'emp':emp,'veh':veh})



def Logout(request):
    logout(request)
    return redirect('/')