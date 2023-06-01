import re
def count_with_regex(text, spaces):
    if spaces == True:
        expression = r"(?<=\s)\[<O(?=\s)"
    else: expression = r"\[<O"
    how_many = 0
    for i in re.findall(expression, text):
        how_many += 1
    return how_many

def count_without_regex(text, spaces):
    how_many = 0
    if spaces == True:
        splitted_text = text.split(" ")
        for word in splitted_text:
            if word == "[<O":
                how_many += 1
        return how_many
    else:
        for i in range(len(text) - 2):
            if (text[i] == "[") and (text[i + 1] == "<") and (text[i + 2] == "O"):
                how_many += 1
        return how_many


test1 = "В четве́рг[<O четвёртого числа́ [<O в четы́ре с че́тве[<Oртью часа́ лигури́йский [<Oрегулиро́вщик регули́ровал в Лигу́рии."
test2 = "Но три́дцать[< O три корабля́ лави́ровали [ < O, лави́ровали, [<O да та[<Oк и не [<O вы́лавировали."
test3 = "А пото́м [[[протоко́л [<<про протоко́л п[[<<OOротоко́лом запротоколи́ровал."
test4 = "Как интервьюе́ром [<O интервьюи́руемый, лигури́йский [<O[<O [<Oрегулиро́вщик, речи́сто, [<O да не чи́сто рапортова́л."
test5 = "Да не́ дорапортова́л, [<O [<O [<O [<O [<O [<O [<O [<O дорапорто́вывал. Да так зарапортова́лс[<Oя про\
 [<O[<O[<O размо́кропого́дившуюся пого́ду, что..."
tests = [test1, test2, test3, test4, test5]

print("Считая смайликом набор символов [<O, окруженный пробелами:")
print("     регулярное выражение:")
for i in range(len(tests)):
    print("         тест ", i + 1, ": ", count_with_regex(tests[i], True))
print("     без использования регулярного выражения")
for i in range(len(tests)):
    print("         тест ", i + 1, ": ", count_without_regex(tests[i], True))

print("Считая смайликом набор символов [<O, стоящий в любом месте текста:")
print("     регулярное выражение:")
for i in range(len(tests)):
    print("         тест ", i + 1, ": ", count_with_regex(tests[i], False))
print("     без использования регулярного выражения")
for i in range(len(tests)):
    print("         тест ", i + 1, ": ", count_without_regex(tests[i], False))