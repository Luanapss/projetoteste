import pandas as pd
from utils import calcular_media_geral, calcular_total_por_categoria

def test_calcular_media_geral():
    df = pd.DataFrame({"valor": [10, 20, 30]})
    assert calcular_media_geral(df) == 20

def test_calcular_total_por_categoria():
    df = pd.DataFrame({"categoria": ["A", "A", "B"], "valor": [10, 20, 30]})
    resultado = calcular_total_por_categoria(df)
    assert resultado["A"] == 30
    assert resultado["B"] == 30