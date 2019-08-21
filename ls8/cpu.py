import sys

# Main CPU class
class CPU:
    # Construct a new CPU
    def __init__(self):
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0


    # Load a program into memory
    def load(self, file_name):
        address = 0
        
        with open(file_name, 'r') as f:
            for line in f:
                if line.startswith('#') or line.startswith('\n'):
                    continue
                else:
                    instruction = line.split(' ')[0]
                    self.ram[address] = int(instruction, 2)
                    address += 1
        


    # Read RAM at given address and return that value
    def ram_read(self, mar):
        return self.ram[mar]


    # Write a value at given address
    def ram_write(self, mar, mdr):
        self.ram[mar] = mdr


    # ALU operations
    def alu(self, op, reg_a, reg_b):
        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")


    # Handy function to print out the CPU state. 
    # You might want to call this from run() if you need help debugging.
    def trace(self):
        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()


    # Run the CPU
    def run(self):
        LDI = 0b10000010
        PRN = 0b01000111
        HLT = 0b00000001

        running = True

        while running:
            ir = self.ram_read(self.pc)

            if ir == HLT:
                running = False

            if ir == PRN:
                reg = self.ram_read(self.pc + 1)
                print(self.reg[reg])
                self.pc += 2

            if ir == LDI:
                reg_a = self.ram_read(self.pc + 1)
                reg_b = self.ram_read(self.pc + 2)
                self.reg[reg_a] = reg_b
                self.pc += 3       