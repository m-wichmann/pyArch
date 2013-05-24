ld  r1, 0xdeadbeef
ld  r2, 0xdecafbad

push r2
push r1

pop r7
pop r8

prt r7
prt r8

ld  r3, @mark
jmp r3

prt r1

mark:
prt r2

add r1, r2
prt r1
