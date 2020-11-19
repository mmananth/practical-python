from typing import Type
from typedproperty import typedproperty, String, Integer, Float

class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    #__slots__ = ('name','_shares','price')
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self) -> str:
        return f'Stock({self.name!r},{self.shares!r},{self.price!r})'

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self,value):
        if not isinstance(value,int):
            raise TypeError('Expected int')
        self._shares = value

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self,numshares):
        self.shares -= numshares

class MyStock(Stock):
    def panic(self):
        self.sell(self.shares)

import fileparse
import sys

def main(args):
    global portDicts, portfolio
    portDicts = {}
    with open(args[1]) as lines:
        portDicts = fileparse.parse_csv(lines, select=['name','shares','price'], types=[str,int,float])

    portfolio = [Stock(d['name'],d['shares'],d['price']) for d in portDicts]

if __name__ == '__main__':
    main(sys.argv)