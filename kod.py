meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap", 
            "FAFOAIFA": "gülmenin kolay yolu",
            "NT": "nice try"
                }
word = input("Anlamadığınız bir kelime yazın  ").upper()
if word in meme_dict.keys():
    print(meme_dict[word])
else:
        print("malesef bilmiyorum")
