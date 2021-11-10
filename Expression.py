#  File: Expression.py

#  Description: Evaluates a tokenized boolean expression.

#  Student Name: Alice Gee

#  Student UT EID: ag67642

#  Course Name: CS 313E

#  Unique Number: 86610

VALID_CHARS = ['T', 'F', '&', '|', '(', ')', ' ']

class Tokenizer(object):
    def __init__(self, string):
        self.__string = string.strip()
        self.__curr_idx = 0
        self.__has_next = len(self.__string) > 0
    
    def peek(self):
        old_curr_idx = self.__curr_idx
        old_has_next = self.__has_next

        next_val = self.next()

        self.__curr_idx = old_curr_idx
        self.__has_next = old_has_next

        return next_val

    def next(self):
        if not self.has_next():
            raise ValueError('String has no additional characters to tokenize.')
        elif self.__string[self.__curr_idx] not in VALID_CHARS:
            raise ValueError('Invalid character in given string.')
        elif self.__string[self.__curr_idx] == ' ':
            self.__curr_idx += 1
            return self.next()
        else:
            self.__curr_idx += 1

            if self.__curr_idx >= len(self.__string):
                self.__has_next = False
            

            return_val = self.__string[self.__curr_idx - 1]

            if return_val == 'T':
                return_val = True
            elif return_val == 'F':
                return_val = False
            return return_val
    
    def has_next(self):
        return self.__has_next
        

class Evaluator(object):
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
    
    def evaluate_expression(self):
        # FILL THIS IN: evaluate the expression given by the tokenizer and return the boolean value

    def parse_or(self):
        # SUGGESTED HELPER METHOD (NOT REQUIRED)

    def parse_and(self):
        # SUGGESTED HELPER METHOD (NOT REQUIRED)

    def parse_paren(self):
        # SUGGESTED HELPER METHOD (NOT REQUIRED)

    def parse_token(self):
        # SUGGESTED HELPER METHOD (NOT REQUIRED)
        

def main():
    boolean_expr = input()

    print(Evaluator(Tokenizer(boolean_expr)).evaluate_expression())

if __name__ == "__main__":
    main()
