def coscc_passwdgen(password_length,passwords_needed):
    if password_length <= 7:
        print('Password Length must be 8 or more characters long.')
    else:   
        import random as random
        for i in range(passwords_needed):
            passwdlen = password_length
            numbers = ['0','1','2','3','4','5','6','7','8','9']
            upperletters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
            lowerletters = [x.lower() for x in upperletters]
            allletters = upperletters + lowerletters
            specialcase = ['!','#','-','_','+','=','^','~',':']
            allcharacters = allletters + specialcase
            countletters = len(upperletters)
            countnumbers = len(numbers)
            countallletters = len(allletters)
            countspecialcase = len(specialcase)
            countallcharacters = len(allcharacters)
 
            pos = random.randint(0,countletters - 1)
            uletter = upperletters[pos]
            pos = random.randint(0,countletters - 1)
            lletter = lowerletters[pos]
            pos = random.randint(0,countspecialcase - 1)
            schar = specialcase[pos]
            pos = random.randint(0,countnumbers - 1)
            numb = numbers[pos]
            reqchars = [uletter,lletter,numb,schar]
 
            rchars = []
            for i in range(passwdlen - 4):
                rchars.append(random.randint(0,countallcharacters - 1))
 
            passvar = []
            for i in range(passwdlen - 4):
                passvar.append(allcharacters[rchars[i]])
                i += 1
 
            passwordarray = reqchars + passvar
            random.shuffle(passwordarray)
            password = ''.join(passwordarray)
            print(password)
