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

# Función que simula el algoritmo Improved Move-to-Front
def improved_move_to_front(sequence, requests):
    
    # Se crea una copia de la lista de configuración inicial
    config_list = sequence.copy()
    total_cost = 0
    costs = []                                      # Lista que almacena los costos de cada solicitud
    configurations = []                             # Lista que almacena las configuraciones de la lista
    
    # Se recorre la secuencia de solicitudes
    for index, request in enumerate(requests):
        pos = config_list.index(request)            # Se obtiene el índice de la solicitud en la lista
        cost = pos + 1                              # Se calcula el costo de la solicitud
        total_cost += cost                          # Se suma el costo al costo total
        
        end_index = index + pos + 1                 # Se calcula el índice final de la sublista
        
        # Se verifica si el elemento solicitado aparece en los próximos elementos de la secuencia
        if end_index <= len(requests):
            next_elements = requests[index + 1:end_index]
        else:
            next_elements = []
        
        # Se eliminan los elementos de la sublista de la lista
        if request in next_elements:
            config_list.insert(0, config_list.pop(pos))
        
        costs.append(cost)                          # Se agrega el costo a la lista de costos
        configurations.append(config_list.copy())   # Se agrega la configuración de la lista a la lista de configuraciones
    
    return total_cost, configurations, costs

# Se ejecuta el algoritmo y se obtienen los resultados
total_cost, configurations, costs = improved_move_to_front(initial_list, request_sequence)

# Impresión de resultados
for element, cost, config in zip(request_sequence, costs, configurations):
    print(f"Solicitud: {element} \t Costo: {cost} \t Configuración de la lista: {config}")

print(f"\nEl costo total de la secuencia es: {total_cost}")
print(f"La lista final obtenida de la secuencia es: {configurations[-1]}")
