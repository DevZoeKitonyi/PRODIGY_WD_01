import time

class TimeKeeper:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.start_time = None
        self.elapsed_time = 0
        self.paused_time = 0
        self.running = False
        self.last_lap = 0
        self.laps = []
    
    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
    
    def pause(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False
    
    def resume(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
    
    def lap(self):
        if self.running:
            current_lap = time.time() - self.start_time - self.last_lap
            self.laps.append(current_lap)
            self.last_lap += current_lap
            return current_lap
        return 0
    
    def get_current_time(self):
        if self.running:
            current_elapsed = time.time() - self.start_time
        else:
            current_elapsed = self.elapsed_time
        
        hours, remainder = divmod(current_elapsed, 3600)
        minutes, seconds = divmod(remainder, 60)
        return hours, minutes, seconds