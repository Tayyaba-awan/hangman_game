import random
import hangman_words

print(hangman_words.logo)
chosen_word=random.choice(hangman_words.word_list)
lives=6
print(chosen_word)
blanks=[]
for letter in chosen_word:
    blanks+="_"
end_of_the_game=False
while not end_of_the_game:
    user_guess=input("guess the letter:").lower()
    # clear()
    if user_guess in blanks:
       print(f"{user_guess} you have already guessed")
    for position in range(len(chosen_word)):
            letter=chosen_word[position]
            if letter==user_guess:
                blanks[position]=letter
    if user_guess not in chosen_word:
      lives-=1
      print(f"{user_guess} is not in the word")
      if lives==0:
       end_of_the_game=True
       print("you lose")
    print(f"{' '.join(blanks)}")
    if "_" not in blanks:
        end_of_the_game=True
        print("you win")
    print(hangman_words.stages[lives])