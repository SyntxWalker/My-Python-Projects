import random

User = input("May I know your name please?\nEnter your name here: ")
print(f"Hello {User}! Welcome to The Fortune Teller.")
Choice = int(input("How do you feeling right now ?\nHappy = 1\nSad = 2\nAdventurous = 3\nEnter the value here : "))

Happy_List = [f"Ah, hey {User}! I see your joy is shining today. The spirits whisper: “A small compliment you give will return to you tenfold.”",f"Greetings, {User}! Your laughter echoes brightly. The signs reveal: “An unexpected sweet moment will find you before the day ends.”",f"Well met, {User}. Your happiness stirs the air. The fortune reads: “Something you once wished for is quietly making its way toward you.”"]
Sad_List = [f"Ah, {User}… The clouds linger gently around you. The spirits say: “This heaviness will water a hidden strength within you.”", f"Welcome, {User}. I sense a quiet heart today. The message reveals: “A comforting word will arrive just when you need it.”", f"Dear {User}, even shadows carry meaning. The fortune speaks softly: “What feels like an ending is quietly becoming a beginning.”"]
Advntrs_List = [f"Ah, welcome {User}! I see the spark of adventure in your eyes. The spirits declare: “A bold step today will open a door you did not know existed.”", f"Greetings, brave {User}. The winds are shifting in your favor. The fortune reads: “Follow your curiosity - it knows the shortcut.”", f"Well met, {User}. Your restless spirit hums loudly. The signs reveal: “A detour will lead you to something far better than the plan.”"]



if Choice == 1:
    print(random.choice(Happy_List))
elif Choice == 2:
    print(random.choice(Sad_List))
elif Choice == 3:
    print(random.choice(Advntrs_List))
else:
    print("A valid value number is been expected.")