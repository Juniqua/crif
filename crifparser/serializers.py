from random import choice
from rest_framework import serializers
from crifparser.models import crifForm



CORRECTIONFLAG_CHOICES=[' ','1']

class SnippetSerializer(serializers.Serializer):
    f_i_code = serializers.CharField(required=True)#, read_only=True
    branch_code = serializers.CharField(required=True)#, allow_blank=True, max_length=100
    last_acc_date = serializers.CharField()#required=True, style={'base_template': 'textarea.html'}
    date_of_prod = serializers.CharField()#required=True),style={'base_template': 'textarea.html'}
    code = serializers.IntegerField(required=True)
    corr_flag = serializers.CharField(required=True)#, choices=CORRECTIONFLAG_CHOICES, default='python'
    #contract_columns = serializers.FileField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return crifForm.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.f_i_code = validated_data.get('f_i_code', instance.f_i_code)
        instance.branch_code = validated_data.get('branch_code', instance.branch_code)
        instance.last_acc_date = validated_data.get('last_acc_date', instance.last_acc_date)
        instance.date_of_prod = validated_data.get('date_of_prod', instance.date_of_prod)
        instance.code = validated_data.get('code', instance.code)
        instance.corr_flag = validated_data.get('corr_flag',instance.corr_flag)
        instance.save()
        return instance