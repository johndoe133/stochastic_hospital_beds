import numpy as np

class simulation():
    def __init__(self, beds):
        self.beds = beds
        self.current_time = 0
        self.los = [[],[],[]] # List of list of length of stays los[0] is the list of when patients are staying until for ward a
        self.next_arrivals = []
        self.blocked = [0,0,0]
        self.total = [0,0,0]

    def next_arrival(self, ward):
        # Return current_time + itnerarrival time for a specific ward
        # ward = 0, 1, 2 for a, b, c
        return 0

    def next_los(self, ward):
        # Return current_time + los time for a specific ward
        # ward = 0, 1, 2 for a, b, c
        return 0

    def get_next_event(self):
        # Return the time of the next event to occur
        # This looks through next_arrivals and los for smallest value
        return 0

    def increment_time(self):
        # Change the time to the next event
        self.current_time = self.get_next_event()
        return 0
    
    def check_in(self):
        # Check in a patient to a ward
        return 0

    def check_out(self):
        # Check a patient out of a ward
        return 0

    def do_current_event(self):
        # Do the event occurring now depending on the time

        if self.current_time in self.next_arrivals:
            # Check which ward they are joining and add them
            self.check_in()
        # It must be a patient leaving
        else:
            self.check_out()
            # Check which patient is leaving and remove them
            return 0

    def run_simulation(self):
        # reset current time
        self.current_time = 0

        # Set initial next arrivals
        self.next_arrivals += [self.next_arrival(i) for i in range(3)]
        while self.current_time < 365:
            # Increment time to next event
            self.increment_time() 

            # Do the event at the current time
            self.do_current_event()
            # This function should change the los or next_arrivals variable
            # It should also adjust self.blocked and self.total (number of patients)
            
       