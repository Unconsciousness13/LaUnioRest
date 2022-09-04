from rest_framework import serializers
from launio.club.models import Gymnast, Team, Trainer , Competition , NotesIndividual , NotesTeam, Contact

class GymnastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gymnast
        fields = '__all__'
        
class TeamSerializer(serializers.ModelSerializer):
    class MEta:
        model = Team
        fields = '__all__'