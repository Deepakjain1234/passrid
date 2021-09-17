from rest_framework import serializers


class ActivitySerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=9)
    webiste_id = serializers.CharField(max_length=9)
    ip = serializers.IPAddressField(protocol='IPv4')
    city = serializers.CharField(max_length=50)
    state = serializers.CharField(max_length=50)
    country = serializers.CharField(max_length=50)
    date_time = serializers.DateTimeField()
    # these are choices having list of key and display name in tuple
    secure_status = [
        # (key , display_name)
        ('secured', 'Secured'),
        ('unsecured', 'Unsecured'),
    ]
    security_status = serializers.ChoiceField(
        choices=secure_status, default='secured')
    via = [
        ('web', 'Website'),
        ('app', 'Application'),
    ]
    medium = serializers.ChoiceField(choices=via, default='web')
