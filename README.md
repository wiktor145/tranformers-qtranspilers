# tranformers-qtranspilers
Repository for code reated with masters thesis idea for predicting quantum transpilers performance with transformers neural network models.

# Idea from master thesis

"Creating way of predicting, which optimizer would probably perform the best on a given circuit - 
different optimizers had very different performances on some circuits. 
Without testing all optimizers, we do not know which one would perform the best. 
It would be very good to have a tool to predict with good probability, without running comparison and simulating all result circuits, which optimizer would probably be the best on a given quantum circuit. 
The author's suggestion is to use the Transformer (https://doi.org/10.48550/arxiv.1706.03762), a deep learning model that uses the mechanism of attention. 
The idea is that these networks are good in NLP use cases and can find connections between input parts.
Such a network would get the QASM file as input and could output labels, which optimizer would most probably perform the best on that circuit. 
It could also have multiple outputs, each one for one desired metric, like gates count, fidelity, etc. 
To train such a network, a larger set of benchmark circuits should be gathered, as the set of 45 circuits is not large enough for training. 
In addition, only a few best optimizers could be selected."


# POC

 network: CodeBERTa-small-v1 (6-layers, 84M parameters)

input: QASM file - quantum circuit

output: 0, 1 or 2 - which of the three transpilers will result in the least amount of control gates

transpilers: QiskitLevel3, RPOLevel3Pure, and l3rpopurel3

2 datasets: 19979 benchmark circuits (94 from benchmarking set and 19885 randomly generated) and balanced subset with 9000 circuits (3000:3000:3000 split)

dataset train:test split - 90:10

# POC results

 5 epochs

 bath size 16

 optimizer Adam with learning rate $5 * 10^{-5}$

 sparse categorical cross entropy as the loss function

 using smaller, balanced dataset with 9000 circuits
 

| precision  | recall | f1-score | support  |
| ----------- | ----- | -------- | ------- |
| transpiler 1 | 0.93 | 0.60 | 0.73 | 306  |
| transpiler 2 | 0.72 | 0.66 | 0.69 | 291  |
| transpiler 3 | 0.55 | 0.80 | 0.65 | 303 |
| accuracy | | | 0.69 | 900 |
 
