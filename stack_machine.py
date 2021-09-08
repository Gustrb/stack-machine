from instruction_set import Instruction
from typing import List


class StackMachine:
    def __init__(self, program: List[Instruction]) -> None:
        self.stack = []
        self.program = program

    def run_program(self):
        for operation in self.program:
            operation.run(self.stack)

