import time
import sched

class Solution:

    def schedule_a_function(self, target_time, fun, *args):

        # runs until the queue is empty, doesn't die with main thread
        sch = sched.scheduler(time.time, time.sleep)
        sch.enterabs(target_time, 1, fun, argument=args)
        sch.run()

if __name__ == "__main__":
    sol = Solution()
    sol.schedule_a_function(time.time()+5, print, 'Hoho')