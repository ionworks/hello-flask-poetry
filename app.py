from flask import Flask
import pybamm

app = Flask(__name__)

@app.route('/')
def hello_fly():
    model = pybamm.lithium_ion.SPM()
    sim = pybamm.Simulation(model)
    sim.solve([0, 3600])
    return list(sim.solution["Voltage [V]"].entries)