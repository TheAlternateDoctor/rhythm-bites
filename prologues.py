output = open("prologue.txt","w")
for x in range(0x61):
    output.write("case "+hex(x)+"\n")
    output.write("0xA4 "+hex(x)+"\n")
    output.write("break\n")