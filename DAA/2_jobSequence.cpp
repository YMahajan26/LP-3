#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Job {
    char id;     // Job ID
    int deadline; // Deadline of job
    int profit;   // Profit if job is completed before or on its deadline
};

// Comparator function to sort jobs in descending order of profit
bool compare(Job a, Job b) {
    return a.profit > b.profit;
}

// Function to perform job sequencing with deadlines
pair<vector<char>, int> jobSequencing(vector<Job>& jobs, int maxDeadline) {
    // Sort jobs in descending order of profit
    sort(jobs.begin(), jobs.end(), compare);

    // Array to store the result (sequence of jobs)
    vector<char> result(maxDeadline, '\0');
    vector<bool> slot(maxDeadline, false); // Slot availability

    int totalProfit = 0; // Variable to store total profit

    // Iterate through all sorted jobs
    for (const auto& job : jobs) {
        // Find a free slot for this job, from the last possible slot within deadline
        for (int j = min(maxDeadline - 1, job.deadline - 1); j >= 0; j--) {
            // If the slot is free, assign this job to the slot
            if (!slot[j]) {
                slot[j] = true;
                result[j] = job.id;
                totalProfit += job.profit;
                break;
            }
        }
    }

    // Filter out empty slots and return job sequence and total profit
    vector<char> jobSequence;
    for (char job : result) {
        if (job != '\0') jobSequence.push_back(job);
    }
    return {jobSequence, totalProfit};
}

int main() {
    // List of jobs with job id, deadline, and profit
    vector<Job> jobs = {{'a', 2, 100}, {'b', 1, 19}, {'c', 2, 27}, {'d', 1, 25}, {'e', 3, 15}};
    int maxDeadline = 3;

    // Get the job sequence and maximum profit
    auto [sequence, profit] = jobSequencing(jobs, maxDeadline);

    // Print the result
    cout << "Job Sequence: ";
    for (char job : sequence) cout << job << " ";
    cout << "\nTotal Profit: " << profit << endl;

    return 0;
}
