def get_answer(question):
    try:
        print(answers[question.lower()])
    except (KeyError):
        print("Нет")

answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}

get_answer(input())