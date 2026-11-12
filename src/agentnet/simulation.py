from agentnet.network import Network
from agentnet.agent import Agent
from agentnet.policy import SimplePolicy


class Simulation:

    def __init__(self, policy=None):

        self.policy = policy

        self.round = 0

        self.agents = {}

        self.history = []

        self.network = Network()

    def add_agent(self, agent):
        self.agents[agent.id] = agent

    def create_population(self, count):
        for i in range(1, count + 1):
            agent = Agent(i)
            self.add_agent(agent)

    def create_line_network(self):
        for i in range(1, len(self.agents)):
            self.network.connect(i, i + 1)

    def step(self):
        snapshot = {}

        # Uloženie vedomostí na začiatku kola
        for agent_id, agent in self.agents.items():
            snapshot[agent_id] = agent.knowledge.copy()

        # Komunikácia medzi agentmi
        for agent_id, knowledge in snapshot.items():

            agent = self.agents[agent_id]

            for information in knowledge:

                if self.policy is None:

                    # Pôvodný broadcast
                    agent.broadcast_information(
                        information,
                        self.network,
                        self.agents
                    )

                else:

                    # Rozhodovanie pomocou politiky
                    target_id = self.policy.choose_target(
                        agent,
                        self.network
                    )

                    if target_id is not None:

                        receiver = self.agents[target_id]

                        agent.send_information(
                            receiver,
                            information,
                            self.network
                        )

        # Aktualizácia počítadla kôl
        self.round += 1

        print(f"Kolo {self.round}")

        # Vytvorenie historického záznamu
        record = {
            'round': self.round,
            'knowledge': {}
        }

        for agent_id, agent in self.agents.items():
            record['knowledge'][agent_id] = agent.knowledge.copy()

        self.history.append(record)


if __name__ == "__main__":

    # Vytvorenie rozhodovacej politiky
    policy = SimplePolicy()

    # Vytvorenie simulácie
    simulation = Simulation(policy=policy)

    # Vytvorenie populácie
    simulation.create_population(5)

    # Vytvorenie líniovej siete
    simulation.create_line_network()

    # Počiatočné vedomosti
    simulation.agents[1].receive_information('A')

    # Spustenie simulácie
    for i in range(4):

        simulation.step()

        for agent_id, agent in simulation.agents.items():
            print(agent_id, agent.knowledge)

    # Výpis histórie
    print("\nHistória simulácie:")

    for record in simulation.history:
        print(record)