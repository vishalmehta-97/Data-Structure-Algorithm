'''Brute Force'''

def mergeintervals(intervals):
    n=len(intervals)
    intervals.sort()
    print(intervals)
    answer=[]

    for i in range(n):
        start=intervals[i][0]
        end=intervals[i][1]
        if len(answer)!=0 and end<=answer[len(answer)-1][1]:
            continue
        for j in range(i+1,n):
            if intervals[j][0]<=end:
                end=max(end,intervals[j][1])
            else:
                break
        answer.append([start,end])
    return answer
        

intervals=[[1,3],[2,6],[8,9],[8,10],[9,11],[15,18],[16,17]]
# print(mergeintervals(intervals))


'''Optimal Approach'''

def mergeintervals(intervals):
    n=len(intervals)
    intervals.sort()
    print(intervals)
    answer=[]
    
    for i in range(n):
        if len(answer)==0 or intervals[i][0]>answer[len(answer)-1][1]:
            answer.append(intervals[i])
        else:
            if intervals[i][0]<=answer[len(answer)-1][1]:
                answer[len(answer)-1][1]=max(intervals[i][1],answer[len(answer)-1][1])
    return answer
        

intervals=[[1,3],[2,6],[8,9],[8,10],[9,11],[15,18],[16,17]]
print(mergeintervals(intervals))