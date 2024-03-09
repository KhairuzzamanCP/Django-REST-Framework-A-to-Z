from rest_framework import serializers
from .models import Student



class StudentSeralizer(serializers.ModelSerializer):
    # Validators
    def start_with_k(value):
        if value[0].lower() != 'k':
            raise serializers.ValidationError('Name Should be start with K')

    name = serializers.CharField(max_length = 100, validators =[start_with_k])
    class Meta:
        model = Student
        fields = ['name','roll','city']
        
    # Field Level Validation
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError("Seat Full")
        return value

    # Object Level Validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'verr' and ct.lower() != 'dhaka':
            raise serializers.ValidationError('city must be Dhaka ')
        return data
   
    