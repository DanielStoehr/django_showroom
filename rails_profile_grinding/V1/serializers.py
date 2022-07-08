from rest_framework import serializers

from ..models import Specification


class TemplateSerializer(serializers.Serializer):
    timestamp = serializers.DateTimeField()
    main_program = serializers.CharField()
    p003 = serializers.FloatField()
    p004 = serializers.FloatField()
    # p006 = serializers.FloatField()
    main_program_file = serializers.CharField()
    process_time_in_minutes = serializers.FloatField()


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = "__all__"
