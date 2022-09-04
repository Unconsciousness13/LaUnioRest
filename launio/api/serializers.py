from rest_framework import serializers
from launio.club.models import Gymnast, Team, Trainer , Competition , NotesIndividual , NotesTeam, Contact

class GymnastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gymnast
        fields = '__all__'
        
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        
class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'
        
class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = '__all__'
        
class NotesIndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotesIndividual
        fields = '__all__'

class NotesTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotesTeam
        fields = '__all__'
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'