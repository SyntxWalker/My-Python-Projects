User = str(input("Enter your name : "))
Age = int(input("Enter your age : "))

if Age >= 18:
    print(f"Congratulations! {User}, You can play this game.\nHere's your pass-code: 999666")
else:
    print(f"Hey {User}, You have to figure out your pass code. Good Luck!")

PassCode = int(input("Enter your pass-code:"))

if PassCode == 999666:
    print("Unlocked!")
    print('''
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢯⠙⠩⠀⡇⠊⠽⢖⠆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠱⣠⠀⢁⣄⠔⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣷⣶⣾⣾⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡔⠙⠈⢱⡟⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡠⠊⠀⠀⣀⡀⠀⠘⠕⢄⠀⠀⠀⠀⠀
⠀⠀⠀⢀⠞⠀⠀⢀⣠⣿⣧⣀⠀⠀⢄⠱⡀⠀⠀⠀
⠀⠀⡰⠃⠀⠀⢠⣿⠿⣿⡟⢿⣷⡄⠀⠑⢜⢆⠀⠀
⠀⢰⠁⠀⠀⠀⠸⣿⣦⣿⡇⠀⠛⠋⠀⠨⡐⢍⢆⠀
⠀⡇⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣦⡀⠀⢀⠨⡒⠙⡄
⢠⠁⡀⠀⠀⠀⣤⡀⠀⣿⡇⢈⣿⡷⠀⠠⢕⠢⠁⡇
⠸⠀⡕⠀⠀⠀⢻⣿⣶⣿⣷⣾⡿⠁⠀⠨⣐⠨⢀⠃
⠀⠣⣩⠘⠀⠀⠀⠈⠙⣿⡏⠁⠀⢀⠠⢁⡂⢉⠎⠀
⠀⠀⠈⠓⠬⢀⣀⠀⠀⠈⠀⠀⠀⢐⣬⠴⠒⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀
          ''')
    print('''
           _____        _  _  _  _                       _            
/__   \ _ __ (_)| || |(_)  ___   _ __    __ _ (_) _ __  ___ 
  / /\/| '__|| || || || | / _ \ | '_ \  / _` || || '__|/ _ \
 / /   | |   | || || || || (_) || | | || (_| || || |  |  __/
 \/___ |_|   |_||_||_||_| \___/ |_| |_| \__,_||_||_|   \___|
/__   \ _   _   ___  ___    ___   _ __                      
  / /\/| | | | / __|/ _ \  / _ \ | '_ \                     
 / /   | |_| || (__| (_) || (_) || | | |                    
 \/     \__, | \___|\___/  \___/ |_| |_|                    
        |___/                                               
          
          ''')
    Will = str(input(f"{User}, Do you want to make money ? (y / n)\n "))
    if Will == "y":
        print("You got $1000 to start.\nBALANCE: $1000.00")
        Ready = str(input("Are you ready ? (y / n)\n"))
        if Ready == "y":
            print(f"Yo! {User}, you got a call from your friend. He's asking $500 to fund a start-up.")
            Pay500F = str(input("Pay $500 ? (y / n)\n"))
            if Pay500F == "y":
                print("You made $45000!\nBALANCE: $45000.00")
                CCoin = str(input("You put all your money in a CryptoCoin. Within next 5 min, is it going up or down? (y = up, n = down)\n"))
                if CCoin == "y":
                    print("You just made $500000!\nBALANCE: $500,000.00")
                    TESLA = str(input(f"Hey {User}, You got a mail from Elon Musk, asking you to pay $500K to make $10 Million. Do you want to pay? (y / n)\n"))
                    if TESLA == "n":
                        print("You saved yourself from being scammed.\nBALANCE: $500,000.00")
                        Pill = int(input(f"Listen up {User}! You got a golden opportunity to choose between 3 Pills.\n1. RED PILL\n2. BLUE PILL\n3. BLACK PILL\nOne of this pill can get you $1000000000000 & Each pill will cost you $500K.\nWhich one are you choosing?\nEnter your pill number: "))
                        if Pill == 1:
                            print(f"CONGRATULATIONS {User}!\nYou just won the game and made $1 Trillion.\nBALANCE:$1,000,000,000,000.00\nThanks for playing! Have a great day {User}.")
                        else:
                            print("You've chosen the wrong one. And lost all your money.\nBALANCE: $0.00\nNow you are broke.\nGAME OVER.")
                    else:
                        print("You just been scammed.\nBALANCE: $0.00\nGAME OVER.")
                else:
                    print("You lost all your money. Now you are broke. GAME OVER.\nBALANCE: $0.00")
            else:
                print("Your friend hired a hitman and whacked you!\nGAME OVER.")    
    else:
        print("Then Go Back.")
    
else:
    print("Invalid Pass-Code. You Can't play.")