from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.home, name="home"),
	path('register/', views.register,name='register'),
	path('registerasexpert/', views.registerasexpert,name='registerasexpert'),
	path('user_login/', views.user_login,name='user_login'),
	path('logout/', views.user_logout,name='logout'),
	path('diabetes_risk/', views.diabetes_risk,name='diabetes_risk'),
	path('diabetes_risk_result/', views.diabetes_risk_result,name='diabetes_risk_result'),
	path('cvd_prediction/', views.cvd_prediction,name='cvd_prediction'),
	path('cvd_prediction_result/', views.cvd_prediction_result,name='cvd_prediction_result'),
	path('detect_brain_tumor/', views.detect_brain_tumor,name='detect_brain_tumor'),
	path('detect_brain_tumor_result/', views.detect_brain_tumor_result,name='detect_brain_tumor_result'),
	path('liver_diagnosis/', views.liver_diagnosis,name='liver_diagnosis'),
	path('liver_diagnosis_result/', views.liver_diagnosis_result,name='liver_diagnosis_result'),
	path('diagnosistools/', views.diagnosistools,name='diagnosistools'),
	path('healthcheckup/', views.symptomsdiagnosis,name='healthcheckup'),
	path('healthcheckup_result/', views.symptomsdiagnosis_result,name='healthcheckup_result'),
	path('article/', views.article,name='article'),
	path('<int:id>/read_article/', views.read_article, name="read_article"),
	path('mentalhealth/', views.mentalhealth,name='mentalhealth'),
	path('mentalhealth_results/', views.mentalhealth_results,name='mentalhealth_results'),
	path('diet_plan/', views.diet_plan,name='diet_plan'),
	path('diet_plan_result/', views.diet_plan_result,name='diet_plan_result'),
	path('search/', views.search,name='search'),
	path('about/', views.about,name='about'),
	path('accounts/', views.accounts,name='accounts'),
	path('rating/', views.rating,name='rating'),
	path('report/', views.report,name='report'),
	path('healthcareexperts/', views.healthcareexperts,name='healthcareexperts'),
	path('<int:id>/appointment/', views.appointment, name="appointment"),
	path('create_medical_profile/', views.create_medical_profile,name='create_medical_profile'),
	path('<int:id>/update_medical_profile/', views.update_medical_profile,name='update_medical_profile'),
	path('404/',views.page_not_found),
	path('reset_password/', auth_views.PasswordResetView.as_view(template_name='MAINAPP/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='MAINAPP/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='MAINAPP/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='MAINAPP/password_reset_complete.html'), name='password_reset_complete'),

    ]
