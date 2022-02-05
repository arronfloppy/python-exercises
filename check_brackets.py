""" Let's say:

'(', '{', '[' are called "openers."
')', '}', ']' are called "closers."
Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.

Examples:

"{ [ ] ( ) }" should return True
"{ [ ( ] ) }" should return False
"{ [ }" should return False """

def check_brackets(value):
    brackets = "{}[]()"
    br1 = 0
    br2 = 0
    br3 = 0

    prevbracket = ""
    
    for i in range(len(value)):
   
        val = value[i]
        if val not in brackets:
            continue
        elif br1 <0 or br2 < 0 or br3 < 0:
            return False
        elif val == brackets[0]:
            br1 +=1
        elif val == brackets[2]:
            br2 +=1
        elif val == brackets[4]:
            br3 +=1
        elif val == brackets[1]:
            if prevbracket != brackets[0]:
                return False
            else:
                br1 -=1
        elif val == brackets[3]:
           if prevbracket != brackets[2]:
                return False
           else:
                br2 -=1
        elif val == brackets[5]:
            if prevbracket != brackets[4]:
                return False
            else:
                br3 -=1
        prevbracket = val
    return True if br1 == 0 and br2 ==0 and br3 == 0 else False

