from seleniumbase import BaseCase
import csv

class AutomatizacaoSwagLabs(BaseCase):
    def login(self):
        self.open("https://www.saucedemo.com/")
        self.type("#user-name", "standard_user")
        self.type("#password", "secret_sauce")
        self.click("#login-button")
        #self.wait_for_url("https://www.saucedemo.com/inventory.html")

    #def extracao_dados_produtos(self):

    def adicionar_ao_carrinho(self):
        self.click("#add-to-cart-sauce-labs-backpack")
        self.click("#add-to-cart-sauce-labs-bike-light")
        self.click("#add-to-cart-sauce-labs-bolt-t-shirt")
        self.click("#add-to-cart-sauce-labs-fleece-jacket")
        self.click("#add-to-cart-sauce-labs-onesie")
        self.click('[data-test="add-to-cart-test.allthethings()-t-shirt-(red)"]')


    def finalizar_compra(self):
        self.click("#shopping_cart_container")
        #self.wait_for_url("https://www.saucedemo.com/cart.html")

        self.click("#checkout")
        #self.wait_for_url("https://www.saucedemo.com/checkout-step-one.html")

        self.type("#first-name", "Trainee")
        self.type("#last-name", "PiJunior")
        self.type("#postal-code", "31270-901")

        self.click("#continue")
        #self.wait_for_url("https://www.saucedemo.com/checkout-step-two.html")

        pagamento = self.get_text("[data-test='payment-info-value']")
        entrega = self.get_text("[data-test='shipping-info-value']")
        valor_total = self.get_text("[data-test='total-label']")

        print("Pagamento:", pagamento)
        print("Entrega:", entrega)
        print("Valor total:", valor_total)

        self.click("#finish")
        #self.wait_for_url("https://www.saucedemo.com/checkout-complete.html")
        
        mensagem = self.get_text(".complete-header")
        self.assert_equal(mensagem, "Thank you for your order!")

    def test_tudo(self):
        self.login()
        #self.extracao_dados_produtos()
        self.adicionar_ao_carrinho()
        self.finalizar_compra()