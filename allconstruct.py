from unittest import result


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]

def countconstruct(targetString,strings):
    if targetString =='':
        return [[]]
    resultt=[]
    for string in strings:
        if targetString.startswith(string):
            suffix_ways=countconstruct(remove_prefix(targetString,string),strings)
            target_ways=[[string]+way for way in suffix_ways]
            resultt.extend(target_ways)
    return resultt

print(countconstruct('abcdef',['ab','abc','cd','def','abcd']))
print(countconstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeeee','eeeeee']))
