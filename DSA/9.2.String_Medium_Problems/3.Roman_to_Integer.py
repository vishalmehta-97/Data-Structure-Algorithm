''' Optimal Approach '''

def roamnToInt(s):
    hash={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    print(hash)
    total=0
    for i in range(len(s)-1):
        curr_elem=hash.get(s[i])
        next_elem=hash.get(s[i+1])

        if curr_elem>=next_elem:
            total+=curr_elem
        elif next_elem>curr_elem:
            total-=curr_elem
        
    total+=hash.get(s[len(s)-1])

    return total
    
        

s='III'
s='LVIII'
s='MCMXCIV'
print(roamnToInt(s))