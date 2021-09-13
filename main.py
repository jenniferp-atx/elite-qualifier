import random

greetings = random.choice(["Hello there, who are you?", "Who are you?", "What's your name?", "Hello, what's your name?",])

name = input(f"{greetings} \n")
print(f"Hello {name}.")

# from stack overflow https://stackoverflow.com/questions/29463078/how-to-programmatically-detect-and-respond-to-a-key-words-in-chat-messages

goodbye_responses = random.choice(["Bye!", "Bye.", "Goodbye.", "Bye bye.", "See you later.", "Adios!"])

reassurance_responses = random.choices(["Think better of yourself.", "Stop it.", "You're fine.", "Quit thinking like that.",])

thoughts_on_topics = random.choices(["I'm not really sure.", "I'm not fluent in this topic.", "I've never heard of this.", "I think that is fine." "It's okay."])

# from https://betterprogramming.pub/how-to-indefinitely-request-user-input-until-valid-in-python-388a7c85aa6e

while True:
  try:
    response = input("What's up? \n")
    if "what are you" in response:
      print("I'm a chatbot.")
    elif "how are you" in response:
      print("I am fine.")
    elif "life" in response:
      print("I don't think you should talk about life with something that isn't alive.")
    elif "address" in response:
      print("I will not help you search for people.")
    elif "think about" in response:
      print(f"{thoughts_on_topics}")
    elif "help" in response:
      help_request = input("What do you need help with? \n")
      if "bot" in help_request:
        print("This might help you: https://stackoverflow.com/questions/29463078/how-to-programmatically-detect-and-respond-to-a-key-words-in-chat-messages")
      elif "math" in help_request:
        print("You might want a calculator rather than me.")
      elif "school" in help_request:
        print("I am not your teacher.")
      elif "game" in help_request:
        print("I don't play games.")
      else:
        print("I can't help you.")
    if response == "bye":
      print(f"{goodbye_responses}")
      break
    else:
      print("I don't know.")
  except Exception as e:
    print(e)
    