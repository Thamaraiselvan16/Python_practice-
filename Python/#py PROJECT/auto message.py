import random
import pyautogui
import time

# Words to choose from
words = ("____", "good", "simply")

# Delay to allow you to focus on the input field
time.sleep(5)

# Number of sentences to generate
num_sentences = 20

for _ in range(num_sentences):
    # Select a random word from the words tuple
    random_word = random.choice(words)
    
    # Form a sentence and type it
    sentence = f"you are a {random_word}"
    pyautogui.write(sentence)
    
    # Press Enter to submit the sentence
    pyautogui.press("enter")
    
    # Add a delay between sentences (adjust as needed)
    time.sleep(1)

# Optional: Add a closing message after all sentences are typed
pyautogui.write("All sentences have been typed!")

# Keep the script running to observe the generated sentences
input("Press Enter to exit...")
