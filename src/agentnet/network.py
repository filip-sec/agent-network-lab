class Network:

    def __init__(self):

        self.connections = {

        }

    def connect(self, agent1, agent2):

        if agent1 not in self.connections:
            self.connections[agent1] = set()

        if agent2 not in self.connections:
            self.connections[agent2] = set()

            
        self.connections[agent1].add(agent2)
        self.connections[agent2].add(agent1)
        
    def disconnect(self, agent1, agent2):

        if agent1 in self.connections and agent2 in self.connections:
            self.connections[agent1].discard(agent2)
            self.connections[agent2].discard(agent1)

    def is_connected(self, agent1, agent2):
        if agent1 in self.connections and agent2 in self.connections[agent1]:
            return True 
        else: 
            return False

    def get_neighbors(self, agent_id):
        if agent_id in self.connections:
            return self.connections[agent_id].copy()
        else: 
            return set()
        
network = Network()

network.connect(2, 3)
network.connect(3, 4)
network.connect(1, 2)

network.disconnect(2, 3)
network.disconnect(5, 6)
print(network.connections)