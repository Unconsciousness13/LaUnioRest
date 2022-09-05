from asyncio.sslproto import _DO_HANDSHAKE
from launio.accounts.models import CustomAccountManager, NewUser
from launio.club.models import Gymnast, Team,Trainer , NotesIndividual , NotesTeam , Contact , Competition
from .serializers import GymnastSerializer,TrainerSerializer, TeamSerializer , NotesIndividualSerializer , NotesTeamSerializer, CompetitionSerializer, ContactSerializer, NewUserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


# Gymnasts
class GymnastList(generics.ListCreateAPIView):
    queryset = Gymnast.objects.all()
    serializer_class = GymnastSerializer
    
    

class GymnastDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gymnast.objects.all()
    serializer_class = GymnastSerializer
    permission_classes = [IsAdminUser]
    
class GymnastAdd(generics.CreateAPIView):
    queryset = Gymnast.objects.all()
    serializer_class = GymnastSerializer
    permission_classes = [IsAdminUser]
    

# Trainers

class TrainerList(generics.ListCreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    
    

class TrainerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

    
class TrainerAdd(generics.CreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    permission_classes = [IsAdminUser]
    
# Teams

class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    
    

class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    
class TeamAdd(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAdminUser]
    
# Notes Individual 

class NotesIndividualList(generics.ListCreateAPIView):
    queryset = NotesIndividual.objects.all()
    serializer_class = NotesIndividualSerializer
    
    

class NotesIndividualDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NotesIndividual.objects.all()
    serializer_class = NotesIndividualSerializer

    
class NotesIndividualAdd(generics.CreateAPIView):
    queryset = NotesIndividual.objects.all()
    serializer_class = NotesIndividualSerializer
    permission_classes = [IsAdminUser]
    
# Notes Team 

class NotesTeamList(generics.ListCreateAPIView):
    queryset = NotesTeam.objects.all()
    serializer_class = NotesTeamSerializer
    
    

class NotesTeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NotesTeam.objects.all()
    serializer_class = NotesTeamSerializer

    
class NotesTeamAdd(generics.CreateAPIView):
    queryset = NotesTeam.objects.all()
    serializer_class = NotesTeamSerializer
    permission_classes = [IsAdminUser]
    
# Competitions 

class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    
    

class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

    
class CompetitionAdd(generics.CreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = [IsAdminUser]
    
    
# Contact

class ContactSend(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAdminUser]
    
# New User
    
class NewUserList(generics.ListCreateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer
    permission_classes = [IsAdminUser]

class NewUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer
    permission_classes = [IsAdminUser]


    
class NewUserAdd(generics.CreateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = NewUserSerializer
    permission_classes = [IsAdminUser]