from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from diabetes.models import *
from perdiction import random_forest, mysvm, decisiontree


def main(request):
    return render(request,"loginindex.html")

def logincode(request):
    uname=request.POST['textfield']
    pw=request.POST['textfield2']
    try:
        ob=login.objects.get(username=uname,password=pw)
        if ob.type == 'admin':
            return HttpResponse('''<script>alert("welcome to admin home");window.location='/adminhome'</script>''')
        elif ob.type == 'expert':
            request.session['lid']=ob.id
            return HttpResponse('''<script>alert("welcome to expert home");window.location='/experthome'</script>''')
        elif ob.type == 'user':
            request.session['lid'] = ob.id
            return HttpResponse('''<script>alert("welcome to user home");window.location='/userhome'</script>''')
        else:
            return HttpResponse('''<script>alert("incorrect password or username");window.location='/'</script>''')
    except:
        return HttpResponse('''<script>alert("incorrect password or username");window.location='/'</script>''')


def addexpert(request):
    return render(request,"admin/Add Expert.html")

def expertadd(request):
    fname = request.POST['textfield']
    lname = request.POST['textfield2']
    place = request.POST['textfield3']
    post = request.POST['textfield4']
    pin = request.POST['textfield5']
    phone = request.POST['textfield6']
    email = request.POST['textfield7']
    qualification = request.POST['textfield8']
    uname = request.POST['textfield9']
    pw = request.POST['textfield10']
    ob = login()
    ob.username = uname
    ob.password = pw
    ob.type = 'expert'
    ob.save()

    iob = expert()
    iob.fname = fname
    iob.lname = lname
    iob.place = place
    iob.post = post
    iob.pin = pin
    iob.phone = phone
    iob.email = email
    iob.qualification = qualification
    iob.lid = ob
    iob.save()
    return HttpResponse('''<script>alert("added");window.location='/manageexpert'</script>''')



def deleteexpert(request,id):
    ob=expert.objects.get(lid__id=id)
    ob.delete()
    iob=login.objects.get(id=id)
    iob.delete()
    return HttpResponse('''<script>alert("deleted");window.location='/manageexpert'</script>''')


def editexpert(request,id):
    ob=expert.objects.get(id=id)
    request.session['eid']=id
    return render(request,"admin/edit Expert.html",{'val':ob})

def expertedit(request):
    fname = request.POST['textfield']
    lname = request.POST['textfield2']
    place = request.POST['textfield3']
    post = request.POST['textfield4']
    pin = request.POST['textfield5']
    phone = request.POST['textfield6']
    email = request.POST['textfield7']
    qualification = request.POST['textfield8']

    iob = expert.objects.get(id=request.session['eid'])
    iob.fname = fname
    iob.lname = lname
    iob.place = place
    iob.post = post
    iob.pin = pin
    iob.phone = phone
    iob.email = email
    iob.qualification = qualification
    iob.save()
    return HttpResponse('''<script>alert("updated");window.location='/manageexpert'</script>''')


def addnotification(request):
    return render(request,"admin/Add Notification.html")

def notificationadd(request):
    notifications = request.POST['textarea']

    iob = notification()
    iob.notification = notifications
    iob.date=datetime.today()
    iob.save()
    return HttpResponse('''<script>alert("updated");window.location='/adminhome'</script>''')

def deletenotification(request,id):
    ob=notification.objects.get(id=id)
    ob.delete()

    return HttpResponse('''<script>alert("deleted");window.location='/managenotification'</script>''')

def editnotification(request,id):
    ob=notification.objects.get(id=id)
    request.session['nid'] = id
    return render(request, "admin/Edit Notification.html", {'val': ob})


def notificationedit(request):
    notifications = request.POST['textarea']

    iob = notification.objects.get(id=request.session['nid'])
    iob.notification = notifications

    iob.save()
    return HttpResponse('''<script>alert("updated");window.location='/managenotification'</script>''')



def adminhome(request):
    return render(request,"admin/Admin Home.html")

def blockusers(request):
    ob=user.objects.all()
    return render(request,"admin/Block Users.html",{'val':ob})

def manageexpert(request):
    ob=expert.objects.all()
    return render(request,"admin/Manage Expert.html",{'val':ob})

def managenotification(request):
    ob=notification.objects.all()
    return render(request,"admin/Manage Notification.html",{'val':ob})

def sendcomplaintreply(request,id):

    request.session['cid']=id
    return render(request,"admin/Send Complaint Reply.html")

def reply_comp(request):
    replys=request.POST['textarea']
    ob=complaint.objects.get(id=request.session['cid'])
    ob.reply=replys
    ob.save()
    return HttpResponse('''<script>alert("replied");window.location='/viewcomplaint'</script>''')



def viewcomplaint(request):
    ob=complaint.objects.all()
    return render(request,"admin/View Complaint.html",{'val':ob})

def addtips(request):
    return render(request,"expert/Add Tips.html")

def tipsadd(request):
    tipss = request.POST['textarea']


    iob = tips()
    iob.tips = tipss
    iob.date=datetime.today()
    iob.eid=expert.objects.get(lid__id=request.session['lid'])
    iob.save()
    return HttpResponse('''<script>alert("added");window.location='/managetips'</script>''')





