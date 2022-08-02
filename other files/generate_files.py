import os

from qiskit import QuantumCircuit




# QuantumCircuit.from_qasm_file(file)


for file in os.listdir("./bfiles1"):

    q = QuantumCircuit.from_qasm_file("./bfiles1/" + file)

    q.barrier()

    q.measure_all()

    q.qasm(filename="./benchmark_files/" + file)



for file in os.listdir("./benchmark_files"):

    with open("./benchmark_files/" + file, "r") as f:
        with open("./benchmark_files_after/" + file, "w") as f1:

            for line in f:
                if not line.startswith("//"):
                    f1.write(line.replace('\n', ' '))


