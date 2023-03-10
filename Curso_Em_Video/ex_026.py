phrase = str(input('Escreva uma frase: ')).strip().lower()
count_phrase = phrase.count('a')
print(f'A letra "A" aparece {count_phrase} vezes')

find_phrase = phrase.find('a') + 1
print(f'A letra "A" aparece pela primeira vez na {find_phrase}° posição')

rfind_phrase = phrase.rfind('a') + 1
print(f'A letra "A" aparece pela última vez na {rfind_phrase}° posição')