def experthome(request):
    return render(request,"expert/Expert Home.html")

def managetips(request):
    ob=tips.objects.all()
    return render(request,"expert/Manage Tips.html",{'val':ob})

def edittips(request,id):
    ob=tips.objects.get(id=id)
    request.session['tid'] = id
    return render(request, "expert/Edit Tips.html", {'val': ob})


def tipsedit(request):
    tipss = request.POST['textarea']

    iob = tips.objects.get(id=request.session['tid'])
    iob.tips = tipss

    iob.save()
    return HttpResponse('''<script>alert("updated");window.location='/managetips'</script>''')

def deletetips(request,id):
    ob=tips.objects.get(id=id)
    ob.delete()

    return HttpResponse('''<script>alert("deleted");window.location='/managetips'</script>''')

def senddoubtreply(request,id):
    request.session['doubtid']=id
    return render(request,"expert/Send Doubt Reply.html")

def doubtreply(request):
    dreplys=request.POST['textarea']
    ob=doubt.objects.get(id=request.session['doubtid'])
    ob.reply=dreplys
    ob.save()
    return HttpResponse('''<script>alert("replied");window.location='/viewdoubt'</script>''')

def viewdoubt(request):
    ob=doubt.objects.all()
    return render(request,"expert/View Doubt.html",{'val':ob})

def viewnotificationexpert(request):
    ob=notification.objects.all()
    return render(request,"expert/View Notification Expert.html",{'val':ob})

def askdoubt(request):
    ob=expert.objects.all()
    return render(request,"user/Ask Doubt.html",{'val':ob})

def doubtask(request):
    doubts = request.POST['textarea']
    expert1=request.POST['select']
    iob = doubt()
    iob.doubt = doubts
    iob.date = datetime.today()
    iob.eid = expert.objects.get(id=expert1)
    iob.uid = user.objects.get(lid__id=request.session['lid'])
    iob.reply = 'pending'
    iob.save()
    return HttpResponse('''<script>alert("Added");window.location='/userhome'</script>''')

def registeruser(request):
    return render(request,"registerindex.html")

def userregister(request):
    fname = request.POST['textfield']
    lname = request.POST['textfield2']
    place = request.POST['textfield3']
    post = request.POST['textfield4']
    pin = request.POST['textfield5']
    phone = request.POST['textfield6']
    email = request.POST['textfield7']
    uname = request.POST['textfield9']
    pw = request.POST['textfield10']
    ob = login()
    ob.username = uname
    ob.password = pw
    ob.type = 'user'
    ob.save()

    iob = user()
    iob.fname = fname
    iob.lname = lname
    iob.place = place
    iob.post = post
    iob.pin = pin
    iob.phone = phone
    iob.email = email
    iob.lid = ob
    iob.save()
    return HttpResponse('''<script>alert("added");window.location='/'</script>''')

def sendcomplaint(request):
    return render(request,"user/Send Complaint.html")

def complaintsend(request):
    complaints = request.POST['textarea']
    iob = complaint()
    iob.complaint = complaints
    iob.date=datetime.today()
    iob.uid=user.objects.get(lid__id=request.session['lid'])
    iob.reply='pending'
    iob.save()
    return HttpResponse('''<script>alert("Added");window.location='/userhome'</script>''')



def userhome(request):
    return render(request,"user/User Home.html")

def viewcomplaintreply(request):
    ob=complaint.objects.all()
    return render(request,"user/View Complaint Reply.html",{'val':ob})

def viewdoubtreply(request):
    ob=doubt.objects.all()
    return render(request,"user/View Doubt Reply.html",{'val':ob})

def viewnotificationuser(request):
    ob=notification.objects.all()
    return render(request,"user/View Notification User.html",{'val':ob})

def viewtips(request):

    ob=tips.objects.all()
    return render(request,"user/View Tips.html",{'val':ob})

def logout(request):
    return render(request,"Login.html")





def prediction(request):
    return render(request,"user/Prediction.html")

def predictionadd(request):
    pregnancies = request.POST['textfield']
    glucose = request.POST['textfield2']
    bloodpressure = request.POST['textfield3']
    skinthickness = request.POST['textfield4']
    insulin = request.POST['textfield5']
    bmi = request.POST['textfield6']
    diabetespedigreefunction = request.POST['textfield7']
    age = request.POST['textfield8']
    rd1,rd2 = random_forest(pregnancies,glucose,bloodpressure,skinthickness,insulin,bmi,diabetespedigreefunction,age)
    sv1,sv = mysvm(pregnancies,glucose,bloodpressure,skinthickness,insulin,bmi,diabetespedigreefunction,age)
    dc1,dc = decisiontree(pregnancies,glucose,bloodpressure,skinthickness,insulin,bmi,diabetespedigreefunction,age)

    print(rd1,"eeeeeeeeee")


    return render(request,"user/Prediction.html",{'rd':str(rd1),'sv':str(sv1),'dc':str(dc1),'rds':str(rd2),'sv2':sv,'dc2':dc})











