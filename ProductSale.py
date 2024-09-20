from __future__ import annotations
from typing import List

# Forward reference for class Sale
class Product:
    __lastSale: Sale = None
    __inventory: int = 0  # Attribute to track inventory

    def __init__(self, inventory: int = 0):
        self.__inventory = inventory

    def setLastSale(self, lastSale: Sale):
        self.__lastSale = lastSale

    @property
    def getLastSale(self) -> Sale:
        return self.__lastSale

    @property
    def getInventory(self) -> int:
        return self.__inventory

    def decreaseInventory(self, amount: int):
        if self.__inventory >= amount:
            self.__inventory -= amount
        else:
            raise ValueError(f"Not enough inventory to sell {amount} units. Current inventory: {self.__inventory}")

# No forward reference needed since Product is already defined
class Sale:
    __saleCounter = 0  # Static variable to track number of sales
    __productSold: List[Product] = None

    def __init__(self, products: List[Product], quantities: List[int]):
        Sale.__saleCounter += 1
        self.__saleNumber = Sale.__saleCounter
        self.__productSold = products

        for index, product in enumerate(products):
            product.decreaseInventory(quantities[index])
            product.setLastSale(self)

    @property
    def getSaleNumber(self) -> int:
        return self.__saleNumber

# Example usage

productOne = Product(inventory=100)
productTwo = Product(inventory=50)

# Sale 1: Selling 5 units of productOne and 3 units of productTwo
saleOne = Sale([productOne, productTwo], [5, 3])

# Sale 2: Selling 2 units of productOne
saleTwo = Sale([productOne], [2])

print(f"ProductOne Inventory: {productOne.getInventory}, Last Sale Number: {productOne.getLastSale.getSaleNumber}")
print(f"ProductTwo Inventory: {productTwo.getInventory}, Last Sale Number: {productTwo.getLastSale.getSaleNumber}")
