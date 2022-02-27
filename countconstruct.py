def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]

def countconstruct(targetString,strings):
    if targetString =='':
        return 1
    totalcount=0
    for string in strings:
        if targetString.startswith(string):
            nums=countconstruct(remove_prefix(targetString,string),strings)
            totalcount=totalcount+nums

    return totalcount
   

print(countconstruct('abcdef',['ab','abc','cd','def','abcd']))
print(countconstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeeee','eeeeee']))
