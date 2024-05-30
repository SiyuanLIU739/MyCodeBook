class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_task = {}
        max_task = 0
        count_max = 0

        for task in tasks:
            if(task not in count_task.keys()):
                count_task[task] = 0

            count_task[task] += 1

            if(count_task[task] > max_task):
                max_task = count_task[task]
                count_max = 1

            elif (count_task[task] == max_task):
                count_max += 1

        sum_tasks = 0
        for key, value in count_task.items():
            sum_tasks += value

        if(n < count_max):
            return sum_tasks

        length = (max_task - 1) * n + max_task + (count_max - 1)
        space = (max_task - 1) * (n - count_max + 1)

        if(space >= (sum_tasks - count_max * max_task)):
            return length
        
        return sum_tasks