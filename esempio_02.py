n=int(input("inserisci un numero: "))
l=input("inserisci una lettera: ")
for i in range(1,n+1):
    print(" "*(n-i) + l*(1+(i-1)*2))