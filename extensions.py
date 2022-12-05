import requests
import json
from config import keys

class ConversionException(Exception):
    pass

class CryptoConvertor:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f'Не удалось обработать валюту {quote}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException('Неверно введено количество')

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        total_base = json.loads(r.content)[keys[base]]
        return total_base * amount