import math
import re
print("=====================================================================================\n"
      "Hej velkommen til Alberts latex formel generator\n"
      "Du skal blot skrive din formel og afslutte med \";\"."
      "Hvis nu du skal lave en ny linje at skrive din formel på skal du benytte \"\\\" så formaterer den automatisk i "
      "outputtet.\n "
      "Du kan benytte følgende symboler:\n"
      "\tmultiplikation: *\n"
      "\taddition: +\n"
      "\tsubtraktion: -\n"
      "\tdivision: /\n"
      "\tpotenser: ^ (virker ikke for nævner i brøker)\n "
      "Et eksempel på en formel er \"13x+2a^32/3=0\\2c*b=a;\" som giver outputtet:\n"
      "\t\t\\begin{align*}\n\t\t\t13x+\\frac{2a^{32}}{3}&=0\\\\\n\t\t\t2c\cdot b&=a\n\t\t\end{align*}\n"
      "For at afslutte skal du skrive \"#quit;;\"\n"
      "=====================================================================================")
print("Skriv din ligning her: ")
inn = ""


def strtoint(in_str):
    counter = 0
    for i in range(0, len(in_str)):
        curr_index = 10 ** (len(in_str) - (i + 1))
        counter += (ord(in_str[i]) - 48) * curr_index
    return counter


def create_func(in_str):
    nums_in_eq = []
    working_num = ""
    for i in range(len(in_str)):
        curr_state = 46 < ord(in_str[i]) < 58
        if curr_state:
            working_num += in_str[i]
        else:
            nums_in_eq.append(strtoint(working_num))
            working_num = ""

    print(nums_in_eq)


def automate_latex(in_str):
    acc = ""
    nums_in_eq = []
    working_num = ""
    holder = ""
    finished = False
    needs_two_num = False
    for letter in in_str:
        curr_state = 47 < ord(letter) < 58
        with_var = False
        if letter.isalpha():
            with_var = True
        else:
            with_var = False
        if curr_state:
            finished = False
            working_num += letter
        else:
            finished = True
            nums_in_eq.append(strtoint(working_num))
            if not needs_two_num:
                holder = working_num+letter if with_var else working_num
            else:
                holder += working_num + '}'
                needs_two_num = False
            working_num = "" if not with_var else holder
        if not with_var:
            match letter, finished, needs_two_num:
                case '/', True, _:
                    needs_two_num = True
                    acc += "\\frac{" + f"{holder}" + "}{"
                    holder = ""
                case '\\', _, _:
                    acc += holder + "\\\\"+"\n\t"
                case '^', True, _:
                    needs_two_num = True
                    holder += letter + '{'
                case _, True, _:
                    acc += holder + format_as(letter) if letter != ';'else holder
                    holder = ""
                case ';', _, _:
                    break
    return acc

def format_as (letter):
    val = ""
    match letter:
        case '*':
            val = "\cdot "
        case '=':
            val = "&="
        case '\\':
            val = ""
        case ';':
            val = ''
        case '(':
            val = "\\left("
        case ')':
            val = "\\right)"
        case _:
            val = letter
    return val


def for_latex_eq(in_str):
    print("\\begin{align*}\n\t"+automate_latex(in_str)+"\n\\end{align*}")
while inn != "#quit;;":
    inn = input()
    for_latex_eq(inn)
