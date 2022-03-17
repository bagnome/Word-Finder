from datetime import datetime 
import re
import sys

class Wordle_Helper:
    errStr = 'You may enter a word as an argument that is five letters in length with only characters A-Z, a-z or underscores. No numbers, special characters, or accented characters are allowed.'

    def __init__(self):
        self.guess = ''
        if len(sys.argv) > 1:
            self.guess = sys.argv[1]
        self.letters_present = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
        self.matched_words = []
        self.check_validiy()
        self.read_words_file()

    def stop_with_err(self):
        print(self.errStr)
        sys.exit()

    def check_validiy(self):
        if len(self.guess) == 5:
            return
        if re.match('[a-zA-Z|_]{5}', self.guess, re.IGNORECASE):
            return
        self.stop_with_err()

    def read_words_file(self):
        try:
            f = open('five_letter_words.txt','r')
            self.words = f.readlines()
        except:
            print('Could not read five_letter_words.txt')
            sys.exit()

    def split(self, word):
        return [char for char in word]

    def gen_expr(self):
        expr = ''
        guess_chars = []
        guess_chars = self.split(self.guess)
        for c in guess_chars:
            if c == '_':
                expr += '[a-z]'
            elif c.isupper():
                expr += c.lower()
            elif c.islower():
                expr += '[^' + c + ']'
                self.letters_present[c] += 1
            else:
                self.stop_with_err()
        return expr

    def match_with_known_letters(self, guess_expr):
        matches = []
        for word in self.words:
            if re.match(guess_expr, word, re.IGNORECASE):
                matches.append(word)
        return matches

    def match_with_present_letters(self, matches):
        new_matches = []
        new_matches = matches
        for key, val in self.letters_present.items():
            if val <= 0:
                continue
            temp_matches = []
            for m in new_matches:
                if m.count(key) >= val:
                    temp_matches.append(m)
            new_matches = temp_matches
        
        return new_matches

    def write_to_file(self, matches):
        now = datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
        with open('output__' + now + '.txt', 'w') as f:
            f.writelines(matches)
            f.close()

    def find_matches(self):
        guess_expr = self.gen_expr()
        matches = self.match_with_known_letters(guess_expr)
        matches = self.match_with_present_letters(matches)
        self.write_to_file(matches)

main = Wordle_Helper()
main.find_matches()