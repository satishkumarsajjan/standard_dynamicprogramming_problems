def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]

def canconstruct(targetString,strings):
    if targetString == '':
        return True
    for string in strings:
        if targetString.startswith(string):
            remaining_string=remove_prefix(targetString,string)
            if canconstruct(remaining_string,strings)==True:
                return True
    return False

print(canconstruct('abcdef',['ab','abc','cd','def','abcd']))
print(canconstruct('eef',['e','ef']))
