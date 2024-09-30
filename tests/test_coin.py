from src.coins import Coin


def test_create_coin():
    coin = Coin(current_side="Zahl")
    assert isinstance(coin) == Coin


def test_coin_flip():
    coin = Coin(current_side="Zahl")
    coin.flip_coin()
    assert "Kopf" == coin.current_side


def test_get_side():
    coin = Coin(current_side="Zahl")
    assert coin.get_side() == "Zahl"


def test_set_side():
    coin = Coin(current_side="Zahl")
    coin.set_side(side="Kopf")
    assert "Kopf" == coin.current_side
