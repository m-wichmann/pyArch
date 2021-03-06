# Instruction Set Architecture
This file describes the ISA.

## General instruction design
* More or less RISC design
* Fixed length: 32 Bit long
    * 8 Bit instruction (e.g. add)
    * 8 Bit flags (depends on instructions; e.g. signed, number-number, address-number, address-address...)
    * 8 Bit first operand (e.g. 4)
    * 8 Bit second operand (e.g. 3)

* First operand always target register
* second operand register or constant
    * Flags Bit 0 (arithmetic and logic): second operand number else register
* ram -> register only mov, pop, push

## Opcodes (Instruction Set)
* to sort:
    * set bit, clear bit, clear reg
    * test, cmp
    * branch (if equal...)
    * flag set, clear

- 0x00 - 0x0F       Basic instructions (nop...)
    + 0x00            nop (should be standard value in mem; see NOP slide)
    - 0x0F            slp (sleep)
+ 0x10 - 0x1F       Data handling (mov...)
    + 0x10            mov (copy register)
    + 0x11            ld  (load ram|constant (flag bit 0) to register; register, $address|constant)
    + 0x12            st  (store register to ram; register, $address)
    + 0x13            push (register)
    + 0x14            pop (register)
+ 0x20 - 0x2F       Arithmetic (add, sub...)
    + 0x20            add (register, register|constant)
    + 0x21            sub (register, register|constant)
    + 0x22            mul (register, register|constant)
    + 0x23            div (register, register|constant)
    + 0x2E            inc (increment; register)
    + 0x2F            dec (decrement; register)
+ 0x30 - 0x3F       Logic (and, or, com, neg...)
    + 0x30            and (register, register|constant)
    + 0x31            or  (register, register|constant)
    + 0x32            xor (register, register|constant)
    + 0x33            com (one's complement; register)
    + 0x34            neg (two's complement; register)
    + 0x35            lsl (logical shift left; register, shift_count)
    + 0x36            lsr (logical shift right; register, shift_count)
    + 0x37            rol (rotate left; register, rotate_count)
    + 0x38            ror (rotate right; register, rotate_count)
    + 0x3F            tst (set zero and sign flag for register; register)
- 0x40 - 0x4F       Reserved
    - 0x42            egg (easteregg ;-))
- 0x50 - 0x8F       Control flow (jmp, call, ret...)
    + 0x50            jmp (direct jump, if register else relative +-7bit; register|constant)

    + 0x60            breq (branch if equal (z = 1); register|constant)
    + 0x61            brne (branch not equal (z = 0); register|constant)
    + 0x62            brp  (branch if positive (n = 0); register|constant)
    + 0x63            brn  (branch if negative (n = 1); register|constant)

    - 0x88            call (call; store ip)
    - 0x89            ret (return; get ip back)
    + 0x8F            cmp (compare/subtract register with register|constant; register, register|constant)
- 0xA0 - 0xFF       Systemcalls (e.g. print)
    + 0xA0            prt (print value of register)







