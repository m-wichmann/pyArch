ld  r1, 0xdeadbeef
ld  r2, 0xdecafbad

ld  r3, @mark
jmp r3

prt r1

mark:
prt r2

add r1, r2
prt r1
