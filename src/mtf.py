"""
Proyecto 03 - MTF
CC3041 - Análisis y Diseño de Algoritmos

Melissa Pérez Alarcón, 21385
"""

# --- Inputs ---
initial_list = [0, 1, 2, 3, 4]

# --- 1 ---
#request_sequence = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]

# --- 2 ---
#request_sequence = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]

# -- 3 ---
#request_sequence = [0] * 20

# -- 4 ---
#request_sequence = [4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0, 4, 3, 2, 1, 0]

# -- 5 ---
request_sequence = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]


# Función que simula el algoritmo Move-to-Front
def move_to_front(sequence, requests):
    
    # Se crea una copia de la lista de configuración inicial
    config_list = sequence.copy()
    total_cost = 0
    costs = []                                      # Lista que almacena los costos de cada solicitud
    configurations = []                             # Lista que almacena las configuraciones de la lista
    
    # Se recorre la secuencia de solicitudes
    for request in requests:
        index = config_list.index(request)          # Se obtiene el índice de la solicitud en la lista
        
        cost = index + 1                            # Se calcula el costo de la solicitud
        total_cost += cost                          # Se suma el costo al costo total
        
        config_list.pop(index)                      # Se elimina la solicitud de la lista
        config_list.insert(0, request)              # Se inserta la solicitud al inicio de la lista
        
        costs.append(cost)                          # Se agrega el costo a la lista de costos
        configurations.append(config_list.copy())   # Se agrega la configuración de la lista a la lista de configuraciones
    
    return total_cost, configurations, costs

# Se ejecuta el algoritmo y se obtienen los resultados
total_cost, configurations, costs = move_to_front(initial_list, request_sequence)

# Impresión de resultados
for element, cost, config in zip(request_sequence, costs, configurations):
    print(f"Solicitud: {element} \t Costo: {cost} \t Configuración de la lista: {config}")

print(f"\nEl costo total de la secuencia es: {total_cost}")
print(f"La lista final obtenida de la secuencia es: {configurations[-1]}")
