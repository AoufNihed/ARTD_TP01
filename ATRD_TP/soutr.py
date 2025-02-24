import numpy as np
import matplotlib.pyplot as plt

#câbles souterrains
exp_data = {
    "V1 (V)": [118.80],
    "V2 (V)": [146.04],
    "P1 (W)": [2.03],
    "Q1 (VAR)": [50.10],
    "I1 (mA)": [22.11]
}

Z_cable = 0.1 + 0.5j  # Impédance caractéristique supposée
L_cable = 5  # Longueur supposée en km

sim_data = {}
for param, values in exp_data.items():
    if "V" in param:
        sim_data[param] = [v * np.exp(-0.02 * L_cable) for v in values] 
    elif "P1" in param:
        sim_data[param] = [values[0] * 0.95]  
    elif "Q1" in param:
        sim_data[param] = [values[0] * 0.90]  
    elif "I1" in param:
        sim_data[param] = [values[0] * 1.05]  

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
params = list(exp_data.keys())

i = 0
for ax in axes.flat:
    param = params[i]
    ax.bar(["Expérimental", "Simulé"], [exp_data[param][0], sim_data[param][0]], color=["blue", "red"], alpha=0.7)
    ax.set_title(param)
    ax.set_ylabel("Valeur")
    i += 1

plt.tight_layout()
plt.show()
