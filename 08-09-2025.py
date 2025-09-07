def main():
    # Данные из таблицы (П1-П9)
    table = [
        [0, 0, 0, 0, 0, 1, 0, 0, 1],  # П1
        [0, 0, 1, 0, 1, 0, 1, 0, 0],  # П2
        [0, 1, 0, 1, 0, 0, 0, 0, 1],  # П3
        [0, 0, 1, 0, 0, 1, 1, 0, 0],  # П4
        [0, 1, 0, 0, 0, 0, 0, 1, 0],  # П5
        [1, 0, 0, 1, 0, 0, 0, 1, 1],  # П6
        [0, 1, 0, 1, 0, 0, 0, 1, 0],  # П7
        [0, 0, 0, 0, 1, 1, 1, 0, 0],  # П8
        [1, 0, 1, 0, 0, 1, 0, 0, 0]   # П9
    ]
    
    # Граф из буквенных обозначений
    graph = {
        'А': ['Б', 'В', 'Г', 'И'],      
        'Б': ['А', 'В'],  
        'В': ['А', 'Б', 'К'],   
        'Г': ['А', 'Д', 'Е'],   
        'Д': ['Г', 'Ж'],   
        'Е': ['Г', 'Ж', 'И'],   
        'Ж': ['Д', 'Е', 'К'],   
        'И': ['А', 'Е', 'К'],      
        'К': ['В', 'Ж', 'И']    
    }
    
    letters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'И', 'К']
    letter_to_index = {letter: idx for idx, letter in enumerate(letters)}
    
    graph_matrix = [[0]*9 for _ in range(9)]
    
    for letter, neighbors in graph.items():
        i = letter_to_index[letter]
        for neighbor in neighbors:
            j = letter_to_index[neighbor]
            graph_matrix[i][j] = 1
            graph_matrix[j][i] = 1
    
    def is_isomorphic(mapping):
        for i in range(9):
            for j in range(9):
                if table[i][j] != graph_matrix[mapping[i]][mapping[j]]:
                    return False
        return True
    
    table_degrees = [sum(row) for row in table]
    graph_degrees = [sum(row) for row in graph_matrix]
    
    print("Степени вершин в таблице:", table_degrees)
    print("Степени вершин в графе:", graph_degrees)
    
    def find_unique_vertices(degrees):
        unique_vertices = []
        for i, deg in enumerate(degrees):
            if degrees.count(deg) == 1:
                unique_vertices.append((i, deg))
        return sorted(unique_vertices, key=lambda x: x[1])
    
    table_unique = find_unique_vertices(table_degrees)
    graph_unique = find_unique_vertices(graph_degrees)
    
    print("Уникальные вершины в таблице:", table_unique)
    print("Уникальные вершины в графе:", graph_unique)
    
    from itertools import permutations
    
    fixed_mapping = {}
    for (table_idx, table_deg), (graph_idx, graph_deg) in zip(table_unique, graph_unique):
        if table_deg == graph_deg:
            fixed_mapping[table_idx] = graph_idx
    
    print("Фиксированные отображения:", fixed_mapping)
    
    remaining_table = [i for i in range(9) if i not in fixed_mapping]
    remaining_graph = [i for i in range(9) if i not in fixed_mapping.values()]
    
    found = False
    for perm in permutations(remaining_graph):
        mapping = {}
        for i in range(9):
            if i in fixed_mapping:
                mapping[i] = fixed_mapping[i]
            else:
                mapping[i] = perm[remaining_table.index(i)]
        
        if is_isomorphic(mapping):
            found = True
            break
    
    if found:
        result = ''.join(letters[mapping[i]] for i in range(9))
        
        print("\nСоответствие пунктов:")
        for i in range(9):
            print(f"П{i+1} -> {letters[mapping[i]]}")
        
        print(f"\nОтвет: {result}")
    else:
        print("Решения не найдено")

if __name__ == "__main__":
    main()