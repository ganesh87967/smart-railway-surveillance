from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
               path("UserLogin.html", views.UserLogin, name="UserLogin"),	      
               path("UserLoginAction", views.UserLoginAction, name="UserLoginAction"),
	       path("AdminLogin.html", views.AdminLogin, name="AdminLogin"),	      
               path("AdminLoginAction", views.AdminLoginAction, name="AdminLoginAction"),
               path("AddEmp.html", views.AddEmp, name="AddEmp"),
               path("AddEmpAction", views.AddEmpAction, name="AddEmpAction"),
               path("LoadDataset", views.LoadDataset, name="LoadDataset"),
	       path("LoadDatasetAction", views.LoadDatasetAction, name="LoadDatasetAction"),
	       path("ExtractFeatures", views.ExtractFeatures, name="ExtractFeatures"),
	       path("TrainModels", views.TrainModels, name="TrainModels"),
	       path("MonitorVideo.html", views.MonitorVideo, name="MonitorVideo"),
               path("MonitorVideoAction", views.MonitorVideoAction, name="MonitorVideoAction"),	
	       path("ViewAlerts", views.ViewAlerts, name="ViewAlerts"),
              
]
