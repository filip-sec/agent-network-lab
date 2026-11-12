from agentnet.simulation import Simulation
from agentnet.policy import SimplePolicy

def test_population():
    simulation = Simulation()
    simulation.create_population(5)

    assert len(simulation.agents) == 5

def test_information_spread():

    simulation = Simulation()

    simulation.create_population(5)

    simulation.create_line_network()

    simulation.agents[1].receive_information('A')

    simulation.step()

    assert 'A' in simulation.agents[1].knowledge
    assert 'A' not in simulation.agents[3].knowledge

def test_multiple_rounds():
    simulation = Simulation()
    
    simulation.create_population(5)
    
    simulation.create_line_network()
    
    simulation.agents[1].receive_information('A')
    

    for i in range(4):
        simulation.step()

    assert 'A' in simulation.agents[5].knowledge
    assert simulation.round == 4

def test_history():
    simulation = Simulation()

    simulation.create_population(3)
    simulation.create_line_network()

    simulation.agents[1].receive_information('A')

    simulation.step()
    simulation.step()

    # Overenie počtu historických záznamov
    assert len(simulation.history) == 2

    # Overenie čísel kôl
    assert simulation.history[0]['round'] == 1
    assert simulation.history[1]['round'] == 2

    # Stav po prvom kole
    assert 'A' in simulation.history[0]['knowledge'][1]
    assert 'A' in simulation.history[0]['knowledge'][2]
    assert 'A' not in simulation.history[0]['knowledge'][3]

    # Stav po druhom kole
    assert 'A' in simulation.history[1]['knowledge'][1]
    assert 'A' in simulation.history[1]['knowledge'][2]
    assert 'A' in simulation.history[1]['knowledge'][3]

    # Overenie, že sa história prvého kola nezmenila
    assert 'A' not in simulation.history[0]['knowledge'][3]

def test_simple_policy():
    simulation = Simulation(policy=SimplePolicy())

    simulation.create_population(5)

    simulation.create_line_network()

    simulation.agents[1].receive_information('A')

    for i in range(4):
        simulation.step()

    assert 'A' in simulation.agents[2].knowledge
    assert 'A' not in simulation.agents[3].knowledge
    assert simulation.round == 4
