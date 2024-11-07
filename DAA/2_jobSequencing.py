class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs, max_deadline):
    # Step 1: Sort jobs by descending order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Step 2: Initialize result and slot availability
    result = [None] * max_deadline  # Array to store result (job sequence)
    slot = [False] * max_deadline    # Array to track if slot is free

    total_profit = 0  # To calculate total profit

    # Step 3: Iterate through all sorted jobs
    for job in jobs:
        # Find a free slot for this job, within its deadline limit
        for j in range(min(max_deadline - 1, job.deadline - 1), -1, -1):
            # If the slot is free, assign this job to the slot
            if not slot[j]:
                slot[j] = True
                result[j] = job.id
                total_profit += job.profit
                break

    # Display job sequence and total profit
    job_sequence = [job_id for job_id in result if job_id is not None]
    return job_sequence, total_profit

# Example usage
jobs = [
    Job('a', 3, 35),
    Job('b', 4, 30),
    Job('c', 4, 25),
    Job('d', 2, 20),
    Job('e', 3, 15)
]
max_deadline = 4
sequence, profit = job_sequencing(jobs, max_deadline)

print("Job Sequence:", sequence)
print("Total Profit:", profit)
