def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]

def canconstruct(targetString,strings,memo={}):
    if targetString in memo: return memo[targetString]
    if targetString == '':
        return True
    for string in strings:
        if targetString.startswith(string):
            remaining_string=remove_prefix(targetString,string)
            if canconstruct(remaining_string,strings,memo)==True:
                memo[targetString]=True
                return True
    memo[targetString]=False
    return False

print(canconstruct('abcdef',['ab','abc','cd','def','abcd']))
print(canconstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeeee','eeeeeef']))
