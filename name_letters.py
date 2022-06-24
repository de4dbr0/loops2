syllables = 'aeiou'
silent_letters= 'qwrtypsdfghjklzxcvbnm'

word = input("enter your name: ")
word = word.casefold()


syllable_count = {}.fromkeys(syllables,0)
silent_letters_count = {}.fromkeys(silent_letters,0)

for w in word:
   if w in syllable_count:
       syllable_count[w] += 1
for w in word:
   if w in silent_letters_count:
       silent_letters_count[w] += 1

print(syllable_count)
print(silent_letters_count)