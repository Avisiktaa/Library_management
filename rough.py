#THIS FILE IS FOR ROUGH, SOMETHING TO DO EXPERIMENT
# ALSO WE CAN DO IT ON TERMINAL, JUST WRITING py

from datetime import datetime
def id_g(name,role,obj):
    year = datetime.now().year % 100
    name_word = name.split()
    letter = name_word[0][0] + name_word[-1][0]
    prefix = str(year) + letter + role 
    
    if obj:
        return f"{prefix}{obj+1}"
    
    return prefix+"0"


a=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
   'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
   'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
   'u', 'v', 'w', 'x', 'y', 'z']

def idg(id): #1679616
    new = list(id)
    i = 3
    while i >= 0:
        if new[i] == "z":
            new[i] = a[0]
            i -= 1
        else:
            idx = a.index(new[i])
            idx += 1
            new[i] = a[idx]
            break
    
    return "".join(new)

print(idg("1bzz"))

#useful function
def id_g(cls,name,role):
    year = datetime.now().year % 100
    name_word = name.split()
    letter = name_word[0][0] + name_word[-1][0]
    prefix = str(year) + letter + role
    obj = cls.query.filter(cls.id.like(f"{prefix}%")).order_by(cls.id).first()
    
    if obj:
        last = obj.id[-1] #not always, exception for more digit number
        return f"{prefix}{int(last)+1}"
    
    return prefix+"0"




        