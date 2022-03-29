from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Question, GameSession
from accounts.models import Profile
from .utils import generate_questions_list, string_to_list
import random


@login_required
def start_game_view(request):
    user = request.user
    question = None
    try:
        session = GameSession.objects.get(user_id=user.id)
        # print(session)
    except:
        session = GameSession.objects.create(user_id=user.id)
        session.save()
        # print(session)
    if session.game_finished:
        session.questions_list = generate_questions_list()
        session.last_answered_question = 0
        session.jokers_used = 0
        session.game_finished = False
        session.save()
        return redirect('start-game')
    if not session.game_finished:
        questions = string_to_list(session.questions_list)
        question_id = questions[int(session.last_answered_question)]
        question = Question.objects.get(id=question_id)
        answers = [question.correct_answer, question.answer_2, question.answer_3, question.answer_4]
        random.shuffle(answers)
        # print(answers)
    context = {
        'session': session,
        'question': question,
        'answers': answers,
        'last_question': session.last_answered_question
        }
    return render(request, 'game/start_game.html', context)


@login_required
def check_answer_view(request, answer):
    user = request.user
    user_profile = get_object_or_404(Profile, user_id=user.id)
    session = GameSession.objects.get(user_id=user.id)
    questions = string_to_list(session.questions_list)
    question_id = questions[int(session.last_answered_question)]
    question = Question.objects.get(id=question_id)
    if answer == question.correct_answer:
        user_profile.total_score += session.last_answered_question * 10 + 10
        user_profile.save()
        if session.last_answered_question <= 14:
            session.last_answered_question += 1
            session.save()
        if session.last_answered_question == 15:
            session.game_finished = True
            user_profile.games_played += 1
            user_profile.total_score += 1000
            session.save()
            user_profile.save()
            return redirect('end-game')
        print(question.correct_answer)
    else:
        session.game_finished = True
        user_profile.games_played += 1
        session.save()
        user_profile.save()
        print('incorrect_answer')
        return redirect('end-game')
    return redirect('start-game')


@login_required
def end_game_view(request):
    user = request.user
    session = GameSession.objects.get(user_id=user.id)
    context = {'last_question': session.last_answered_question}
    return render(request, 'game/end_game.html', context)
