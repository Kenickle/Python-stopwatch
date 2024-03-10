import time

class Timer():
    '''Every instance is a new timer'''

    def __init__(self):
        self.timerstart = False
        self.timerstop = False

    def start(self):
        '''Begin / reset the timer. If time provided, it will start at that many seconds.'''
        self.timerstart = time.perf_counter()
        self.timerstop = False

    def stop(self):
        '''Temporarily pause the timer, will not reset but The time will stop increasing.'''
        if not self.timerstop:
            self.timerstop = time.perf_counter()

    def resume(self):
        '''Resume the timer - only works if the timer has been stopped.'''
        if self.timerstop:
            self.timerstart = time.perf_counter() - (self.timerstop - self.timerstart)
            self.timerstop = False

    def gettime(self, formatted: bool = False):
        '''Will return the time, if formatted is True, 
        it will be shown as {hh}h {mm}m {ss.ss}s, else it will 
    return seconds, rounded to 2dp'''
        if not self.timerstart:
            currenttime = 0
        elif not self.timerstop:
            currenttime = round(time.perf_counter() - self.timerstart, 2)
        else:
            currenttime = round(self.timerstop - self.timerstart, 2)

        if formatted:
            seconds = round(currenttime % 60, 2)
            minutes = int(currenttime // 60 % 60)
            hours = int(currenttime // 60 // 60)

            return f"{hours}h {minutes}m {seconds}s"
        else:
            return currenttime