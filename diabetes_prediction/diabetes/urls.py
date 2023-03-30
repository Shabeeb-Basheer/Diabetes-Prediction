from django.urls import path

from diabetes import views

urlpatterns=[
    path('',views.main,name="main"),
    path('logincode',views.logincode,name="logincode"),
    path('addexpert',views.addexpert,name="addexpert"),
    path('addnotification',views.addnotification,name="addnotification"),
    path('adminhome',views.adminhome,name="adminhome"),
    path('expertedit',views.expertedit,name="expertedit"),
    path('blockusers',views.blockusers,name="blockusers"),
    path('manageexpert',views.manageexpert,name="manageexpert"),
    path('managenotification',views.managenotification,name="managenotification"),
    path('sendcomplaintreply/<int:id>',views.sendcomplaintreply,name="sendcomplaintreply"),
    path('editnotification/<int:id>',views.editnotification,name="editnotification"),
    path('edittips/<int:id>',views.edittips,name="edittips"),
    path('notificationedit',views.notificationedit,name="notificationedit"),
    path('tipsedit',views.tipsedit,name="tipsedit"),
    path('editexpert/<int:id>',views.editexpert,name="editexpert"),
    path('viewcomplaint',views.viewcomplaint,name="viewcomplaint"),
    path('deleteexpert/<int:id>',views.deleteexpert,name="deleteexpert"),
    path('deletenotification/<int:id>',views.deletenotification,name="deletenotification"),
    path('deletetips/<int:id>',views.deletetips,name="deletetips"),
    path('reply_comp',views.reply_comp,name="reply_comp"),
    path('doubtreply',views.doubtreply,name="doubtreply"),
    path('addtips',views.addtips,name="addtips"),
    path('complaintsend',views.complaintsend,name="complaintsend"),
    path('doubtask',views.doubtask,name="doubtask"),
    path('experthome',views.experthome,name="experthome"),
    path('managetips',views.managetips,name="managetips"),
    path('senddoubtreply/<int:id>',views.senddoubtreply,name="senddoubtreply"),
    path('viewdoubt',views.viewdoubt,name="viewdoubt"),
    path('viewnotificationexpert',views.viewnotificationexpert,name="viewnotificationexpert"),
    path('askdoubt',views.askdoubt,name="askdoubt"),
    path('registeruser',views.registeruser,name="registeruser"),
    path('userregister',views.userregister,name="userregister"),
    path('sendcomplaint',views.sendcomplaint,name="sendcomplaint"),
    path('userhome',views.userhome,name="userhome"),
    path('viewcomplaintreply',views.viewcomplaintreply,name="viewcomplaintreply"),
    path('viewdoubtreply',views.viewdoubtreply,name="viewdoubtreply"),
    path('viewnotificationuser',views.viewnotificationuser,name="viewnotificationuser"),
    path('viewtips',views.viewtips,name="viewtips"),
    path('logout',views.logout,name="logout"),
    path('expertadd',views.expertadd,name="expertadd"),
    path('notificationadd',views.notificationadd,name="notificationadd"),
    path('tipsadd',views.tipsadd,name="tipsadd"),
















]