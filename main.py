# DATA MINING (SIMILATIRY, DISIMILARITY)

# IMPORT LIBRARY
import math

nominal = ['B', 'D', 'A', 'B', 'B', 'C']
ordinal = [3, 2, 1, 3, 2, 1]
numberic = [80, 50, 90, 75, 82, 65]

# DEFINITION ARRAY 2D
data_nominal = [[0 for _ in range(len(nominal))] for _ in range(len(nominal))]
data_ordinal = [[0 for _ in range(len(ordinal))] for _ in range(len(ordinal))]
data_numberic = [[0 for _ in range(len(numberic))] for _ in range(len(numberic))]

def print_data():
    # VIEW DATA IN ONE TABLE
    for i in range(len(nominal)):
        print(nominal[i], end="\t|\t")
        print(ordinal[i], end="\t|\t")
        print(numberic[i])
    print()
    

def numberic_function():
    print("NUMERIC")
    max_numeric = max(numberic)
    min_numeric = min(numberic)
    print("Max: ", max_numeric)
    print("Min: ", min_numeric)

    print("\nMatriks ketidakmiripan disimilarity")
    print("=========================================================================================")
    for i in range(len(numberic)):
        for j in range(len(numberic)):
            # RUMUS = |X - Y| / MAX - MIN
            result_numeric = round(abs(numberic[i] - numberic[j]) / (max_numeric - min_numeric), 2)
            # INSERT MULTIPLE DATA ARRAY WITH 2D ARRAY WITH INDEX I AND J
            data_numberic[i][j] = result_numeric
            
            print(result_numeric, end="\t|\t")
        print()
    print("=========================================================================================")


def nominal_function():
    print("NOMINAL")
    # HITUNG MATRIKS KETIDAKMIRIPAN DISIMILARYTY
    # 1. JUMLAH DATA
    jumlah_data = len(nominal)
    print("Jumlah data: ", jumlah_data)
    # 2. JUMLAH DATA YANG SAMA
    jumlah_data_sama = 0
    jumlah_data_tidak_sama = 0

    print("=========================================================================================")
    for i in range(jumlah_data):
        for j in range(jumlah_data):
            # if x /= Y = 0
            # if x == Y = 1
            if nominal[i] == nominal[j]:
                # UPDATE TO VIEW MATRIKS
                print("0", end="\t|\t")
                data_nominal[i][j] = 0

                jumlah_data_sama += 1
            else:
                # UPDATE TO VIEW MATRIKS
                print("1", end="\t|\t")
                data_nominal[i][j] = 1

                jumlah_data_tidak_sama += 1
        print()
    print("=========================================================================================")
    print("Jumlah data yang sama: ", jumlah_data_sama)

def ordinal_function():
    print("ORDINAL")
    # NORMALISASI ORDINAL
    # 1. MENCARI MIN
    min_ordinal = min(ordinal)
    print("Min ordinal: ", min_ordinal)
    # 2. MENCARI MAX
    max_ordinal = max(ordinal)
    print("Max ordinal: ", max_ordinal)
    # 3. NORMALISASI
    normalisasi_ordinal = []
    for i in range(len(ordinal)):
        # RUMUS: (X - MIN) / (MAX - MIN)
        normalisasi = (ordinal[i] - min_ordinal) / (max_ordinal - min_ordinal)
        normalisasi_ordinal.append(normalisasi)
    print("Normalisasi ordinal: ", normalisasi_ordinal)

    # HITUNG MATRIKS KETIDAKMIRIPAN DISIMILARYTY
    # 1. JUMLAH DATA
    jumlah_data = len(normalisasi_ordinal)
    print("Jumlah data: ", jumlah_data)
    # 2. JUMLAH DATA YANG SAMA
    jumlah_data_sama = 0
    jumlah_data_tidak_sama = 0

    print("=========================================================================================")
    for i in range(jumlah_data):
        for j in range(jumlah_data):
            # RUMUS = |X - Y|
            # PRINT VIEW IN MATRIX
            result_ordinal = abs(normalisasi_ordinal[i] - normalisasi_ordinal[j])
            data_ordinal[i][j] = result_ordinal

            print(abs(result_ordinal), end="\t|\t")
            if normalisasi_ordinal[i] == normalisasi_ordinal[j]:
                jumlah_data_sama += 1
            else:
                jumlah_data_tidak_sama += 1
        print()
    print("=========================================================================================")

def campuran_function():
    print("CAMPURAN")
    numberic_function()
    print('\n\n')
    nominal_function()
    print('\n\n')
    ordinal_function()
    print('\n\n')

    len_data_method = 3

    print("Matriks CAMPURAN")
    print("=========================================================================================")
    for i in range(len(nominal)):
        for j in range(len(nominal)):
            # RUMUS = DATA_NOMINAL[INDEX] + DATA_ORDINAL[INDEX] + DATA_NUMBERIC[INDEX] / 3
            result_campuran = round((data_nominal[i][j] + data_ordinal[i][j] + data_numberic[i][j]) / len_data_method, 2)
            # print(f'({data_nominal[i][j]} + {data_ordinal[i][j]} + {data_numberic[i][j]}) / {len_data_method}', end="|")
            print(f'{result_campuran}', end="\t|\t")
        print()
    print("=========================================================================================")
        
def main():
    # SELECT OPTION TO FUNCTION
    print("1. Numberic")
    print("2. Nominal")
    print("3. Ordinal")
    print("4. Campuran")
    option = int(input("Select option: "))
    if option == 1:
        print_data()
        numberic_function()
    elif option == 2:
        print_data()
        nominal_function()
    elif option == 3:
        print_data()
        ordinal_function()
    elif option == 4:
        print_data()
        campuran_function()
    else:
        print("Wrong option")

if __name__ == "__main__":
    main()