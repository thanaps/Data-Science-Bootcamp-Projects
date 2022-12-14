# import random 
from random import sample

print("Condition of Pao Ying Chub")
print(" self draw self\n",
      "hammer lose paper\n",
      "hammer win scissors\n",
      "scissors win paper")
results = ("draw","lose","win")
user_name = input("What's your name? ->") 
print(f"Hi {user_name}")
win_num = 0
lose_num = 0
draw_num = 0
total = 0

while(True):
  z = sample([1,2,3],1)
  select_list = ["1. hammer", "2. scissors", "3. paper"]
  print(select_list)
  customer_num = int(input("Select ->"))
  if(customer_num == 1 ):
    print(f"You Select -> {select_list[customer_num-1]}")
    if(z[0] == 1):
      print("draw")
      draw_num += 1
    elif(z[0] == 2):
      print("win")
      win_num += 1
    elif(z[0] == 3):
      print("lose")
      lose_num += 1
    print( f"Bot select -> {select_list[z[0]-1]}")
    total += 1
    
  elif(customer_num == 2 ):
    print(f"You Select -> {select_list[customer_num-1]}")
    if(z[0] == 1):
      print("lose")
      lose_num += 1
    elif(z[0] == 2):
      print("draw")
      draw_num += 1
    elif(z[0] == 3):
      print("win")
      win_num += 1
    print( f"Bot select -> {select_list[z[0]-1]}")
    total += 1
    
  elif(customer_num == 3 ):
    print(f"You Select -> {select_list[customer_num-1]}")
    if(z[0] == 1):
      print("win")
      win_num += 1
    elif(z[0] == 2):
      print("lose")
      lose_num += 1
    elif(z[0] == 3):
      print("draw")
      draw_num += 1
    print( f"Bot select -> {select_list[z[0]-1]}")
    total += 1
    
  else:
      print("Please select 1,2 or 3")
  
  p_again = int(input("Do you want stop now? 1.Yes 2.No ->"))
  if(p_again == 1):
    break
  else:
    print(f"Let's play number:, {total+1}")

total = win_num +lose_num +draw_num
summary = print(f"{user_name} Total: {total}, Win:{win_num}, Lose:{lose_num}, Draw: {draw_num}")
if(total != 0):
    print(summary)
else:
    print("Good bye")
