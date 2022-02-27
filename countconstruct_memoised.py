def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]

def countconstruct(targetString,strings,memo={}):
    if targetString in memo: return memo[targetString]
    if targetString =='':
        return 1
    totalcount=0
    for string in strings:
        if targetString.startswith(string):
            nums=countconstruct(remove_prefix(targetString,string),strings,memo)
            totalcount=totalcount+nums
    memo[targetString]=totalcount
    return totalcount
   

print(countconstruct('abcdef',['ab','abc','cd','def','abcd']))
print(countconstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',['e','ee','eee','eeeeef','eeeeeef']))
