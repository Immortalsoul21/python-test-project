
name=input("enter your name:")
print("hello" , name)
time=float(input("enter the time:"))
if time<12.00:
  print("good morning ",name)
elif time > 12.00 and time<16.00:
  print("good afternoon" , name)
else: 
  print("good night" ,name)