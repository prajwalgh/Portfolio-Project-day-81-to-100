import time
import requests
from api import quotes

print("Press Enter to print test to write")
string=quotes()['text']
user_input = input()
def accuracy1(user_input):
  l=len(string)
  count=1
  for i in zip(user_input,string):
    if i[0]==i[1]:
      count+=1
  x=(count/l) *100
  return x
if user_input == "":
  print(f"{string}")
  x=time.time()
  text=input()
  y=time.time() -x
  z=accuracy1(text)
  print(f"required time {y}, and accuracy is {z} %")
else:
    print("You didn't press the Enter key.")
