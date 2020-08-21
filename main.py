'''
A very basic program can be:
Evaluating 8 + 2
'''

from Machine import *

machine = Machine()
machine.add_program_line("PUSHI 8")
machine.add_program_line("PUSHI 2")
machine.add_program_line("ADD")
machine.evaluate()
print(machine.get_top())