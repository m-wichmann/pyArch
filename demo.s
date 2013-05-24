ld  r6, 0xdeadbeef
ld  r7, 0xdecafbad

ld  r1, 0xf0000001

ld  r3, @mark1

tst r1

brp r3
prt r6

mark1:
prt r7
