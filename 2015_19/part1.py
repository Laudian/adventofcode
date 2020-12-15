target = "CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF"

with open("input.txt") as file:
    data = [line.strip("\n") for line in file.readlines()]

produktionen = {}
results = []

import re

for line in data:
    left, right = line.split(" => ")
    if left not in produktionen:
        produktionen[left] = [right]
    else:
        produktionen[left].append(right)
    starts = [m.start() for m in re.finditer(left, target)]
    for start in starts:
        end = start + len(left)
        result = target[:start] + right + target[end:]
        results.append(result)

print("Part 1: " + str(len(set(results))))