from collections import deque
from random import uniform

"""
Events:
1. Client arrives to the system
2. Client goes out from teller 1
3. Client goes out from teller 2
Relevant state variables:
1. Watch simulation (current simulation time)
2. Length of queue1
3. Length of queue2
4. Next time instance of each event
"""


class Client:
    pass


class Teller:
    def __init__(self, t):
        self.queue = deque()
        self.end_time = 2 * t
        """
        Initially the ending time of serve must be out of  range
        because no client can leave a teller if there is not a
        client being attended. With 2*t we ensure that someone always
        'arrives' before the event 'goes out of teller' is activated.
        """


class Bank:
    def __init__(self, t):
        self.tellers = [Teller(t), Teller(t)]


class Simulation:
    def __init__(self, max_time, arrival, departure):

        self.ending_time_sim = max_time
        self.simulation_time = 0
        self.next_client_arrival = uniform(1, arrival)
        self.bank = Bank(max_time)
        self.departure = departure
        self.arrival = arrival

    def departure_first(self, queue_yes, queue_no):

        queue = self.bank.tellers[queue_yes].queue
        print('[start] departure queue', queue_yes,
              len(self.bank.tellers[queue_yes].queue),
              len(self.bank.tellers[queue_no].queue))

        if len(self.bank.tellers[queue_yes].queue) > 0:
            queue.popleft()

        if len(self.bank.tellers[queue_no].queue) > \
                        len(self.bank.tellers[queue_yes].queue) + 1 >= 0:
            print('client changes queue')
            self.bank.tellers[queue_yes].queue.append(
                self.bank.tellers[queue_no].queue.popleft())

        if len(self.bank.tellers[queue_yes].queue) == 0:
            self.bank.tellers[queue_yes].end_time = \
                2 * self.ending_time_sim
        else:
            self.bank.tellers[
                queue_yes].end_time = self.simulation_time + \
                                      uniform(1, self.departure)

        print('[end] departure queue', queue_yes,
              len(self.bank.tellers[queue_yes].queue),
              len(self.bank.tellers[queue_no].queue))

    def arrival_first(self, first):

        print('client arrives', first)
        self.next_client_arrival = self.simulation_time + \
                                   uniform(1, self.arrival)

        if len(self.bank.tellers[0].queue) <= \
                len(self.bank.tellers[1].queue):
            if len(self.bank.tellers[0].queue) == 0:
                self.bank.tellers[0].end_time = \
                    self.simulation_time + \
                    uniform(1, self.departure)
            self.bank.tellers[0].queue.append(Client())
        else:
            if len(self.bank.tellers[1].queue) == 0:
                self.bank.tellers[1].end_time = \
                    self.simulation_time + \
                    uniform(1, self.departure)
            self.bank.tellers[1].queue.append(Client())

        print('queues', len(self.bank.tellers[0].queue),
              len(self.bank.tellers[1].queue))

    def run(self):

        while True:
            first = min(self.bank.tellers[0].end_time,
                        self.bank.tellers[1].end_time,
                        self.next_client_arrival)
            if first >= self.ending_time_sim:
                break

            self.simulation_time = first

            if self.next_client_arrival == first:
                self.arrival_first(first)
            else:
                if self.bank.tellers[0].end_time == first:
                    self.departure_first(0, 1)
                else:
                    self.departure_first(1, 0)


if __name__ == '__main__':
    s = Simulation(80, 3, 10)
    s.run()
