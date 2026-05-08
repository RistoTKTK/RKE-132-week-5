# Kirjutage programm, mis käib läbi iga tähe sõnes ja prindib selle välja.

text = "C#"

"""  for i in text:
    print(i) """

# Prindi sõne tagurpidi (viimasest tähemärgist esimese tähemärgini, iga täht sõnast kuvatakse eraldi reale, tagurpidi järjekorras).

length = len(text)
print (length)

for letter in range(len(text)-1, -1, -1):
    print(text[letter])