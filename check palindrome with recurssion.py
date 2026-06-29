def func(word,left,right):
    if left>=right:
        return True
    if word[left]!=word[right]:
        return False
    return func(word,left+1,right-1)
word=input("enter a word:")
print(func(list(word),0,len(list(word))-1))
        
