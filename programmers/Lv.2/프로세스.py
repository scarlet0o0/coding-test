def solution(priorities, location):
    
    ### priorities -> 중요도 
    answer = 0
    
    max_index = priorities.index(max(priorities)) # 중요도가 가장 큰 값의 인덱스를 구함.

    while True: 
        
        i = max(priorities) # 현재 중요도 리스트에서 가장 큰 값
        
        if priorities[max_index] == i: # priorities에서 max_index 위치에 있는 값이 i랑 같다면 
            priorities[max_index] = 0 # 프로세스를 실행하고 0으로 만든다. 
            answer += 1 # 프로세스가 하나 실행되었으므로 += 1
            
        
            if max_index == location: # 실행시킨 프로세스의 인덱스와 찾으려고 하는 프로세스 인덱스(location)가 동일하면 반복문 종료 
                break
        max_index += 1 # priorities 리스트를 계속 탐색 
        
        if max_index >= len(priorities): # priorities에서 가장 큰 값을 가지는 인덱스가 priorities 길이를 넘어가면 
            max_index = 0 # max_index를 0으로 초기화, 0번째 인덱스부터 다시 탐색 
        
    
    
        
    return answer