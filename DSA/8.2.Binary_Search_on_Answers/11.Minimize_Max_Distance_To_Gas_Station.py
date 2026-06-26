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
print(minimize_Max_Distance_to_Gas_Station(stations,k))


''' Better Approach '''

def minimize_Max_Distance_to_Gas_Station_(stations,k):
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
print(minimize_Max_Distance_to_Gas_Station_(stations,k))
