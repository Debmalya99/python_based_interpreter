class Machine:
    __stack = list()
    __program = list()
    def __init__(self):
        pass

    def add_program_line(self,line):
        self.__program.append(line)

    def __process_line(self,line):
        # This is the main big function
        list_words = line.split(' ')
        # Now we check the list_words[0]
        if(list_words[0] == 'PUSHI'):
            num = int(list_words[1])
            self.__stack.append(num)
        if(list_words[0] == 'ADD'):
            num1 = self.__stack.pop()
            num2 = self.__stack.pop()
            self.__stack.append(num1+num2)

    def evaluate(self):
        for line in self.__program:
            self.__process_line(line)

    def get_top(self):
        return self.__stack[-1]