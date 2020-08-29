def run_time()-> None:
    """Returns the average time a user used in running """
    total_time = 0 
    number_runs = 0

    while True:
        one_run = float(input('Enter 10 km run time:'))
            
        if not one_run :
            break
            
        number_runs += 1
        total_time += one_run
    
    average_time = float(total_time)/float(number_runs)
    print(f'Average of {average_time}, over {number_runs} runs')
run_time()

