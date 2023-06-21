
m=input("enter the first letter of your birth month:")
if(m=='j'):
  print("either january, june or july")
  n=input("enter the second letter of your birth month:")
  if(n=='a'):
    print("january")
  elif(n=='u'):
    print("either june or july")
  
    x=input("enter the third letter of your birth month:")
    if(x=='n'):
      print("june")
    elif(x=='l'):
      print("july")
    else:
      print("other")
elif(m=='f'):
  print("february")
elif(m=='m'):
  print("either march or may")
  o=input("enter the second letter of your birth month:")
  if(o=='a'):
    print("either march or may")
 
    y=input("enter the third letter of your birth month:")
    if(y=='r'):
      print("march")
    elif(y=='y'):
      print("may")
    else:
      print("other")
elif(m=='a'):
  print("either april or august")
  z=input("enter the second letter of your birth month:")
  if(z=='p'):
    print("april")
  elif(z=='u'):
    print("august")
  else:
    print("other")
elif(m=='s'):
  print("september")
elif(m=='o'):
  print("october")
elif(m=='n'):
  print("november")
elif(m=='d'):
  print("december")  
else:
  print("you are not a human being\nyou are somethimg else")
