from agentnet.agent import Agent
from agentnet.network import Network
from agentnet.policy import RandomPolicy, SimplePolicy


def test_simple_policy():

    agent1 = Agent(1)

    network = Network()
    network.connect(1, 4)
    network.connect(1, 3)
    network.connect(1, 2)

    policy = SimplePolicy()

    target = policy.choose_target(agent1, network)

    assert target == 2


def test_random_policy_no_neighbors():
    agent1 = Agent(1)

    network = Network()

    policy = RandomPolicy()

    target = policy.choose_target(agent1, network)

    assert target is None


def test_random_policy_reproducibility():
    agent = Agent(1)

    network = Network()
    network.connect(1, 2)
    network.connect(1, 3)
    network.connect(1, 4)

    # Dve nezávislé politiky s rovnakým seedom
    policy1 = RandomPolicy(seed=42)
    policy2 = RandomPolicy(seed=42)

    choices1 = []
    choices2 = []

    # Vykonáme 10 náhodných rozhodnutí
    for i in range(10):
        choices1.append(policy1.choose_target(agent, network))
        choices2.append(policy2.choose_target(agent, network))

    # Overíme reprodukovateľnosť
    assert choices1 == choices2

    # Overíme počet rozhodnutí
    assert len(choices1) == 10

    # Overíme, že všetky vybrané ID patria susedom
    assert all(target in {2, 3, 4} for target in choices1)
