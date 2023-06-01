import re

cons = "йцкнгшщзхъфвпрлджчсмтбЙЦКНГШЩЗХЪФВПРЛДЖЧСМТБ"
vows = "уеыаоэяиюУЕЫАОЭЯИЮ"

def find_with_regex(text):
    return re.findall(r"\b\S*[" + vows + r"]{2,}\S*(?=\s(?!\b\S*[" + cons
                      + r"]\S*[" + cons + r"]\S*[" + cons + r"]\S*[" + cons + r"]\S*\b))", text)

def find_without_regex(text):
    good_words = []
    splitted_cons = list(cons)
    splitted_vows = list(vows)
    words = text.split(" ")
    for i in range(len(words) - 1):
        letters1 = list(words[i])
        how_many_vows_in_row = 0
        for letter in letters1:
            if how_many_vows_in_row == 2: break
            if letter in splitted_vows:
                how_many_vows_in_row += 1
            else: how_many_vows_in_row = 0
        if how_many_vows_in_row == 2:
            letters2 = list(words[i + 1])
            how_many_cons = 0
            for letter in letters2:
                if letter in splitted_cons:
                    how_many_cons += 1
            if how_many_cons <= 3:
                good_words.append(words[i])
    return good_words

test1 = "В течение всего дня мы ходили по городу и казалось, что каждый угол как-то связан с нами:\
 то в наших глазах отражались деревья, стоявшие на другой стороне улицы, или нас сбивали с ног разноцветные\
 рекламные щиты, которые всюду вешали предприимчивые люди."
test2 = "Для меня утро начинается с холодного душа под струями воды. Я люблю просыпаться\
 рано и готовить себе вкусный завтрак. Обычно я делаю кашу на молоке или яичницу с беконом."
test3 = "У меня есть множество увлечений, которыми я занимаюсь в свободное время. Например,\
 я увлекаюсь чтением книг различных жанров, начиная от классики и заканчивая фэнтези и детективами."
test4 = "Я часто езжу в поездах, потому что считаю, что это самый удобный способ передвижения.\
 Я садюсь на вокзале, занимаю свое место и раскладываю свои вещи, чтобы сделать себе уютно."
test5 = "Моя работа занимает большую часть моего времени, но я стараюсь не забывать про свои увлечения и хобби.\
 Я люблю готовить и экспериментировать с разными блюдами, а также проводить время на кухне со своей семьей и друзьями."

tests = [test1, test2, test3, test4, test5]
print("регулярное выражение:")
for i in range(len(tests)):
    print("     тест ", i + 1, ": ", find_with_regex(tests[i]))
print("без использования регулярного выражения:")
for i in range(len(tests)):
    print("     тест ", i + 1, ": ", find_without_regex(tests[i]))