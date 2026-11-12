import random


class SimplePolicy:
    def choose_target(self, agent, network):
        neighbors = network.get_neighbors(agent.id)

        if not neighbors:
            return None

        return min(neighbors)


class RandomPolicy:
    def __init__(self, seed=None):
        self.rng = random.Random(seed)

    def choose_target(self, agent, network):
        neighbors = network.get_neighbors(agent.id)

        if neighbors:
            neighbors_list = sorted(neighbors)
            return self.rng.choice(neighbors_list)
        else:
            return None
