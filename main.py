import numpy as np


class Simulation:
    def __init__(self, beds):
        """
        :param beds: Max number of beds allocated for this simulation
        """
        self.beds = beds
        self.current_time = 0
        self.los = {k: [] for k in ["A", "B", "C"]}  # Dictionary of length of stays los[0] is the list of when 
        # patients are staying until for ward a 
        self.next_arrivals = []
        self.blocked = [0, 0, 0]
        self.total = [0, 0, 0]

    def next_arrival(self, ward):
        """
        :type ward: str
        :param ward: choose ward between a, b or c.
        :return: the current time t AND the next arrival for this specific ward.
        """
        return 0

    def next_los(self, ward):
        """
        :type ward: str
        :param ward: choose ward between a, b or c.
        :return: the current time t AND the length of stay (los) in this ward.
        """
        return 0

    def get_next_event(self):
        """
        This looks through next_arrivals and los for smallest value.
        :return: Time when the next event occurs.
        """
        return 0

    def increment_time(self):
        """
        :return: Change the time t.
        """
        self.current_time = self.get_next_event()
        return 0

    def check_in(self):
        """
        :return: Check in a patient to a ward
        """
        return 0

    def check_out(self):
        """
        :return: Check a patient out of a ward
        """
        return 0

    def do_current_event(self):
        """
        Activate the event occurring at time t.
        :return:
        """

        if self.current_time in self.next_arrivals:
            # Check which ward they are joining and add them
            self.check_in()
        # It must be a patient leaving
        else:
            self.check_out()
            # Check which patient is leaving and remove them
            return 0

    def run_simulation(self):
        """
        Runs the simulation.
        :return:
        """
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
