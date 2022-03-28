from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Question, GameSession
from .utils import generate_questions_list
import random


@login_required
def start_game_view(request):
    user = request.user
    question = None
    try:
        session = GameSession.objects.get(user_id=user.id)
        print(session)
    except:
        session = GameSession.objects.create(user_id=user.id)
        session.save()
        print(session)
    if session.game_finished:
        session.questions_list = generate_questions_list()
        session.last_answered_question = 0
        session.jokers_used = 0
        session.game_finished = False
        session.save()
    if not session.game_finished:
        questions = [int(num) for num in session.questions_list if num.isdigit()]
        question_id = questions[int(session.last_answered_question)]
        question = Question.objects.get(id=question_id)
        answers = [question.correct_answer, question.answer_2, question.answer_3, question.answer_4]
        random.shuffle(answers)
        print(answers)
    context = {'session': session, 'question': question, 'answers': answers}
    return render(request, 'game/start_game.html', context)
