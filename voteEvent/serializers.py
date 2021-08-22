from voteEvent.models import Choice, VoteEvent, Question
from rest_framework import serializers

class ChoiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'votes']
        depth = 1

class QuestionSerializer(serializers.ModelSerializer):
    
    choices = ChoiceSerializer(source = 'choice_set', many = True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'choices']
        depth = 2

class VoteEventSerializer(serializers.ModelSerializer):
    
    questions = QuestionSerializer(source = 'question_set', many = True)

    class Meta:
        model = VoteEvent
        fields = ['id', 'title', 'content', 'created', 'questions']

    def create(self, validated_data):
        questions_data = validated_data.pop('question_set')
        print(questions_data)
        voteEvent = VoteEvent.objects.create(**validated_data)
        for question_data in questions_data:
            choices_data = question_data.pop('choice_set')
            question = Question.objects.create(voteEvent = voteEvent, **question_data)
            for choice_data in choices_data:
                Choice.objects.create(question = question, **choice_data)
        return voteEvent


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()

        questions_data = validated_data.get('question_set')

        for question_data in questions_data:
            title = question_data.get('title')
            try:
                question = Question.objects.get(title = title, voteEvent = instance)
            except Question.DoesNotExist:
                continue
            choices_data = question_data.get('choice_set')
            for choice_data in choices_data:
                choice_text = choice_data.get('choice_text')
                try:
                    inv_choice = Choice.objects.get(choice_text = choice_text, question = question)
                except Choice.DoesNotExist:
                    continue
                inv_choice.votes += choice_data.get('votes', inv_choice.votes)
                inv_choice.save()
        return instance

