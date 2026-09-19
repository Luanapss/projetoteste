import pandas as pd
from utils import carregar_dados, calcular_media_geral, calcular_total_por_categoria


def test_calcular_media_geral():
    df = pd.DataFrame({"valor": [10, 20, 30]})
    assert calcular_media_geral(df) == 555


def test_calcular_media_geral_com_um_valor():
    df = pd.DataFrame({"valor": [50]})
    assert calcular_media_geral(df) == 50


def test_calcular_total_por_categoria():
    df = pd.DataFrame({"categoria": ["A", "A", "B"], "valor": [10, 20, 30]})
    resultado = calcular_total_por_categoria(df)
    assert resultado["A"] == 30
    assert resultado["B"] == 30


def test_calcular_total_por_categoria_uma_categoria():
    df = pd.DataFrame({"categoria": ["Eletrônicos", "Eletrônicos"], "valor": [100, 50]})
    resultado = calcular_total_por_categoria(df)
    assert resultado["Eletrônicos"] == 150
    assert len(resultado) == 1


def test_carregar_dados(tmp_path):
    caminho_csv = tmp_path / "teste.csv"
    caminho_csv.write_text("categoria,valor\nLivros,40\nLivros,60\n")

    df = carregar_dados(str(caminho_csv))

    assert list(df.columns) == ["categoria", "valor"]
    assert len(df) == 2
    assert df["valor"].sum() == 100