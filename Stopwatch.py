from Timekeeper import TimeKeeper
import os
import platform
            


class StopwatchUI:
    def __init__(self):
        self.time_keeper = TimeKeeper()
        self.clear_screen()
    
    def clear_screen(self):
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
    
    def display_header(self):
        print("\n" + "="*50)
        print("PYTHON STOPWATCH APPLICATION".center(50))
        print("="*50)
    
    def display_controls(self):
        print("\nCONTROLS:")
        print("[S]tart | [P]ause | [R]esume | [L]ap | [C]lear | [Q]uit")
    
    def display_time(self, hours, minutes, seconds):
        print(f"\nCurrent Time: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}")
    
    def display_laps(self):
        if self.time_keeper.laps:
            print("\nLap Times:")
            for i, lap in enumerate(self.time_keeper.laps, 1):
                h, m, s = self._convert_to_hms(lap)
                print(f"Lap {i}: {int(h):02d}:{int(m):02d}:{int(s):02d}")
    
    def _convert_to_hms(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return hours, minutes, seconds
    
    def run(self):
        while True:
            self.clear_screen()
            self.display_header()
            self.display_controls()
            
            hours, minutes, seconds = self.time_keeper.get_current_time()
            self.display_time(hours, minutes, seconds)
            self.display_laps()
            
            command = input("\nEnter command: ").lower()
            
            if command == 's':
                self.time_keeper.start()
                print("\033[92mStopwatch started!\033[0m")  # Green text
            elif command == 'p':
                self.time_keeper.pause()
                print("\033[93mStopwatch paused.\033[0m")  # Yellow text
            elif command == 'r':
                self.time_keeper.resume()
                print("\033[92mStopwatch resumed.\033[0m")  # Green text
            elif command == 'l':
                if self.time_keeper.running:
                    lap_time = self.time_keeper.lap()
                    h, m, s = self._convert_to_hms(lap_time)
                    print(f"\033[94mLap recorded: {int(h):02d}:{int(m):02d}:{int(s):02d}\033[0m")  # Blue text
                else:
                    print("\033[91mCannot record lap while stopped\033[0m")  # Red text
            elif command == 'c':
                self.time_keeper.reset()
                print("\033[91mStopwatch reset.\033[0m")  # Red text
            elif command == 'q':
                print("\033[95mExiting stopwatch application...\033[0m")  # Purple text
                break
            else:
                print("\033[91mInvalid command!\033[0m")  # Red text
            
            input("\nPress Enter to continue...")

#
