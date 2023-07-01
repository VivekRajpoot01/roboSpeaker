import pyttsx3

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print("Hey, Welcome to this Robo Speaker 1.0")
    sx = input("Enter the text: ")
    say(f"{sx}")

# use 'pip install pyttsx3' in the terminal
