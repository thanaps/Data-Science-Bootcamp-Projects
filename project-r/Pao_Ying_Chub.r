print("Condition of Pao Ying Chub")
user <- c("hammer", "scissors", "paper")
bot <- c("hammer", "scissors", "paper")
results <- c("draw","lose","win",
             "win","draw","lose",
             "lose","win","draw")
y <- merge(user,bot)    # from google
result_table <- data.frame(y,results)
names(result_table)[1] <- "user"
names(result_table)[2] <- "bot"
print(result_table)

user_name <- readline("What's your name? ->") 
print( paste("Hi", user_name))
win_num <- 0
lose_num <- 0
draw_num <- 0
total <- 0

#while(TRUE){
#  print("R u ready !!!")
# decision <- as.numeric(readline("1.Yes 2.No ->"))
#  if(decision == 1){

while(TRUE){
  
  select_list <- c("hammer", "scissors", "paper")
  select_df <- data.frame(select_list)
  print(select_df)
  customer_num <- as.numeric(readline("Select ->"))
  z <- sample(1:3 , 1)
  
  if(customer_num == 1 ){
    print( paste("You Select ->", select_list[[customer_num]]))
    if(z == 1){
      print("draw")
      draw_num <- draw_num + 1
    }else if(z == 2){
      print("win")
      win_num <- win_num + 1
    }else if(z == 3){
      print("lose")
      lose_num <- lose_num + 1
    }
    print( paste("Bot select ->",bot[z]))
    total <- total + 1
    
  }else if(customer_num == 2 ){
    print( paste("You Select ->", select_list[[customer_num]]))
    if(z == 1){
      print("lose")
      lose_num <- lose_num + 1
    }else if(z == 2){
      print("draw")
      draw_num <- draw_num + 1
    }else if(z == 3){
      print("win")
      win_num <- win_num + 1
    }
    print( paste("Bot select ->",bot[z]))
    total <- total + 1
    
  }else if(customer_num == 3 ){
    print( paste("You Select ->", select_list[[customer_num]]))
    if(z == 1){
      print("win")
      win_num <- win_num + 1
    }else if(z == 2){
      print("lose")
      lose_num <- lose_num + 1
    }else if(z == 3){
      print("draw")
      draw_num <- draw_num + 1
    }
    print( paste("Bot select ->",bot[z]))
    total <- total + 1
    
  }else(print("Please select 1,2 or 3"))
  
  p_again <- as.numeric(readline("Do you want stop now? 1.Yes 2.No ->"))
  if(p_again == 1){
    break
  }else(
    print(paste("Let's play number:", total+1))
    )
  
}

total <- win_num+lose_num+draw_num
summary <- data.frame(user_name,
                      win_num,
                      lose_num,
                      draw_num,
                      total)
if(total != 0){
  print(summary)
}else(print("Good bye"))
