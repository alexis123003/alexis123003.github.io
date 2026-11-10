English = input("Input a sentence to turn it into pig latin:")
#In one version, to convert a word to Pig Latin, you remove the first letter and place that letter at the end of the word. Then, you append the string “ay” to the word. Here is an example:

#English:	I SLEPT MOST OF THE NIGHT
#Pig Latin:	IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY
if len(English) == 1:
    PigLatin = English + "ay"
    print(PigLatin.title())
else:
    PigLatin = ""
    for word in English.split():
        PigLatin += word[1:] + word[0] + "ay "
    print(PigLatin)