# Büyük küçük harf çevirici

def ConvertSig(text):
    words = text.split(" ")
    
    i = 0
    sigedWords = []
    for word in words:
        sigedLetters = ""
        for letter in word:
            if i % 2 == 0:
                sigedLetters += letter.upper();
            else:
                sigedLetters += letter.lower();
            i += 1
        sigedWords.append(sigedLetters)

    sigedText = ""
    for sigedWord in sigedWords:
        sigedText += (sigedWord + " ")

    sigedText = sigedText.replace("I", "İ")

    return sigedText


text = input("Enter text to sig: ")
print()
print(ConvertSig(text))