a = "AAAAAAA"
b = "bbbbbbbb"
c = 1.1
string = "a={nome2} b={nome1} c={nome3:.2f}"
formato = string.format(nome2=a,nome1=b,nome3=c)

print(formato)