
def check_brackets(value):
    """ Let's say:
    '(', '{', '[' are called "openers."
    ')', '}', ']' are called "closers."
    Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.
    Examples:
    "{ [ ] ( ) }" should return True
    "{ [ ( ] ) }" should return False
    "{ [ }" should return False """

    brOpen = "{[("
    brClose = "}])"
    brackets = brOpen + brClose
    checkSubstr = True

    # empty string return True
    if not value:
        return True
    elif len(value) == 1:
        # one length string
        if value in brackets:
            return False
        else:
            return True
    else:
        idxOpen = -1
        idxClose = -1
        openBr = ""
        closedBr = ""
        for i in range(len(value)):
            if value[i] in brOpen:
                idxOpen = i
                openBr = value[i]
                break
        if  idxOpen == len(value) - 1:
            return False
        if idxOpen == -1: 
            if value.find(brClose[0]) != -1 or value.find(brClose[1]) != -1 or value.find(brClose[2]) != -1:
                return False
            else:
                return True
        
        # found open bracket, check the closing one
        idxo = brOpen.find(openBr)
        closedBr = brClose[idxo]
        # find closed bracket index
        idxClose = value.rfind(closedBr)
        if idxClose < idxOpen:
            # not found or something wrong 
            return False
        # check the string between brackets
        checkSubstr = check_brackets(value[idxOpen + 1:idxClose ])

        # check the end of the string
        if idxClose < len(value) - 1:
            checkSubstr &= check_brackets(value[idxClose+1:])
            
    return checkSubstr


def check_brackets2(value):
    """ Let's say:
    '(', '{', '[' are called "openers."
    ')', '}', ']' are called "closers."
    Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.
    Examples:
    "{ [ ] ( ) }" should return True
    "{ [ ( ] ) }" should return False
    "{ [ }" should return False """

    brOpen = "{[("
    brClose = "}])"
    brackets = brOpen + brClose

    # empty string return True
    if not value:
        return True
    elif len(value) == 1:
        # one length string
        if value in brackets:
            return False
        else:
            return True
    else:
        bracketsin = ""

        for i in range(len(value)):
            if value[i] in brClose:
                closeBrIdx = brClose.index(value[i])
                openBr = brOpen[closeBrIdx]

                lastBracket = bracketsin[-1] if len(bracketsin) else None
                if openBr == lastBracket:
                    bracketsin = bracketsin[0:-1]
                else: 
                    return False
            elif value[i] in brOpen:
                bracketsin += value[i]

    return True if len(bracketsin) == 0 else False
                
