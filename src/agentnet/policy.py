import random

class SimplePolicy:

    def choose_target(self, agent, network):
        neighbors = network.get_neighbors(agent.id)

        if not neighbors:
            return None

        return min(neighbors)
    
class RandomPolicy:

    def choose_target(self, agent, network):
        neighbors = network.get_neighbors(agent.id)

        if neighbors:
            neighbors_list = list(neighbors)
            return random.choice(neighbors_list)
        else:
            return None



    