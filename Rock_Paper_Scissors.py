import random
choice1 = input('"rock", "paper", or "scissors"? ')
if choice1 == "rock": 
    print ('''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
           ''')
elif choice1 == "paper":
    print('''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|              
          ''')
else:
    print('''
                d8b                                        
                Y8P                                        
                                                           
.d8888b  .d8888b888.d8888b .d8888b  .d88b. 888d888.d8888b  
88K     d88P"   88888K     88K     d88""88b888P"  88K      
"Y8888b.888     888"Y8888b."Y8888b.888  888888    "Y8888b. 
     X88Y88b.   888     X88     X88Y88..88P888         X88 
 88888P' "Y8888P888 88888P' 88888P' "Y88P" 888     88888P' 
          ''')
    
rock = ('''
                _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
              ''')
paper = ('''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|   
''')
scissors = ('''
                d8b                                        
                Y8P                                        
                                                           
.d8888b  .d8888b888.d8888b .d8888b  .d88b. 888d888.d8888b  
88K     d88P"   88888K     88K     d88""88b888P"  88K      
"Y8888b.888     888"Y8888b."Y8888b.888  888888    "Y8888b. 
     X88Y88b.   888     X88     X88Y88..88P888         X88 
 88888P' "Y8888P888 88888P' 88888P' "Y88P" 888     88888P' 
''')
gen = [rock, paper, scissors]
aimove = random.choice(gen)
print (aimove)

if choice1 == "rock" and aimove == scissors:
    print ("You win!")
elif choice1 == "rock" and aimove == rock:
    print ("Its a draw!")
elif choice1 == "rock" and aimove == paper:
    print("You Lose.")
elif choice1 == "scissors" and aimove == paper:
    print ("You win!") 
elif choice1 == "scissors" and aimove == scissors:
    print("It's a draw!")
elif choice1 == "scissors" and aimove == rock:
    print("You lose.")
elif choice1 == "paper" and aimove == rock:
    print("You win!")
elif choice1 == "paper" and aimove == paper:
    print("It's a draw")
elif choice1 == "paper" and aimove == scissors:
    print("You lose.")