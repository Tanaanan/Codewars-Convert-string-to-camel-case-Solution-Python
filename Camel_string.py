text = "the_pippi_pas_pippi" #testcase

def to_camel_case(text):
    if "-" in text:
        Camel_text = text.split("-") 
    elif "_" in text:
        Camel_text = text.split("_") 
    else:
        return text

    Basedtext = Camel_text[0] #text[0] don't change
    Camel_text.remove(Camel_text[0]) 

    List_result = []

    for word in Camel_text:
        if word[0].isupper():
            List_result.append(word)
        else:
            List_result.append(word[0].upper()+word[1:])

    result = ("").join(List_result) 
    result = Basedtext+result
    
    return to_camel_case(result) #double check when method have "-" and "_"
    

to_camel_case(text)
