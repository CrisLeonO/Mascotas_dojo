from dog import Perro
from cat import Gato
from mico import Mico
from mascotas import TiposAnimales
from ninja import Ninja

jacko = Perro(
    "Jacko",
    "galleta",
    50,
    20
)

agata = Gato(
    "Agata",
    "galletas",
    50,
    50
)

marcel = Mico(
    "Marcel",
    "banana",
    80,
    100
)

ALIMENTOS = {
    TiposAnimales.PERRO: "hills",
    TiposAnimales.GATO: "chunky",
    TiposAnimales.MICO: "banana"
}

cristina = Ninja(
    "cristina",
    "leon",
    [jacko, agata, marcel],
    "carne",
    ALIMENTOS
)

cristina.alimentar()
cristina.caminar()
cristina.bañar()
