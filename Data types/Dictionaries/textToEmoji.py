message=input("> ")
words=message.split(' ')
emojis={
    ":)":"😉️",
    ":(":"😔"
}
Output=""
for word in words:
    Output += emojis.get(word, word) + " "

print(Output)