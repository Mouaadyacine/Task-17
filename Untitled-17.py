a=int( input("svp entrer votre age"))
s=input("svp entrer votre sexe")
if a>20 or a==20 and s=="homme":
  print("toi imposable")
elif a>18 or a==18 and s=="femme":
  print("toi imposable")
else:
  print("toi ne pas imposable")