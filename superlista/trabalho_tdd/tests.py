from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time

MAX_WAIT = 10


class NewVsitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    # Auxiliary method
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except(AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_trabalho_tdd(self):

        self.browser.get(self.live_server_url)

        # Edith ouviu falar que agora a aplicação online de lista de tarefas
        # aceita definir prioridades nas tarefas do tipo baixa, média e alta
        # Ela decide verificar a homepage
        baixa = self.browser.find_element_by_xpath('//label[@for="baixa"]').text
        self.assertIn('Baixa', baixa)
        media = self.browser.find_element_by_xpath('//label[@for="media"]').text
        self.assertIn('Média', media)
        alta = self.browser.find_element_by_xpath('//label[@for="alta"]').text
        self.assertIn('Alta', alta)

        # Ela percebe que o título da página e o cabeçalho mencionam
        # listas de tarefas com prioridade (priority to-do)

        self.assertIn('Lista de Tarefas com Prioridades', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Lista de Tarefas com Prioridades', header_text)

        # Ela é convidada a inserir um item de tarefa e a prioridade da
        # mesma imediatamente
        # Ela digita "Comprar anzol" em uma nova caixa de texto
        # e assinala prioridade alta no campo de seleção de prioridades
        inputbox = self.browser.find_element_by_id('id_new_item')

        inputbox.send_keys('Comprar anzol')

        ckalta = self.browser.find_element_by_id('alta')
        ckalta.click()

        # Quando ela tecla enter, a página é atualizada, e agora
        # a página lista "1 - Comprar anzol - prioridade alta"
        # como um item em uma lista de tarefas

        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1 Comprar anzol Alta')

        # Ainda continua havendo uma caixa de texto convidando-a a
        # acrescentar outro item. Ela insere "Comprar cola instantâne"
        # e assinala prioridade baixa pois ela ainda tem cola suficiente
        # por algum tempo

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Comprar cola instantânea')

        ckbaixa = self.browser.find_element_by_id('baixa')
        ckbaixa.click()

        inputbox.send_keys(Keys.ENTER)

        # A página é atualizada novamente e agora mostra os dois
        # itens em sua lista e as respectivas prioridades

        self.wait_for_row_in_list_table('1 Comprar anzol Alta')
        self.wait_for_row_in_list_table('2 Comprar cola instantânea Baixa')

        # Edith se pergunta se o site lembrará de sua lista. Então
        # ela nota que o site gerou um URL único para ela -- há um
        # pequeno texto explicativo para isso.

        edith_url = self.browser.current_url
        edith_id = edith_url.split('/')[-1]

        # Ela acessa essa URL -- sua lista de tarefas continua lá.

        self.browser.quit()
        self.browser = webdriver.Firefox()
        self.browser.get('/'.join([self.live_server_url, edith_id]))

        self.wait_for_row_in_list_table('1 Comprar anzol Alta')
        self.wait_for_row_in_list_table('2 Comprar cola instantânea Baixa')

        ################################# FIM ####################################