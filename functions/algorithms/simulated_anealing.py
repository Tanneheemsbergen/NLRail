import random
import math
from functions.algorithms.hillclimber import Hillclimber
from functions.helpers.calculation import calculate_quality

class SimulatedAnnealing(Hillclimber):
    """
    The SimulatedAnnealing class that changes a random node in the model to a random valid value.
    Each improvement or equivalent solution is kept for the next iteration.
    Also sometimes accepts solutions that are worse, depending on the current temperature.
    Most of the functions are similar to those of the HillClimber class, which is why
    we use that as a parent class.
    """
    def __init__(self, graph, rounds, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME, temperature: int or float=1,):
        
        # Starting temperature and current temperature
        self.T0 = temperature
        self.T = temperature

        # Use the init of the Hillclimber class
        super().__init__(graph, rounds, iteration, MAX_AMOUNT_TRAJECTS, MAX_TIME)

        
    def update_temperature(self) -> None:
        """
        This function implements a *linear* cooling scheme.
        Temperature will become zero after all iterations passed to the run()
        method have passed.
        """
        self.T = self.T - (self.T0 / self.iterations)
<<<<<<< HEAD:functions/algorithms/simulating_anealing.py
        #print(self.iterations)

=======
  
>>>>>>> 469b19d74239a85cf54c725d4ac20b0fb4335f8f:functions/algorithms/simulated_anealing.py
        # Exponential would look like this:
        # alpha = 0.99
        # self.T = self.T * alpha

        # where alpha can be any value below 1 but above 0
    def check_solution(self, check_trajects, MAX_AMOUNT_TRAJECTS):
        """
        Checks the solution and remembers and accepts the solution, if better.
        """
        new_quality = calculate_quality(check_trajects, self.graph, MAX_AMOUNT_TRAJECTS)
        old_quality = self.quality

        delta = old_quality - new_quality

        probability = math.exp(-delta / self.T)
  
        # Pull a random number between 0 and 1 and see if we accept the soltuion!
        if random.random() < probability:
            self.trajects = check_trajects
            self.quality = new_quality

        # Update the temperature
        self.update_temperature()
