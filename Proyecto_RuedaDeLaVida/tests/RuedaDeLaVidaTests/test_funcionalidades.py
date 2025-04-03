import pytest, csv, os
import pandas as pd


# Check if exists any None value
@pytest.mark.parametrize('item', ["Nicky", "Mene Gomez", 2,5,1,5,1,5,1,None])
def test_check_null_values(item):
    if(item == None):
        assert True

# Check if exists any Empty value
test_items = ["", "Mene Gomez", 2, 5, 1, 5, 1, 5, 1]
@pytest.mark.parametrize('item', test_items)
def test_check_empty_values(item):
    if(item == "" or len(test_items) < 10):
        assert True


# Check if numerical values 
test_items = ["Nicky", "Mene Gomez", 2, 5, 1, 2, 2, 5, 1, 7]

def test_string_values_in_numerical():
    i = 2
    for j in range(i, len(test_items)):
        assert not isinstance(test_items[j], str)


# Check if digit count is not greater than 2  
test_items = ["Nicky", "Mene Gomez", 2, 5, 1, 2, 2, 5, 1, 7]
def test_digit_count():
    i = 2
    for j in range(i, len(test_items)):
        assert not test_items[j] > 99

# Check if name and lastname its string
test_items = ["Nicky", "Mene", 2, 5, 1, 2, 2, 5, 1, 7]
def test_name_lastname_string():
    for j in range(0, 2):
        assert isinstance(test_items[j], str)


# Check if ange_value_numerical
test_items = ["Nicky", "Mene Gomez", 2, 5, 1, 2, 2, 5, 1, 7]
def test_range_value_numerical_less_10():
    i = 2
    for j in range(i, len(test_items)):
        assert test_items[j] < 11

def test_range_value_numerical_greater_0():
    i = 2
    for j in range(i, len(test_items)):
        assert test_items[j] > 0


# CASOS DE PRUEBA

# Guardar registro
def test_guardar_registro():

    info = ["Juan", "Florez Aristizabal", 10, 2, 7, 10, 1, 1, 4, 1]

    with open("../../datos.csv", "r", encoding="utf-8") as f:
        line_count = sum(1 for line in f)

    with open("../../datos.csv", "a+", newline ='') as csvfile:
        wr = csv.writer(csvfile, dialect='excel', delimiter=',')
        wr.writerow(info)

    with open("../../datos.csv", "r", encoding="utf-8") as f:
        line_count2 = sum(1 for line in f)    

    assert line_count2 == line_count+1

def test_lectura_archivo():
    # Verifica que el archivo existe
    assert os.path.exists("../../datos.csv"), "El archivo datos.csv no existe"

    # Intenta leer el archivo
    df = pd.read_csv("../../datos.csv")

    # Verifica que se cargaron filas
    assert not df.empty, "El archivo está vacío"