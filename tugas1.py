import threading

# Fungsi untuk menghitung satu baris hasil matrix
def compute_row(A, B, C, row):
    N = len(A)
    for j in range(N):
        for k in range(N):
            C[row][j] += A[row][k] * B[k][j]

def matrix_multiply_parallel(A, B):
    N = len(A)
    C = [[0]*N for _ in range(N)]
    threads = []

    for i in range(N):
        t = threading.Thread(target=compute_row, args=(A, B, C, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return C


# Contoh Matrix 2x2
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

result = matrix_multiply_parallel(A, B)

print("Hasil Perkalian Matrix:")
for row in result:
    print(row)