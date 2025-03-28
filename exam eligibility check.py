medical_cause=input("did you have a medical cause y or n:")
atten=int(input("enter the attendance of the student:"))
if medical_cause=='y':
#checking the condition:
  print("you are allowed")
else:
  if atten>=75: #checking the condition 2
    print("allowed")
  else:
    print("not allowed")