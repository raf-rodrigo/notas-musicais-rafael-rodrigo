"""
AAA - 3A - A3
Arange - Act - Asserts
(Arrumar - Agir - Garantir)
"""
from pytest import mark, raises

from notas_musicais_rafael_rodrigo.escalas import ESCALAS, NOTAS, escala


def test_deve_funcionar_com_notas_minusculas():

    # Arrumar
    tonica = 'c'
    tonalidade = 'maior'

    # act - chamo o que quero testar
    result = escala(tonica, tonalidade)

    # Assert
    assert result


def test_deve_retornar_um_erro_dizendo_que_a_nota_nao_existe():
    tonica = 'X'
    tonalidade = 'maior'

    mensagem_de_erro = f'A nota não existe. Tente uma dessas {NOTAS}'

    with raises(ValueError) as error:
        escala(tonica, tonalidade)

    assert mensagem_de_erro == error.value.args[0]


def test_deve_retornar_um_erro_dizendo_que_a_escala_nao_existe():
    tonica = 'C'
    tonalidade = 'tonalidade'
    mensagem_de_erro = (
        f'Essa escala não existe ou não foi implementada. Tente uma dessas '
        f'{list(ESCALAS.keys())}'
    )

    with raises(KeyError) as error:
        escala(tonica, tonalidade)

    assert mensagem_de_erro == error.value.args[0]


@mark.parametrize(
    'tonica,esperado',
    [
        ('C', ['C', 'D', 'E', 'F', 'G', 'A', 'B']),
        ('C#', ['C#', 'D#', 'F', 'F#', 'G#', 'A#', 'C']),
        ('F', ['F', 'G', 'A', 'A#', 'C', 'D', 'E']),
    ],
)
def test_deve_retornar_notas_corretas(tonica, esperado):
    resultado = escala(tonica, 'maior')
    assert resultado['notas'] == esperado


def test_deve_retornar_os_sete_grau():
    tonica = 'c'
    tonalidade = 'maior'
    esperado = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']

    resultado = escala(tonica, tonalidade)
    assert resultado['graus'] == esperado
