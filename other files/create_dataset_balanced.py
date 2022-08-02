import random
import json

import pandas as pd

dataset = {}

all_cases = []

BENCHMARK_FILE = "../benchmark_results.csv"

df = pd.read_csv(BENCHMARK_FILE, sep=";")

# print(df)

benchmark_files = list(set([item for subl in df[['file']].values.tolist() for item in subl]))
benchmark_files.sort()

labels = {}
labels[0] = 0
labels[1] = 0
labels[2] = 0

for file in benchmark_files:
    print(file)
    try:
        control_gates_qiskit = df[df['file'] == file][df['method'] == 'QiskitLevel3']['control_gates'].values[0]
        control_gates_rpo = df[df['file'] == file][df['method'] == 'RPOLevel3Pure']['control_gates'].values[0]
        control_gates_rpoqiskit = df[df['file'] == file][df['method'] == 'l3rpopurel3']['control_gates'].values[0]

        # print(control_gates_qiskit)

        label = 0

        if control_gates_rpo < control_gates_qiskit:
            label = 1

            if control_gates_rpoqiskit < control_gates_rpo:
                label = 2

        elif control_gates_rpoqiskit < control_gates_qiskit:
            label = 2

        new_case = {}
        new_case["label"] = label
        labels[label] += 1
        with open("../benchmark_files/{}".format(file), "r") as f:
            s = f.read()
            new_case["text"] = s.replace('\n', ' ')

        all_cases.append(new_case)
    except:
        pass

split = 0.9

test_max_i = int(len(all_cases) * split)

random.shuffle(all_cases)


all_cases_balanced = []

counts = {0:0, 1:0, 2:0}
limit = 3000

for q in all_cases:
    if counts[int(q['label'])] < limit:
        all_cases_balanced.append(q)
        counts[int(q['label'])] += 1

all_cases = all_cases_balanced


split = 0.9

test_max_i = int(len(all_cases) * split)

random.shuffle(all_cases)

labels_trin = {}
labels_trin[0] = 0
labels_trin[1] = 0
labels_trin[2] = 0

labels_test = {}
labels_test[0] = 0
labels_test[1] = 0
labels_test[2] = 0

with open('btrain_x.txt', "w") as f:

    for i in range(0, test_max_i):
        f.write(all_cases[i]['text'] + "\n")

with open('btrain_y.txt', "w") as f:
    for i in range(0, test_max_i):
        labels_trin[all_cases[i]['label']] += 1
        f.write(str(all_cases[i]['label']) + "\n")


with open('btest_x.txt', "w") as f:

    for i in range(test_max_i, len(all_cases)):
        f.write(all_cases[i]['text'] + "\n")

with open('btest_y.txt', "w") as f:
    for i in range(test_max_i, len(all_cases)):
        labels_test[all_cases[i]['label']] += 1
        f.write(str(all_cases[i]['label']) + "\n")



dataset_test = {}
dataset_train = {}

dataset_test["data"] = all_cases[:test_max_i]
dataset_train["data"] = all_cases[test_max_i:]

dataset["data"] = all_cases

with open('bdataset_test.json', "w") as f:
    json.dump(dataset_test, f)

with open('bdataset_train.json', "w") as f:
    json.dump(dataset_train, f)

with open('bdataset.json', "w") as f:
    json.dump(dataset, f)

print(labels)

print(labels_trin)

print(labels_test)
