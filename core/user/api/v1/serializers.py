from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs.get("old_password") == attrs.get("new_password"):
            raise serializers.ValidationError({"detail":"The new password must be different from the previous one"})
        if attrs.get("new_password") != attrs.get("new_password1"):
            raise serializers.ValidationError({"detail":"passwords aren't same"})
        
        try:
            validate_password(password=attrs.get("new_password"))
            
        except ValidationError as messages:
            raise serializers.ValidationError({"password":list(messages.messages)})
        return super().validate(attrs)