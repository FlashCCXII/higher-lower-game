import random
from art import logo, vs
from game_data import data
from replit import clear

def game():
  print(logo)
  score = 0
  should_continue = True
  
  choice2 = random.choice(data)
  
  while should_continue:
    choice1 = choice2
    choice2 = random.choice(data)
  
    while choice1 == choice2:
      choice2 = random.choice(data)
    
    def format_data(account):
      account_name = account["name"]
      account_descr = account["description"]
      account_country = account["country"]
      return f"{account_name}, a {account_descr}, from {account_country}"
    
    def check_answer(guess, value1, value2):
      if value1 > value2:
        return guess == "a"
      else:
        return guess == "b"
        
    print(f"Compare A: {format_data(choice1)}")
    print(vs)
    print(f"Against B: {format_data(choice2)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    value1 = choice1["follower_count"]
    value2 = choice2["follower_count"]
    
    is_correct = check_answer(guess, value1, value2)
    
    clear()
    
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}")
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      play_again = input("Play again? Y or N: ").lower()
      if play_again == "y":
        return game()
      else:
        print("Thanks for playing!")
        should_continue = False

game()