"""
Proyecto 03 - MTF
CC3041 - Análisis y Diseño de Algoritmos

Melissa Pérez Alarcón, 21385
"""

# --- Inputs ---
initial_list = [0, 1, 2, 3, 4]

# --- 1 ---
request_sequence = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]

# --- 2 ---
# request_sequence = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]

def move_to_front(sequence, requests):
    config_list = sequence.copy()
    total_cost = 0
    costs = []
    configurations = []
    
    for request in requests:
        index = config_list.index(request)
        cost = index + 1
        total_cost += cost
        config_list.pop(index)
        config_list.insert(0, request)
        costs.append(cost)
        configurations.append(config_list.copy())
    
    return total_cost, configurations, costs

total_cost, configurations, costs = move_to_front(initial_list, request_sequence)

print(f"Lista de configuración inicial: {initial_list}\n")

for element, cost, config in zip(request_sequence, costs, configurations):
    print(f"Solicitud: {element} \t Costo: {cost} \t Configuración de la lista: {config}")

print(f"\nEl costo total de la secuencia es: {total_cost}")
print(f"La lista final obtenida de la secuencia es: {configurations[-1]}")
