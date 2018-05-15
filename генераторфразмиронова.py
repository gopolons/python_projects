from random import randint

ver = str(1.2)
#def lists of words
happy = ["а", "у", "нас", "всё", "хорошо", "поздравляю", "всех", "с", "Новым", "Годом", "сегодня", "всем", "всего", "наилучшего", "в", "Москве", "много", "плюсов", "а", "минусам", "надо", "привыкнуть"]
philosophy = ["свобода", "совокупность", "возможностей", "определяемая", "для", "всех", "природой", "и", "определённая", "для", "себя", "живым", "существом", "дыхание", "учителей", "дыхание", "победителей", "дыхание", "их", "учеников", "дыхание", "будущих", "победителей", "причём", "больших", "чем", "сами", "учителя", "кто", "то", "ещё", "смеет", "судить", "о", "жизни", "России", "для", "чего", "он", "это", "делает", "чтобы", "не", "находились", "те", "чернила", "у", "России", "которые", "опишут", "как", "сделать", "Россию", "лучше", "и", "в", "чем", "она", "уже", "хороша"]
patriotic = ["была", "бы", "Россия", "такой", "уж", "нищей", "не", "было", "бы", "у", "неё", "чернил", "для", "тех", "писателей", "которые", "пишут", "о", "ней", "как", "о", "нищей", "если", "у", "России", "ни", "гроша", "в", "кармане", "её", "бюджета", "то", "тогда", "на", "чьи", "гроши", "и", "на", "чьи", "чернила", "пишутся", "плохие", "отзывы", "или", "же", "кто", "то", "продаёт", "свои", "чернила", "России", "только", "потому", "что", "им", "этими", "же", "чернилами", "о", "своей", "стране", "той", "другой", "стране", "отличной", "от", "России", "в", "которой", "они", "так", "гордо", "поселились", "писать", "то", "нечего", "разве", "что", "только", "о", "бесконечных", "преступлениях", "своей", "страны"]
science = ["между", "прочим", "один", "из", "корней", "уравнения", "посчитан", "правильно", "несмотря", "на", "убогое", "решение", "но", "наша", "кровь", "тоже", "содержит", "железо", "в", "таком", "случае", "получается", "мы", "ржавые", "изнутри", "но", "живём", "благодаря", "этому", "мудрость", "приходит", "без", "ума", "но", "остаётся", "с", "умом"]

choices = ["Жизнерадостные", "Философия", "Патриотизм", "Наука"]

print()
print("Генератор фраз Миронова. Версия " + ver) 
print()

def again():
    print()
    restart = input("Желаете ли вы продолжить? ").lower()
    print()
    if restart == "да" or restart == " да" or restart == "да ":
        prog()
    elif restart == "нет" or restart == " нет" or restart == "нет ":
        print("Да пребудет с вами мудрость Миронова!")
    else:
        print("Такого ответа не существует.")
        again()

