from django.urls import path
from . import views

urlpatterns = [
    path('gymnasts/', views.GymnastList.as_view(), name='gymnasts'),
    path('gymnast/<int:pk>/', views.GymnastDetail.as_view(), name='gymnast'),
    path('gymnast/add/', views.GymnastAdd.as_view(), name='gymnast-add'),
    path('trainers/', views.TrainerList.as_view(), name='trainers'),
    path('trainer/<int:pk>/', views.TrainerDetail.as_view(), name='trainer'),
    path('trainer/add/', views.TrainerAdd.as_view(), name='trainer-add'),
    path('teams/', views.TeamList.as_view(), name='teams'),
    path('team/<int:pk>/', views.TeamDetail.as_view(), name='team'),
    path('team/add/', views.TeamAdd.as_view(), name='team-add'),
    path('notesindividual/', views.NotesIndividualList.as_view(), name='notes-individual'),
    path('notesindividual/<int:pk>/', views.NotesIndividualDetail.as_view(), name='notes-individual-single'),
    path('notesindividual/add/', views.NotesIndividualAdd.as_view(), name='notes-individual-add'),
    path('notesteam/', views.NotesTeamList.as_view(), name='notes-team'),
    path('notesteam/<int:pk>/', views.NotesTeamDetail.as_view(), name='notes-team-single'),
    path('notesteam/add/', views.NotesTeamAdd.as_view(), name='notes-team-add'),
    path('competition/', views.CompetitionList.as_view(), name='competitions'),
    path('competition/<int:pk>/', views.CompetitionDetail.as_view(), name='competition-single'),
    path('competition/add/', views.CompetitionAdd.as_view(), name='competition-add'),
    path('competition/', views.CompetitionList.as_view(), name='competitions'),
    path('competition/<int:pk>/', views.CompetitionDetail.as_view(), name='competition-single'),
    path('competition/add/', views.CompetitionAdd.as_view(), name='competition-add'),
    path('contact/send/', views.ContactSend.as_view(), name='contact-send'),
        
]   

