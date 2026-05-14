def scoreValidator(events):
    counter=0
    score=0
    total_elem=[]
    for i in range(len(events)):
        if events[i]=="W":
            counter+=1
        elif events[i] == "WD" or events[i] == "NB":
            score+=1
        else:
            sc=int(events[i])
            score+=sc
            

    total_elem.append(score)
    total_elem.append(counter)

    return total_elem

events=["W","W","W","W","W","W","W","W","W","W","W"]
# print(scoreValidator(events))