def prog():

    print("На какую тематику вы бы хотели цитату? Доступные варианты: жизнерадостные, философия, патриотизм, наука.")
    print()

    quote = []

    user_answer = input().lower()

    if user_answer == "жизнерадостные" or user_answer == " жизнерадостные" or user_answer == "жизнерадостные ":
        print()
        print("""Григорий Миронов не только великий философ, но еще и потрясающий поэт!
Популярность его цитат касательно счастья в повседневной жизни не стихает ни на минуту!
Его цитаты печатают такие популярные издания как New York Times, Bibirevo Today и множество других!""")
        print()
        length_choice = input("Пожалуйста, выбирите подходящую длинну цитаты: короткая, средняя, длинная: ").lower()
        if length_choice == "короткая" or length_choice == " короткая" or length_choice == "короткая ":
            for x in range(6):
                new_word = happy[randint(0, (len(happy) - 1))]
                happy.remove(new_word)
                quote.append(new_word)
            print()
            final_quote = (" ".join(quote))
            print(final_quote.capitalize() + ".")
            again()
        elif length_choice == "средняя" or length_choice == " средняя" or length_choice == "средняя ":
            for x in range(12):
                new_word = happy[randint(0, (len(happy) - 1))]
                happy.remove(new_word)
                quote.append(new_word)
            print()
            final_quote = (" ".join(quote))
            print(final_quote.capitalize() + ".")
            again()
        elif length_choice == "длинная" or length_choice == " длинная" or length_choice == "длинная ":
            for x in range(18):
                new_word = happy[randint(0, (len(happy) - 1))]
                happy.remove(new_word)
                quote.append(new_word)
            print()
            final_quote = (" ".join(quote))
            print(final_quote.capitalize() + ".")
            again()
        else:
            print("Извините, такого варианта не существует.")
            print()
            prog()



    elif user_answer == "философия" or user_answer == " философия" or user_answer == "философия ":
        print()
        print("""Философские цитаты Григория Миронова уже не один год будоражат умы передовых представителей философской мысли.
Его потрясающая умение находит позиции касательно любого вопроса (даже в тех, в которых он не разбирается), 
всегда находит отклик в душах его почитателей. Вы определенно сделали правильный выбор!""")
        print()
        length_choice = input("Пожалуйста, выбирите подходящую длинну цитаты: короткая, средняя, длинная: ").lower()
        if length_choice == "короткая" or length_choice == " короткая" or length_choice == "короткая ":
            for x in range(6):
                new_word = philosophy[randint(0, (len(philosophy) - 1))]
                philosophy.remove(new_word)
                quote.append(new_word)
            print()
            final_quote = (" ".join(quote))
            print(final_quote.capitalize() + ".")
            again()
        elif length_choice == "средняя" or length_choice == " средняя" or length_choice == "средняя ":
            for x in range(12):
                new_word = philosophy[randint(0, (len(philosophy) - 1))]
                philosophy.remove(new_word)
                quote.append(new_word)
            print()
            final_quote = (" ".join(quote))
            print(final_quote.capitalize() + ".")
            again()
        elif length_choice == "длинная" or length_choice == " длинная" or length_choice == "длинная ":
            for x in range(18):
                new_word = philosophy[randint(0, (len(philosophy) - 1))]
                philosophy.remove(new_word)
                quote.append(new_word)
            print()
            final_quote = (" ".join(quote))
            print(final_quote.capitalize() + ".")
            again()
        else:
            print("Извините, такого варианта не существует.")
            print()
            prog()

    elif user_answer == "патриотизм" or user_answer == " патриотизм" or user_answer == "патриотизм ":
        print()
        print("""Патриотические изыскания Григория Миронова уже не один год впечатляют своей глубиной людей искренне любящих свою страну.
Его поэзия и проза насквозь пропитаны любовью к своей отчизне. 
Этот выбор определенно является хорошей точкой для старта своего дня для любителей Григория любого уровня.""")
        print()
        length_choice = input("Пожалуйста, выбирите подходящую длинну цитаты: короткая, средняя, длинная: ").lower()
        if length_choice == "короткая" or length_choice == " короткая" or length_choice == "короткая ":
            for x in range(6):
                new_word = patriotic[randint(0, (len(patriotic) - 1))]
                patriotic.remove(new_word)
                quote.append(new_word)
            print()
            final_quote = (" ".join(quote))
            print(final_quote.capitalize() + ".")
            again()
        elif length_choice == "средняя" or length_choice == " средняя" or length_choice == "средняя ":
            for x in range(12):
                new_word = patriotic[randint(0, (len(patriotic) - 1))]
                patriotic.remove(new_word)
                quote.append(new_word)
            print()
            final_quote = (" ".join(quote))
            print(final_quote.capitalize() + ".")
            again()
        elif length_choice == "длинная" or length_choice == " длинная" or length_choice == "длинная ":
            for x in range(18):
                new_word = patriotic[randint(0, (len(patriotic) - 1))]
                patriotic.remove(new_word)
                quote.append(new_word)
            print()
            final_quote = (" ".join(quote))
            print(final_quote.capitalize() + ".")
            again()
        else:
            print("Извините, такого варианта не существует.")
            print()
            prog()

    elif user_answer == "наука" or user_answer == " наука" or user_answer == "наука ":
        print()
        print("""Научные познания Григория уже не один год потрясают умы ученых из разных областей.
Его умопомрачительные знания в любой научной области удивят любого, и даже Вас!""")
        print()
        length_choice = input("Пожалуйста, выбирите подходящую длинну цитаты: короткая, средняя, длинная: ").lower()
        if length_choice == "короткая" or length_choice == " короткая" or length_choice == "короткая ":
            for x in range(6):
                new_word = science[randint(0, (len(science) - 1))]
                science.remove(new_word)
                quote.append(new_word)
            print()
            final_quote = (" ".join(quote))
            print(final_quote.capitalize() + ".")
            again()
        elif length_choice == "средняя" or length_choice == " средняя" or length_choice == "средняя ":
            for x in range(12):
                new_word = science[randint(0, (len(science) - 1))]
                science.remove(new_word)
                quote.append(new_word)
            print()
            final_quote = (" ".join(quote))
            print(final_quote.capitalize() + ".")
            again()
        elif length_choice == "длинная" or length_choice == " длинная" or length_choice == "длинная ":
            for x in range(18):
                new_word = science[randint(0, (len(science) - 1))]
                science.remove(new_word)
                quote.append(new_word)
            print()
            final_quote = (" ".join(quote))
            print(final_quote.capitalize() + ".")
            again()
        else:
            print("Извините, такого варианта не существует.")
            print()
            prog()

    else:
        print()
        print("Извините, такого варианта не существует.")
        print()
        prog()

prog()