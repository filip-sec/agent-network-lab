from agentnet.agent import Agent
from agentnet.network import Network
from agentnet.policy import SimplePolicy


def test_simple_policy():

    agent1 = Agent(1)

    network = Network()
    network.connect(1, 4)
    network.connect(1, 3)
    network.connect(1, 2)

    policy = SimplePolicy()

    target = policy.choose_target(agent1, network)

    assert target == 2