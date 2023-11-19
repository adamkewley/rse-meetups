import numpy as np

def compute_matrix_product(n):
    matrix_a = np.random.rand(n, n)
    matrix_b = np.random.rand(n, n)
    result = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i, j] += matrix_a[i, k] * matrix_b[k, j]

    return result

def process_data(data):
    processed_data = []
    for row in data:
        processed_row = []
        for value in row:
            if value > 0.5:
                processed_row.append(value * 2)
            else:
                processed_row.append(value)
        processed_data.append(processed_row)
    return processed_data

def perform_simulation(iterations, matrix_size):
    result_matrix = np.zeros((matrix_size, matrix_size))

    for _ in range(iterations):
        intermediate_result = compute_matrix_product(matrix_size)
        processed_data = process_data(intermediate_result)
        result_matrix += np.array(processed_data)

    return result_matrix

if __name__ == "__main__":
    result = perform_simulation(iterations=100, matrix_size=200)
    print("Simulation result:")
    print(result)
