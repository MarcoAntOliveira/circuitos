import matplotlib.pyplot as plt
import numpy as np
from PySpice.Spice.Library import SpiceLibrary
from PySpice.Doc.ExampleTools import find_libraries
from PySpice.Probe.Plot import plot
from PySpice.Spice.Netlist import Circuit

# Define the circuit
circuit = Circuit('Basic Resistor Example')
circuit.V('input', 'in', circuit.gnd, 5)  # Voltage source
circuit.R(1, 'in', 'out', 1000)           # Resistor

# Run DC analysis
simulator = circuit.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.dc(Vinput=slice(0, 10, 1))

# Plot results
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(analysis.input, analysis.out, 'bo-', label='Output Voltage')
ax.set_xlabel('Input Voltage (V)')
ax.set_ylabel('Output Voltage (V)')
ax.grid(True)
ax.legend()
plt.show()
