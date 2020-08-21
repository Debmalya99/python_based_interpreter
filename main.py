'''
A very basic program can be:
Evaluating 8 + 2 - 6 + 4
'''

from Machine import *

machine = Machine()
#src = open('assembly_source/simple_arithmetic.sasm')

machine.add_program_from_file('assembly_source/simple_arithmetic.sasm')

machine.evaluate()
print(machine.get_top())