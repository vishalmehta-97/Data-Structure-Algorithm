'''Brute Force Approach'''

def minimize_Max_Distance_to_Gas_Station(stations,k):
    arr=[0]*((len(stations))-1)

    if len(stations)<=1:
        return 0

    for _ in range(k):
        dist_max=-1
        max_index=-1
        for i in range(len(stations)-1):
            diff=stations[i+1]-stations[i]
            
            section_length=diff/(arr[i]+1)
            
            if dist_max<section_length:
                dist_max=section_length
                max_index=i

        arr[max_index]+=1

    max_ans=-1
    for i in range(len(stations)-1):
        diff=stations[i+1]-stations[i]
        ans=diff/(arr[i]+1)
        max_ans=max(max_ans,ans)

    return max_ans


stations=[1,13,17,23]
k=5
stations=[13]
k=1
# print(minimize_Max_Distance_to_Gas_Station(stations,k))


''' Better Approach '''

import heapq
def minimize_Max_Distance_to_Gas_Station_(stations,k):

    if len(stations)<=1:
        return 0
    
    heap=[]
    for i in range(len(stations)-1):
        diff=stations[i+1]-stations[i]
        heapq.heappush(heap,(-diff,i))  # we have used this - sign in here to get the max value in the first to order to solve this problem
    
    how_many=[0]*((len(stations))-1)

    for _ in range(k):
        distance,index=heapq.heappop(heap)
        dist=stations[index+1]-stations[index]

        how_many[index]+=1
        section_len=dist/((how_many[index])+1)
        heapq.heappush(heap,(-section_len,index))

    # distance,index=heapq.heappop(heap)
    # distance=-distance

    ans=heap[0][0]  ## this is the way to get the top of the priority queue in pairs
    return -ans

stations=[1,13,17,23]
k=5
# print(minimize_Max_Distance_to_Gas_Station_(stations,k))


'''
Time Complexity= NlogN+ klogN
Space Complexity= 0(N-1)
'''


''' Optimal Approach '''

def check_stations(stations,mid):
    count=0

    for i in range(1,len(stations)):
        total_gap=int((stations[i]-stations[i-1])/mid)
        if (stations[i]-stations[i-1])==total_gap*mid:
            total_gap-=1

        count+=total_gap
    
    return count

def minimize_Max_Distance_to_Gas_Station_opt(stations,k):
    if len(stations)<=1:
        return 0
    
    low=0
    high=-1
    for i in range(len(stations)-1):
        high=max(high,stations[i+1]-stations[i])

    while(high-low)>1e-6:
        mid=(low+high)/2.0
        count=check_stations(stations,mid)
        if count<=k:
            high=mid
        else:
            low=mid

    return high   ## here the high polarity concept will not work

stations=[1,13,17,23]
k=5
# stations=[13]
# k=1
print(minimize_Max_Distance_to_Gas_Station_opt(stations,k))