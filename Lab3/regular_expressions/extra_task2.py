import re
def addUpperCase(list_of_letters):
    for i in list_of_letters:
        list_of_letters.remove(i)
        if (i == i.lower()):
            i = i + i.upper()
        else: i = i + i.lower()
        list_of_letters.insert(0, i)
    list_of_letters.reverse()

def rmUpperCase(list_of_list_of_letters):
    for i in list_of_list_of_letters:
        list_of_list_of_letters.remove(i)
        for j in i:
            i.remove(j)
            i.insert(0, j[0])
        i.reverse()
        list_of_list_of_letters.insert(0, i)
    list_of_list_of_letters.reverse()

def find_with_regex(text, letters, distance):
    addUpperCase(letters)
    return re.findall(r"\b\S*[" + letters[0] + r"]\S{" + distance + r"}[" + letters[1]
                      + r"]\S{" + distance + r"}[" + letters[2] + r"]\S*\b", text)

def find_without_regex(text, letters, distance):
    addUpperCase(letters)
    distance = int(distance)
    good_words = []
    words = text.split(" ")
    for i in range(len(words)):
        word_letters = list(words[i])
        if len(word_letters) > (2*distance + 2):
            for j in range(len(word_letters) - 2*distance - 2):
                if (word_letters[j] == letters[0][0]) or\
                        (word_letters[j] == letters[0][1]):
                    if (word_letters[j + distance + 1] == letters[1][0]) or\
                            (word_letters[j + distance + 1] == letters[1][1]):
                        if (word_letters[j + 2*distance + 2] == letters[2][0]) or\
                                (word_letters[j + 2*distance + 2] == letters[2][1]):
                            good_words.append(words[i])
    return good_words
test1 = "Одинокий дятел выбрал неожиданное для себя место для обитания - нагруженную вереском\
 поляну в таежном лесу, оживленную только редкими животными и звуками ветра. Дятел не строил гнездо\
  в высокой тополе, как его кузены, а устроил свое новое дом в запутанных корнях старого дерева. Каждый\
   день дятел трудился - грыз и выкладывал деталь за деталью свое будущее дома."
test2 = "Робот решил проехаться на мотоцикле в городском парке. Он одел свой защитный костюм\
 и шлем и отправился в путь. Поехав несколько кругов, робот заметил, что в дальнем углу парка располагается\
  много растений, среди которых присутствовали и розы. Не устояв перед этой красотой, робот решил остановиться\
   и посмотреть на цветы поближе."
test3 = "Книга - это окно в другой мир, возможность совершить путешествие во времени и пространстве. Она поражает\
 своим многогранностью и многословностью, открывая глаза на новые знания и идеи. Книга - это не только средство развлечения,\
  но и средство обучения и самосовершенствования."
test4 = "АропалО, ОппАорП, АгПггО, АоПогО, агопооо, АшПшО, АзхАзхО, АзхПгоО"
test5 = "Компьютер - это удивительное устройство, изменившее нашу жизнь и работу. Он способен ускорить все сферы нашей жизни,\
 от управления и финансов до музыки и фильмов. Компьютеры стали неотъемлемой частью производства во многих сферах, а также позволяют\
  людям работать и получать образование в любом уголке мира. "

tests = [test1, test2, test3, test4, test5]
list_of_list_of_letters = [["д", "т", "л"], ["р", "б", "т"], ["к", "и", "а"], ["а", "п", "о"], ["к", "ь", "р"]]
distances = ["1", "1", "1", "2", "3"]
print("регулярное выражение:")
for i in range(len(tests)):
    print("     тест", i + 1, ":")
    print("          ", "letters =", list_of_list_of_letters[i], "distance =", distances[i])
    print("          ", find_with_regex(tests[i], list_of_list_of_letters[i], distances[i]))
print("без использования регулярного выражения:")

for i in range(len(tests)):
    rmUpperCase(list_of_list_of_letters)
    print("     тест", i + 1, ":")
    print("          ", "letters =", list_of_list_of_letters[i], "distance =", distances[i])
    print("          ", find_without_regex(tests[i], list_of_list_of_letters[i], distances[i]))