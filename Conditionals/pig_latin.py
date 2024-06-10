def translate(text):
    vowel = ["a","e","h","i","o","u","l","n","y","x"]
    consonant_sound_vowel = ["yt","xr"]
    consonant = ["b","c","d","f","g","j","k","p","q","t","v","s","w","z","x","y","r","m"]
    vowel_sound_consonant = ["ch","th","rh","thr","sch","sc"]
        
    tex=text.split(" ")   
    salida=""
    
    contador = 0
    for i in tex:
        text=i
        #rule1
        contador += 1
        if contador > 1:
            salida+=" "
        if text[0] in vowel:
            if text[0]+text[1] in consonant_sound_vowel:
                salida += text+"ay"
                print("Termina 1")
            elif text[0] in consonant:
                salida += text.replace(text[0],"")+text[0]+"ay"
                print("Termina 2")
            else:
                salida += text+"ay"
            print("Termina 3")
        elif text[0] in consonant:
            if "qu" in text:
                #print("Entre en consonantes")
                if text[1] == "q":
                    #print("Entre en caso 1 de q")
                    salida += text.replace(text[0]+"qu","")+text[0]+"qu"+"ay"
                    print("Termina 4")
                #print("Entre en caso 2 de q")
                else:
                    salida += text.replace("qu","")+"qu"+"ay"
                print("Termina 5")
            elif text[0]+text[1] in vowel_sound_consonant:
                if text[0]+text[1]+text[2] in vowel_sound_consonant:
                    salida += text.replace(text[0]+text[1]+text[2],"")+text[0]+text[1]+text[2]+"ay"  
                    print("Termina 6") 
                else: 
                    salida += text.replace(text[0]+text[1],"")+text[0]+text[1]+"ay"
                print("Termina 7")
            else: 
                salida += text.replace(text[0],"")+text[0]+"ay"
                print("Termina 8")
                        
    return salida