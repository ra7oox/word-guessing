#Ra7oox

list_word=["car","nike","hungry","python","happy","big","fast"]

score=0
pt="."
def main():
    for i in list_word:
    
    
    
        ask=str(input(f"complete the word: {i[0:int(len(i)/2)+1:1]}{pt*(int(len(i)/2)-1)} "))
        if ask==i:
            score=score+1
        
        
    print(f"your score is:{score}")
    
if __name__=="__main__":
    main()
    
