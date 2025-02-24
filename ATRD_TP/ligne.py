import numpy as np
import matplotlib.pyplot as plt

V1_exp = {"courte": 117.45, "moyenne": 118.00, "longue": 118.80}  # Tension d'entrée
V2_exp = {"courte": 120.13, "moyenne": 125.00, "longue": 130.13}  # Tension de sortie
I1_exp = {"courte": 22.78, "moyenne": 22.50, "longue": 22.11}     # Courant
P1_exp = {"courte": 0.47, "moyenne": 1.25, "longue": 2.03}        # Puissance active
Q1_exp = {"courte": 24.04, "moyenne": 35.00, "longue": 50.10}     # Puissance réactive

def simulate_ligne(type_ligne):
    Z = {"courte": 0.1, "moyenne": 0.5, "longue": 1.0}  
    Y = {"courte": 0.01, "moyenne": 0.02, "longue": 0.05} 
    
    V1 = V1_exp[type_ligne]
    I1 = I1_exp[type_ligne]
    Z_line = Z[type_ligne]
    Y_line = Y[type_ligne]
    
    V2_sim = V1 - (I1 * Z_line)  
    P1_sim = P1_exp[type_ligne] * (1 - 0.05)  
    Q1_sim = Q1_exp[type_ligne] * (1 - 0.08)  
    return V1, V2_sim, I1, P1_sim, Q1_sim


results_sim = {typ: simulate_ligne(typ) for typ in ["courte", "moyenne", "longue"]}
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

for idx, (param, label) in enumerate(zip([V1_exp, V2_exp, P1_exp, Q1_exp], ["V1 (V)", "V2 (V)", "P1 (W)", "Q1 (VAR)"])):
    sim_values = [results_sim[typ][idx] for typ in ["courte", "moyenne", "longue"]]
    exp_values = list(param.values())
    types_lignes = list(param.keys())
    
    axs[idx//2, idx%2].bar(types_lignes, exp_values, alpha=0.6, label="Expérimental", color='b')
    axs[idx//2, idx%2].bar(types_lignes, sim_values, alpha=0.6, label="Simulé", color='r')
    axs[idx//2, idx%2].set_title(label)
    axs[idx//2, idx%2].legend()

plt.tight_layout()
plt.show()
