from datetime import datetime
def id_g(name,role,obj):
    year = datetime.now().year % 100
    name_word = name.split()
    letter = name_word[0][0] + name_word[-1][0]
    prefix = str(year) + letter + role 
    
    if obj:
        return f"{prefix}{obj+1}"
    
    return prefix+"0"


print(id_g("Biswayan Biman Mal","S",None))