
def frequency_counter():
  print("\n--- Input the sentence ---")
  sentence = input("Enter sentence or paragraph: ").lower()
  words = sentence.split()
  word_count = {}
  
  # loop through splited words
  for w in words:
    # check if word exist in the dictionary, if so, increment to 1
    if w in word_count:
      word_count[w] += 1
    
    # if not which is first time to count, then simply place 1
    else:
      word_count[w] = 1
  
  print(word_count)
  return word_count

# Call the function
frequency_counter()

"""
  Set 1: Simple Sentences

“Rain fell softly while the city slowly woke up.”

“The cat chased the butterfly across the garden.”

“Bright stars filled the sky above the quiet town.”

“She found a hidden key under the old wooden chair.”
  
"""