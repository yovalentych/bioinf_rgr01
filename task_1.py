import numpy as np
import math
from data import (
    control_0,
    control_4,
    control_10,
    control_16,
    control_22,
    control_28,
    mf_0,
    mf_4,
    mf_10,
    mf_16,
    mf_22,
    mf_28,
    chelate_0,
    chelate_4,
    chelate_10,
    chelate_16,
    chelate_22,
    chelate_28,
    mf_chelate_0,
    mf_chelate_4,
    mf_chelate_10,
    mf_chelate_16,
    mf_chelate_22,
    mf_chelate_28,
)

total_experiment = {
    "control": [control_0, control_4, control_10, control_16, control_22, control_28],
    "mf": [mf_0, mf_4, mf_10, mf_16, mf_22, mf_28],
    "chelate": [chelate_0, chelate_4, chelate_10, chelate_16, chelate_22, chelate_28],
    "mf_chelate": [
        mf_chelate_0,
        mf_chelate_4,
        mf_chelate_10,
        mf_chelate_16,
        mf_chelate_22,
        mf_chelate_28,
    ],
}
# Total average value
all_values = [
    values for values_list in total_experiment.values() for values in values_list
]
avg_total = np.mean(all_values)

print(f"Total average value: {round(avg_total)}")

# std dev
std_dev = []
exp_duration = [0, 4, 10, 16, 22, 28]

for experiment, values in total_experiment.items():
    sub_std_dev = []
    for sub_values in values:
        sub_std_dev.append(round(np.std(sub_values)))
    std_dev.append(sub_std_dev)

for i in range(len(exp_duration)):
    duration = exp_duration[i]
    print("-----------------------------------")
    print(f"Cultivation time {duration} hours:")
    for j, experiment_name in enumerate(total_experiment.keys()):
        deviation = std_dev[j][i]
        print(f"  {experiment_name}: {deviation}")
