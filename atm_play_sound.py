from playsound import playsound

print("\nPress 1 for Hindi\n2 for English\n3 for Gujarati")
ch=int(input("Select Language = "))

def play_audio(fnm):
    playsound(fnm)

    
play_audio("welcome.mp3")
print("Press1.Sign Up")
print("Press2.Sign In")
print("Press3.Exit")
play_audio("menu.mp3")
play_audio("enter_choice.mp3")
ch=int(input("Enter Your Choice = "))

