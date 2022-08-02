from qiskit.circuit.random import random_circuit
import random

for i in range(20000):
    q = random_circuit(random.randint(1, 14), random.randint(1, 14), measure=True, seed=random.randint(1, 1000000))
    q.qasm(filename="./benchmark_files_after/rand_{}.qasm".format(i))
