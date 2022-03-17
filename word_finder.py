from datetime import datetime 
import re
import sys

class Wordle_Helper:
    errStr = 'You may enter a word as an argument that is five letters in length with only characters A-Z, a-z or underscores. No numbers, special characters, or accented characters are allowed.'

    def __init__(self):
        self.output_setting = 'console'
        self.output_dir = ''
        self.handle_cli_args(sys.argv)
        self.guess = ''
        if len(sys.argv) > 1:
            self.guess = sys.argv[1]
        self.letters_present = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
        self.matched_words = []
        self.check_validiy()
        self.read_words_file()

    def handle_cli_args(self, args):
        for arg in args:
            if arg.startswith('-o'):
                self.output_setting = 'file'
                o_param = arg.split('=')
                if len(o_param) == 2:
                    self.output_dir = o_param[1]

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
        try:
            with open(self.output_dir + 'output__' + now + '.txt', 'w') as f:
                f.writelines(matches)
                f.close()
        except:
            print('A problem was encountered while saving to file. Check that the directory was written correctly.')

    def write_to_console(self, matches):
        print('\n')
        for m in matches:
            print(m)
            curr_index = matches.index(m) + 1
            if (curr_index)%20 == 0:
                input('------------------------------\n' + str(curr_index) + ' of ' + str(len(matches)) + '\nPress any key to show more...\n------------------------------')

        print('------------------------------\n' + str(len(matches)) + ' matches found.\nDone.\n------------------------------')

    def find_matches(self):
        guess_expr = self.gen_expr()
        matches = self.match_with_known_letters(guess_expr)
        matches = self.match_with_present_letters(matches)
        if self.output_setting == 'file':
            self.write_to_file(matches)
        else:
            self.write_to_console(matches)

main = Wordle_Helper()
main.find_matches()