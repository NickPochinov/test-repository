def numtostr3(number: str, man_rod: bool = True):
    itog: str = ""
    textnum: str = ""
    correct_number: str = ""
    if (number[0] == "-"):
        itog += "минус "
        number = number.removeprefix("-")
    for n in number:
        add: bool = True
        if (n == "0"):
            textnum += "ноль "
        elif (n == "1"):
            textnum += "один " if (man_rod) else "одна "
        elif (n == "2"):
            textnum += "два " if (man_rod) else "две "
        elif (n == "3"):
            textnum += "три "
        elif (n == "4"):
            textnum += "четыре "
        elif (n == "5"):
            textnum += "пять "
        elif (n == "6"):
            textnum += "шесть "
        elif (n == "7"):
            textnum += "семь "
        elif (n == "8"):
            textnum += "восемь "
        elif (n == "9"):
            textnum += "девять "
        else:
            add = False
        if (add):
            correct_number += n
    textnums: list = textnum.split()
    if (correct_number == "0"):
        return "ноль"
    elif (correct_number == "10"):
        return "десять"
    if (int(correct_number) > 10 and int(correct_number) < 20):
        if (int(correct_number) >= 15):
            itog += str(textnums[1]).removesuffix("ь") + "надцать"
        elif (correct_number == "11"):
            itog += "одиннадцать"
        elif (correct_number == "12"):
            itog += "двеннадцать"
        elif (correct_number == "13"):
            itog += "триннадцать"
        else:
            itog += "четырнадцать"
    else:
        for i in range(len(textnums)):
            if (textnums[i] == "четыре"):
                if (len(textnums) - i == 2):
                    itog += "сорок "
                    continue
            if (textnums[i] == "девять"):
                if (len(textnums) - i == 2):
                    itog += "девянносто "
                    continue
            if (i == 0 and len(textnums) == 3):
                if (int(correct_number[i]) == 1):
                    itog += "сто "
                elif (int(correct_number[i]) == 2):
                    itog += "двести "
                elif (int(correct_number[i]) == 3 or int(correct_number[i]) == 4):
                    itog += textnums[i] + "ста "
                else:
                    itog += textnums[i] + "сот "
                continue
            if (len(textnums) - i == 2):
                num: int = int(str(correct_number[i]) + str(correct_number[i + 1]))
                if (num >= 10 and num < 20):
                    if (num >= 15):
                        itog += str(textnums[1]).removesuffix("ь") + "надцать"
                    elif (num == 11):
                        itog += "одиннадцать"
                    elif (num == 12):
                        itog += "двеннадцать"
                    elif (num == 13):
                        itog += "триннадцать"
                    elif (num == 10):
                        itog += "десять"
                    else:
                        itog += "четырнадцать"
                    break
            if (textnums[i] != "ноль"):
                itog += textnums[i]
            if (len(textnums) - i == 2):
                if (int(correct_number[i]) >= 5 and int(correct_number[i]) < 9):
                    itog += "десят "
                elif (int(correct_number[i]) >= 2 and int(correct_number[i]) < 4):
                    itog += "дцать "
    return itog.strip()
def getStringIndentity(number_length: int, num3zn: int):
    if (number_length < 4):
        return ""
    ids: list = ["тысяча", "миллион", "миллиард", "триллион", "квадраллион", "квинтиллион", "сепстиллион", "октиллион"]
    ids2: list = ["тысячи", "миллиона", "миллиарда", "триллиона", "квадраллиона", "квинтиллиона", "сепстиллиона", "октиллиона"]
    ids3: list = ["тысяч", "миллионов", "миллиардов", "триллионов", "квадраллионов", "квинтиллионов", "сепстиллионов", "октиллионов"]
    last: int = num3zn % 10
    last2: int = num3zn % 100
    current: list = []
    correct_length: int = number_length
    while ((correct_length - 1) % 3 != 0):
        correct_length -= 1
    current = [ids[correct_length // 3 - 1], ids2[correct_length // 3 - 1], ids3[correct_length // 3 - 1]]
    if (last2 == 11 or last2 == 12 or last2 == 13 or last2 == 14):
        return current[2]
    elif (last == 1):
        return current[0]
    elif (last >= 2 and last < 5):
        return current[1]
    else:
        return current[2]
def numtostr(number: str):
    if (number.count("0") == len(number)):
        return "ноль"
    sections: list = []
    itog: str = ""
    current: str = ""
    converted_length: int = 0
    if (number[0] == "-"):
        itog += "минус "
        number = number.removeprefix("-")
    for i in range(len(number)):
        current += number[i]
        converted_length += 1
        if ((len(number) - converted_length) % 3 == 0):
            if (current.count("0") == len(current)):
                for j in range(len(current)):
                    sections.append("0")
            else:
                while (current.find("0") == 0):
                    current = current.removeprefix("0")
                sections.append(current)
            current = ""
    if (len(current) != 0):
        if (current.count("0") == len(current)):
            for j in range(len(current)):
                sections.append("0")
        else:
            while (current.find("0") == 0):
                current = current.removeprefix("0")
            sections.append(current)
    number_length: int = len(number)
    for s in sections:
        if (s != "0"):
            man_rod: bool = False if (number_length == 4) else True
            itog += numtostr3(s, man_rod) + " " + getStringIndentity(number_length, int(s)) + " "
        number_length -= len(s)
    return itog.strip()