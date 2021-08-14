from voteEvent.models import Choice, VoteEvent
from rest_framework import serializers

class ChoiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'votes']
        depth = 1

class VoteEventSerializer(serializers.ModelSerializer):
    
    choices = ChoiceSerializer(source = 'choice_set', many = True)

    class Meta:
        model = VoteEvent
        fields = ['id', 'title', 'content', 'created', 'choices']

    def create(self, validated_data):
        choices_data = validated_data.pop('choice_set')
        voteEvent = VoteEvent.objects.create(**validated_data)
        for choice_data in choices_data:
            Choice.objects.create(voteEvent = voteEvent, **choice_data)
        return voteEvent


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()

        choices = validated_data.get('choice_set')

        for choice in choices:
            choice_text = choice.get('choice_text')
            try :
                inv_choice = Choice.objects.get(choice_text = choice_text, voteEvent = instance)
            except Choice.DoesNotExist:
                break
            if inv_choice:
                inv_choice.votes += choice.get('votes', inv_choice.votes)
                inv_choice.save()
        return instance

