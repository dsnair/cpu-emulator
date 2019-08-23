# Computer Architecture

## Project

* [Implement the LS-8 Emulator](ls8/)

## Task List: add this to the first comment of your Pull Request

### Day 1: Get `print8.ls8` running

- [x] Inventory what is here
- [x] Implement the `CPU` constructor
- [x] Add RAM functions `ram_read()` and `ram_write()`
- [x] Implement the core of `run()`
- [x] Implement the `HLT` instruction handler
- [x] Add the `LDI` instruction
- [x] Add the `PRN` instruction

### Day 2: Add the ability to load files dynamically, get `mult.ls8` running

- [x] Un-hardcode the machine code
- [x] Implement the `load()` function to load an `.ls8` file given the filename
      passed in as an argument
- [x] Implement a Multiply instruction (run `mult8.ls8`)

### Day 3: Stack

- [x] Implement the System Stack and be able to run the `stack.ls8` program

### Day 4: Get `call.ls8` running

- [x] Implement the CALL and RET instructions
- [x] Implement Subroutine Calls and be able to run the `call.ls8` program

### Day 5: Sprint Challenge, get `sctest.ls8` working

- [x] Add the `CMP` instruction and `equal` flag to your LS-8.
- [x] Add the `JMP` instruction.
- [x] Add the `JEQ` and `JNE` instructions.

1. When is the ALU activated in the CPU?

    ALU is activated when logic based arithmetic operations are called.

2. Why is the purpose of a CPU stack?
    1. Temporary storage of variables.
    Suppose we want to store the values of some variables. Since there are a limited number of registers, we can push their values on to a stack, re-use those registers to store those variable values, then pop them off the stack when done. 

    2. Store the return address of a subroutine.
    Suppose CALL is called. The program executes that part of the code until RET is reached. At RET, the program resumes to what it was doing before CALL. We can store this return address in the CPU stack.

    3. Store registers and CPU state to handle interrupt.
    When there is an interrupt, like a keyboard interrupt, that part of the program runs. After the interrupt ends and the program is to be resumed, we can restore the entire CPU state such as registers, flags, etc. from the CPU stack.

    4. Store subroutine local variables.
    Same as #1

3. Convert 01010110 to Decimal:
    0101 = (0 * 2^3) + (1 * 2^2) + (0 * 2^1) + (1 * 2^0) = 5
    0110 = (0 * 2^3) + (1 * 2^2) + (1 * 2^1) + (0 * 2^0) = 6
    Thus, 56

4. Convert 10100011 to Hexadecimal:
    1010 = (1 * 2^3) + (0 * 2^2) + (1 * 2^1) + (0 * 2^0) = 10 = A
    0011 = (0 * 2^3) + (0 * 2^2) + (1 * 2^1) + (1 * 2^0) = 3
    Thus, A3

### Stretch

- [ ] Add the ALU operations: `AND` `OR` `XOR` `NOT` `SHL` `SHR` `MOD`
- [ ] Add an `ADDI` extension instruction to add an immediate value to a register
- [ ] Add timer interrupts
- [ ] Add keyboard interrupts
- [ ] Write an LS-8 assembly program to draw a curved histogram on the screen