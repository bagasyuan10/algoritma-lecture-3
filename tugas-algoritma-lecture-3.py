answer = input("greeting, can i help you : ").lower().strip()
if "hello" in answer :
    print ("$0")
elif answer == "how you doing?":
    print("$20")
elif answer == "what's happening?":
    print ("$100")
else:
    print("try again")