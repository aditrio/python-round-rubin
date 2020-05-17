




def findWaitingTime(processes, n, bt, 
						wt, quantum): 
	rem_bt = [0] * n 

	
	for i in range(n): 
		rem_bt[i] = bt[i] 
	t = 0 

	
	
	
	while(1): 
		done = True

		
		
		for i in range(n): 
			
			
			
			if (rem_bt[i] > 0) : 
				done = False 
				
				if (rem_bt[i] > quantum) : 
				
					
					
					t += quantum 

					
					
					rem_bt[i] -= quantum 
				
				
				
				else: 
				
					
					
					t = t + rem_bt[i] 

					
					
					wt[i] = t - bt[i] 

					
					
					rem_bt[i] = 0
				
		
		if (done == True): 
			break
			

def findTurnAroundTime(processes, n, bt, wt, tat): 
	
	
	for i in range(n): 
		tat[i] = bt[i] + wt[i] 




def findavgTime(processes, n, bt, quantum): 
	wt = [0] * n 
	tat = [0] * n 

	
	
	findWaitingTime(processes, n, bt, 
						wt, quantum) 

	
	
	findTurnAroundTime(processes, n, bt, 
								wt, tat) 

	
	print("Processes Burst Time	 Waiting", 
					"Time Turn-Around Time") 
	total_wt = 0
	total_tat = 0
	for i in range(n): 

		total_wt = total_wt + wt[i] 
		total_tat = total_tat + tat[i] 
		print(" ", i + 1, "\t\t", bt[i], 
			"\t\t", wt[i], "\t\t", tat[i]) 

	print("\nAverage waiting time = %.5f "%(total_wt /n) ) 
	print("Average turn around time = %.5f "% (total_tat / n)) 
	

if __name__ =="__main__": 
	
	
    n = int(input("masukan banyak process : "))
    proc = [] 
    burst_time = []   
    for i in range(0,n):
        proc.append(i+1)
        burst_time.append(float(input("burst time : "))) 
        

    quantum = int(input("waktu kuantum : "))

    findavgTime(proc, n, burst_time, quantum) 

# This code is contributed by 
# Shubham Singh(SHUBHAMSINGH10) 
# modified by Aditry