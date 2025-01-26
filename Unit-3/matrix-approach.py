import numpy as np
import fractions


def create_fourier_matrix(N):
    """
    Creates a Fourier matrix of size NxN.

    Parameters:
    N (int): The size of the matrix.

    Returns:
    numpy.ndarray: The Fourier matrix.
    """
    fourier_matrix = np.zeros((N, N), dtype=complex)
    for i in range(N):
        for j in range(N):
            fourier_matrix[i, j] = np.exp(-2j * np.pi * i * j / N)
    return fourier_matrix


def print_complex_matrix(matrix):
    """
    Prints a matrix of complex numbers in a pretty format.

    Parameters:
    matrix (numpy.ndarray): The matrix to print.
    """
    for row in matrix:
        for elem in row:
            r = np.abs(elem)

            # angle = np.angle(elem)
            # print((f"{r:.2f}*e^({angle:.2f}i)").ljust(20), end="\t")

            angle = np.angle(elem) / np.pi
            frac_angle = fractions.Fraction(angle).limit_denominator()

            if round(r, 2) == 0:
                print("0".ljust(20), end="\t")
            else:
                print((f"{r:.2f}*e^[({frac_angle})πi]").ljust(20), end="\t")
        print()


def is_symmetric(matrix):
    """
    Checks if a matrix is equal to its transpose.

    Parameters:
    matrix (numpy.ndarray): The matrix to check.

    Returns:
    bool: True if the matrix is symmetric, False otherwise.
    """
    return np.allclose(matrix, matrix.T)


def create_random_complex_matrix(N):
    """
    Creates a complex matrix of size NxN with random complex numbers.

    Parameters:
    N (int): The size of the matrix.

    Returns:
    numpy.ndarray: The complex matrix.
    """
    real_part = np.random.rand(N, N)
    imag_part = np.random.rand(N, N)
    complex_matrix = real_part + 1j * imag_part
    return complex_matrix


def inverse_complex_matrix(matrix):
    """
    Calculates the inverse of a complex matrix.

    Parameters:
    matrix (numpy.ndarray): The complex matrix to invert.

    Returns:
    numpy.ndarray: The inverse of the matrix.
    """
    return np.linalg.inv(matrix)


def print_unique_entries(A):
    # Get the shape of the matrix
    rows, cols = A.shape

    # Create a set to store the printed entries
    printed_entries = set()

    print("Unique entries:")

    # Iterate over the entries of the matrix
    for i in range(rows):
        for j in range(cols):
            entry = np.round(A[i, j], 10)
            # Check if the entry has already been printed
            if entry not in printed_entries:
                r = np.abs(entry)
                angle = np.angle(entry) / np.pi
                frac_angle = fractions.Fraction(angle).limit_denominator()
                print(f"Entry ({i}, {j}) = {entry}".ljust(50) + f"-> {r:6.2f}".rjust(10) + f"*e^[({frac_angle})πi]")

                printed_entries.add(entry)

    print("Total unique entries:", len(printed_entries))


# N=3
# M = create_random_complex_matrix(N)
# print(M)
# print("")
# print(M.T)

# N = 5
# fourier_matrix = create_fourier_matrix(N)
# print_complex_matrix(fourier_matrix)
# print("")
# print_complex_matrix(fourier_matrix.T)
# print("")
# print(f"Is symmetric: {is_symmetric(fourier_matrix)}")

# N = 5
# F = create_fourier_matrix(N)
# F_1 = inverse_complex_matrix(F)
# print_complex_matrix(F)
# print("")
# print_complex_matrix(F_1)
# print("")
# print_complex_matrix(F @ F_1)

N = 11
F = create_fourier_matrix(N)
print_complex_matrix(F)
print("")
print_unique_entries(F)
