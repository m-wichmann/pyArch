# CPU
CPU arch is based in Von-Neumann-Architecture

* CPU contains following modules:
    * ALU (got its own file)
    * Control Unit (implemented in this file)
    * maybe Decode Stage in own file?!
    * Memory (only data that is necesary for execution)
    * Flags (e.g. carry, zero)
    * Registers (ARM-style 32 register; r0 to r31)
    * System registers (ip, sp, temp regs t0 to t3)

* Computation is done in following stages:
    * Get data at IP
    * Decode instruction
    * Fetch data
    * Execute instruction
    * Write data

* Maybe implement Cache, Branch-Prediction, Pipelining etc.

* System registers
    * IP -> Instruction pointer
    * SP -> Stack pointer
    * SREG -> Status
        * Bit 0: Carry
        * Bit 1: Zero
        * Bit 2: Negative
        * Bit 3: Overflow
        * Bit 4: Sign
