import heapq


def solution(jobs):
    
    # 작업의 요청시각, 작업의 소요시간, 작업의 번호를 저장해 두는 대기 큐
    sorted_jobs  = sorted([[req_time, exe_time, job_id] for job_id, (req_time, exe_time) in enumerate(jobs)])
    turnaround_times = [None] * len(jobs)
    queue = []
    time = 0
    job_id = 0
    
    # min heap을 이용해 수행 시간이 짧은 순으로 push, 작업 완료시 바로 다음 작업 수행
    # 작업을 마치자마자 디스크 컨트롤러는 요청이 들어온 작업을 대기 큐에 저장한 뒤 우선순위가 높은 작업을 대기 큐에서 꺼내서 하드디스크에 그 작업 수행
    while None in turnaround_times:
                
        # 현재시간이 요청시간이면, 작업 큐에 작업 추가
        # 작업의 소요시간이 짧은 것, 작업의 요청 시각이 빠른 것, 작업의 번호가 작은 것 순으로 우선순위가 높음
        while job_id < len(sorted_jobs) and sorted_jobs[job_id][0] <= time:
            # 현재 작업의 소요시간, 요청시간, 작업번호
            heapq.heappush(queue, (sorted_jobs[job_id][1], sorted_jobs[job_id][0], job_id))
            job_id += 1
        
        # 작업 수행
        if queue:
            cur_exe_time, cur_req_time, cur_job_id = heapq.heappop(queue)
            time += cur_exe_time # 현재 시간 경과
            turnaround_times[cur_job_id] = time - cur_req_time # 반환 시간 계산
            
        # 대기 큐가 비어있다면 다음 작업의 요청 시간으로 경과
        else:
            time = sorted_jobs[job_id][0]
                
    # 모든 요청 작업의 반환 시간의 평균의 정수부분 return
    return int(sum(turnaround_times)) // len(sorted_jobs)
