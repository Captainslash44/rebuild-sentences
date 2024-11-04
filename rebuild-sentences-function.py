def Rebuild_sentences(words, lengths):
    new_words = []

    for i in range(len(words)):
        temp_word = ""

        for j in range(lengths[i]):
            temp_word += words[i][j]

        new_words.append(temp_word)

    return new_words



words = []
lengths = []

while True:

    WORD = input("Please enter words for words list, or type a number to enter lengths: ")

    if WORD.isdigit():
        break
    
    else:
        words.append(WORD)

for i in range(len(words)):
    LENGTH = int(input("Please enter the lengths(integers): "))
    lengths.append(LENGTH)


print(f"""original lists: words: {words}, lengths: {lengths}""")

print(f"New words: {Rebuild_sentences(words, lengths)}")