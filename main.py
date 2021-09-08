from instruction_set import DumpInstruction, PlusInstruction, PushInstruction
from stack_machine import StackMachine


def main():
    program = [
        PushInstruction(1),
        PushInstruction(2),
        DumpInstruction(),
        PlusInstruction(),
        DumpInstruction()
    ]

    stack_m = StackMachine(program)
    stack_m.run_program()

if __name__ == '__main__':
    main()
