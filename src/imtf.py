"""
Proyecto 03 - IMTF
CC3041 - Análisis y Diseño de Algoritmos

Melissa Pérez Alarcón, 21385
"""

# --- Inputs ---
initial_list = [0, 1, 2, 3, 4]

# -- Best case --
#request_sequence = [0] * 20

# -- Worst case --
request_sequence = [4, 3, 2, 1, 0] * 4

def improved_move_to_front(sequence, requests):
    config_list = sequence.copy()
    total_cost = 0
    costs = []
    configurations = []
    
    request_list = list(requests)
    
    for index, request in enumerate(request_list):
        pos = config_list.index(request)
        cost = pos + 1
        total_cost += cost
        
        next_elements = request_list[index + 1:index + pos + 1] if (index + pos + 1 <= len(request_list)) else []
        
        if request in next_elements:
            config_list.insert(0, config_list.pop(pos))
        
        costs.append(cost)
        configurations.append(config_list.copy())
    
    return total_cost, configurations, costs

total_cost, configurations, costs = improved_move_to_front(initial_list, request_sequence)

for element, cost, config in zip(request_sequence, costs, configurations):
    print(f"Solicitud: {element} \t Costo: {cost} \t Configuración de la lista: {config}")

print(f"\nEl costo total de la secuencia es: {total_cost}")
print(f"La lista final obtenida de la secuencia es: {configurations[-1]}")
