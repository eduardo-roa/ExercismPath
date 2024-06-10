def response(hey_bob):
    hey_bob = hey_bob.strip()
    
    #verify if the string is empty
    if not hey_bob:
        return "Fine. Be that way!"

    #string is question
    elif hey_bob[-1] == '?':
        #if string is question and is in upper case
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        else: 
            return "Sure."
    #string is in upper case
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."
