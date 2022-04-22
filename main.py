#1.

#card=("1234123456785678")
#card = "******5678"

#def card_hide(card):
 #   return '*' * len(card[:-4]) + card[-4:]
#2.

#def Palindrome(a):
 #   if len(a)<1:
 #       return True
 #   else:
 #       if a[0]==a[-1]:
 #           return Palindrome(a[1:-1])
  #      else:
  #           return False
#a=str(input("Ввод данных"))
#if Palindrome(a) is True:
   # print("слово является палиндромом")
#else:
    #print("слово не является палиндромом")

#3.
import string


class Alphabet:

    def __init__(self, language, letters_str):
        self.lang = language
        self.letters = list(letters_str)

    def print(self):
        print(self.letters)

    def letters_num(self):
        len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return True
        return False

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        print("English Example:\nDon't judge a book by it's cover".)
    if __name__ == '__main_':
    eng_alphabet = EngAlphabet
    eng_alphabet.print()
    print(eng_alphabet.letters_num())
    print(eng_alphabet.is_en_letter('F'))








    -
    print(eng_alphabet.is_en_letter('Щ'))
    EngAlphabet.example()
b