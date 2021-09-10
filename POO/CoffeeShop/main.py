import abc


class Invoice:
    @abc.abstractmethod
    def print(self):
        """Abstract method to implement"""


class InvoiceA(Invoice):
    def __init__(self, date, total, details):
        self._date = date
        self._total = total
        self._details = details

    def print(self):
        print("*" * 60)
        print(f"Date: {self._date}; Total: {self._total}; Details: {self._details};")
        print("*" * 60)


class InvoiceB(Invoice):
    def __init__(self, modified_by, client_name, shipping_address, tax_code):
        self._modified_by = modified_by
        self._client_name = client_name
        self._shipping_address = shipping_address
        self._tax_code = tax_code

    def print(self):
        print("*" * 120)
        print(f"Modified By: {self._modified_by}; "
              f"Client: {self._client_name}; "
              f"Shipping Address: {self._shipping_address}; "
              f"Tax Code: {self._tax_code}")
        print("*" * 120)


class Country:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


class CoffeeShopFactory:
    @staticmethod
    def make_coffee_shop(country, invoice):
        if country.name == "Bolivia" and isinstance(invoice, InvoiceA):
            return CoffeeShopA("Bolivian Coffee Shop", invoice)
        elif country.name == "Canada" and isinstance(invoice, InvoiceB):
            return CoffeeShopB("An international Coffee Shop", invoice)
        else:
            raise NotImplemented("The given country and invoice are not registered to generate a valid Invoice.")


class CoffeeShop:
    def __init__(self, name, invoice):
        self._name = name
        self._invoice = invoice

    @property
    @abc.abstractmethod
    def invoice(self):
        """Abstract Method to implement"""


class CoffeeShopA(CoffeeShop):
    def invoice(self):
        return self._invoice


class CoffeeShopB(CoffeeShop):
    def invoice(self):
        return self._invoice


if __name__ == "__main__":
    country = Country("Bolivia")
    invoice = InvoiceA(date="09/07/2021", total="15bs", details="Stump town Coffee")
    coffeeShop = CoffeeShopFactory.make_coffee_shop(country, invoice)

    country_2 = Country("Canada")
    invoice_2 = InvoiceB(modified_by="Fernando Gutierrez", client_name="Javier",
                         tax_code=4, shipping_address="101 W Main ST APT101")
    coffeeShop_2 = CoffeeShopFactory.make_coffee_shop(country_2, invoice_2)

    # country_3 = Country("Argentina")
    # invoice_3 = InvoiceA(date="09/07/2021", total="15bs", details="Stump town Coffee2")
    # coffeeShop_3 = CoffeeShopFactory.make_coffee_shop(country_3, invoice_3)

    print(coffeeShop.invoice().print())
    print(coffeeShop_2.invoice().print())
