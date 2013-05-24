ld      r31, 0xdeadbeef # var to print

ld      r4, @print
ld      r5, @end
ld      r6, @top

ld      r0, 2          # run var
ld      r1, 0           # end var

top:
cmp     r0, r1
breq    r5

call    r4
add     r1, 1

jmp r6

print:
prt     r31
ret




end:
