from seleniumbase import BaseCase
import json
from selenium.webdriver.common.by import By

class SwagLabsTest(BaseCase):
    def test_fluxo_completo(self):
        """Teste completo do fluxo do Swag Labs"""
        # Configurações para evitar problemas
        self.DISABLE_LOGGING = True
        self.headless = False  # Altere para True se não quiser ver o navegador
        
        # 1. Login
        self.open("https://www.saucedemo.com/")
        self.type("#user-name", "standard_user")
        self.type("#password", "secret_sauce")
        self.click("#login-button")
        self.assert_element(".inventory_list")
        
        # 2. Extração de dados dos produtos
        produtos = []
        items = self.find_elements(".inventory_item")
        
        for item in items:
            nome = item.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
            descricao = item.find_element(By.CSS_SELECTOR, ".inventory_item_desc").text
            preco = item.find_element(By.CSS_SELECTOR, ".inventory_item_price").text
            
            produtos.append({
                "nome": nome,
                "descricao": descricao,
                "preco": preco
            })
        
        with open('produtos.json', 'w', encoding='utf-8') as f:
            json.dump(produtos, f, indent=4, ensure_ascii=False)
        
        # 3. Adicionar itens ao carrinho
        add_buttons = self.find_elements("button.btn_inventory")
        for btn in add_buttons:
            btn.click()
        
        # 4. Finalizar compra
        self.click(".shopping_cart_link")
        self.click("#checkout")
        
        self.type("#first-name", "Trainee")
        self.type("#last-name", "PiJunior")
        self.type("#postal-code", "31270-901")
        self.click("#continue")
        
        # Validações finais - SELEtores ATUALIZADOS
        payment_info = self.get_text(".summary_info > div:nth-of-type(1)")
        shipping_info = self.get_text(".summary_info > div:nth-of-type(2)")
        total = self.get_text(".summary_total_label")
        
        print(f"\nInformações de pagamento: {payment_info}")
        print(f"Informações de entrega: {shipping_info}")
        print(f"Total: {total}")
        
        self.assert_text("Checkout: Overview", ".title")
        self.click("#finish")
        
        # Verificação final
        self.assert_exact_text("Thank you for your order!", ".complete-header")
        print("\nTeste concluído com sucesso!")