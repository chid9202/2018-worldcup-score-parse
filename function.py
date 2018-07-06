import datetime
import time

def getNow():
    year = datetime.date.today().strftime("%G")
    monthOfYear = datetime.date.today().strftime("%b") # June
    dayOfWeek = datetime.date.today().strftime("%A") # Friday
    dayOfMonth = datetime.date.today().strftime("%d") # 29
    now = dayOfMonth + ' ' + monthOfYear + ' ' + year
    return now


"""
Get nth line from a string
in: "line1 is what\n line2 is who\n line3 is which\n", "2"
out: "line2 is who"
"""
def get_nth_line(str, number):
    str = str.splitlines()
    str = str[number]
    return str

"""
Get number of words in a string
in: "here is string", "2"
out: "here is"
"""
def get_first_n_words(str, number):
    str = str.split()
    result = ""
    for i in range(0, number):
        result += str[i] + " "
    result = remove_last(result)
    return result

"""
Remove last character of a string
in: "teststring"
out: "teststrin"
"""
def remove_last(str):
    return str[:-1]

"""
Convert country name to country code
in: "Russia"
out: "ru"

"""
def convert_name_to_code(name):
    if name == "Russia":
        return "ru"
    elif name == "Uruguay":
        return "uy"
    elif name == "Egypt":
        return "eg"
    elif name == "Saudi Arabia":
        return "sa"
        # B
    elif name == "Portugal":
        return "pt"
    elif name == "Spain":
        return "es"
    elif name == "Morocco":
        return "ma"
    elif name == "IR Iran":
        return "ir"
        # C
    elif name == "France":
        return "fr"
    elif name == "Australia":
        return "au"
    elif name == "Peru":
        return "pe"
    elif name == "Denmark":
        return "dk"
        # D
    elif name == "Argentina":
        return "ar"
    elif name == "Iceland":
        return "is"
    elif name == "Croatia":
        return "hr"
    elif name == "Nigeria":
        return "ng"
        # E
    elif name == "Brazil":
        return "br"
    elif name == "Switzerland":
        return "ch"
    elif name == "Costa Rica":
        return "cr"
    elif name == "Serbia":
        return "rs"
        # F
    elif name == "Germany":
        return "de"
    elif name == "Mexico":
        return "mx"
    elif name == "Sweden":
        return "se"
    elif name == "Korea Republic":
        return "kr"
        # G
    elif name == "Belgium":
        return "be"
    elif name == "Panama":
        return "pa"
    elif name == "Tunisia":
        return "tn"
    elif name == "England":
        return "gb-eng"
        # H
    elif name == "Poland":
        return "pl"
    elif name == "Senegal":
        return "sn"
    elif name == "Colombia":
        return "co"
    elif name == "Japan":
        return "jp"
