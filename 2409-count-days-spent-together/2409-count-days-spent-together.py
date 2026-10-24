class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        stt=max(arriveAlice,arriveBob)
        end=min(leaveAlice,leaveBob)
        if stt>end:
            return 0
        days=[31,28,31,30,31,30,31,31,30,31,30,31]
        def to_days(date):
            month,day=map(int,date.split('-'))
            return sum(days[:month-1])+day
        return to_days(end) - to_days(stt)+1    
                           


        