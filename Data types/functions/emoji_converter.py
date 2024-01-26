#A reusable function 
def emoji_converter(message):
    words=message.split(" ")
    emojis={
        ":)":"😉️",
        ":(":"😔"
    }
    Output=""
    for word in words:
        Output += emojis.get(word, word) + " "
    return Output   #Removes the trailing space

message=input(">")
print(emoji_converter(message))