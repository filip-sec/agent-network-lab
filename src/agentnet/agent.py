from agentnet.network import Network


class Agent:

    def __init__(self, agent_id):
        self.id = agent_id
        self.knowledge = set()

        print(f'Agent {self.id} initialized with knowledge: {self.knowledge}')

    def receive_information(self, information):
        self.knowledge.add(information)

    def send_information(self, receiver, information, network):
        if information in self.knowledge and network.is_connected(self.id, receiver.id):
            receiver.receive_information(information)

    def broadcast_information(self, information, network, agents):
        neighbors = network.get_neighbors(self.id)

        for neighbor_id in neighbors:
            neighbor = agents[neighbor_id]
            self.send_information(neighbor, information, network)


if __name__ == "__main__":

    agent1 = Agent(1)
    agent2 = Agent(2)
    agent3 = Agent(3)

    agents = {
        1: agent1,
        2: agent2,
        3: agent3
    }

    network = Network()

    network.connect(agent1.id, agent2.id)
    network.connect(agent1.id, agent3.id)

    agent1.receive_information('A')
    agent2.receive_information('B')

    agent1.broadcast_information('A', network, agents)

    print(agent1.knowledge)
    print(agent2.knowledge)
    print(agent3.knowledge)