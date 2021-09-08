from typing import List
from enum import Enum


class InvalidInstruction(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class OperationType(Enum):
    OP_PUSH = 1,
    OP_DUMP = 2,
    OP_PLUS = 3,
    OP_SUB  = 4,
    OP_MUL  = 5,
    OP_DIV  = 6


class Instruction:
    def __init__(self, operation: OperationType, value = None) -> None:
        self.operation = operation
        self.value = value

    def run(self, stack: List):
        raise NotImplementedError()


class PushInstruction(Instruction):
    def __init__(self, value) -> None:
        super().__init__(OperationType.OP_PUSH, value=value)

    def run(self, stack: List):
        stack.append(self.value)


class PlusInstruction(Instruction):
    def __init__(self) -> None:
        super().__init__(OperationType.OP_PLUS)

    def run(self, stack: List):
        if len(stack) < 2:
            raise InvalidInstruction('PlusInstruction: Too few arguments')

        second_operand = stack.pop()
        first_operand = stack.pop()

        stack.append(first_operand + second_operand)

class SubtractInstruction(Instruction):
    def __init__(self) -> None:
        super().__init__(OperationType.OP_SUB)

    def run(self, stack: List):
        if len(stack) < 2:
            raise InvalidInstruction('SubtractInstruction: Too few arguments')

        second_operand = stack.pop()
        first_operand = stack.pop()

        stack.append(first_operand - second_operand)

class MultiplyInstruction(Instruction):
    def __init__(self) -> None:
        super().__init__(OperationType.OP_MUL)

    def run(self, stack: List):
        if len(stack) < 2:
            raise InvalidInstruction('MultiplyInstruction: Too few arguments')

        second_operand = stack.pop()
        first_operand = stack.pop()

        stack.append(first_operand * second_operand)

class DivisionInstruction(Instruction):
    def __init__(self) -> None:
        super().__init__(OperationType.OP_DIV)

    def run(self, stack: List):
        if len(stack) < 2:
            raise InvalidInstruction('DivisionInstruction: Too few arguments')

        second_operand = stack.pop()
        first_operand = stack.pop()

        if second_operand == 0:
            raise InvalidInstruction('DivisionInstruction: Division by zero error')

        stack.append(first_operand // second_operand)


class DumpInstruction(Instruction):
    def __init__(self) -> None:
        super().__init__(OperationType.OP_DUMP)

    def run(self, stack: List):
        print('-------------------------------')
        for (index, value) in enumerate(stack):
            print(f'{index}: {value}')

