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

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith ouviu falar de uma nova aplicação online interessante
        # para lista de tarefas. Ela decide verificar a homepage

        #self.browser.get(self.live_server_url)
        self.browser.get('localhost:8000')

        # Ela percebe que o título da página e o cabeçalho mencionam
        # listas de tarefas (to-do)

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Ela é convidada a inserir um item de tarefa imediatamente

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Ela digita "Buy peacock featers" (Comprar penas de pavão)
        # em uma nova caixa de texto (o hobby de Edith é fazer iscas
        # para pesca com fly)

        inputbox.send_keys('Buy peacock featers')

        # Quando ela tecla enter, a página é atualizada, e agora
        # a página lista "1 - Buy peacock feathers" como um item em
        # uma lista de tarefas

        inputbox.send_keys(Keys.ENTER)
        #time.sleep(1)
        self.wait_for_row_in_list_table('1 Buy peacock featers Low')#('1: Buy peacock featers')

        # Ainda continua havendo uma caixa de texto convidando-a a
        # acrescentar outro item. Ela insere "Use peacock feathers
        # to make a fly" (Usar penas de pavão para fazer um fly -
        # Edith é bem metódica)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        #time.sleep(1)

        # A página é atualizada novamente e agora mostra os dois
        # itens em sua lista
        self.wait_for_row_in_list_table('1 Buy peacock featers Low')#('1: Buy peacock featers')
        self.wait_for_row_in_list_table('2 Use peacock feathers to make a fly Low')#('2: Use peacock feathers to make a fly')

        # Edith se pergunta se o site lembrará de sua lista. Então
        # ela nota que o site gerou um URL único para ela -- há um
        # pequeno texto explicativo para isso.

        #self.fail('Finish the test!')

        # Ela acessa essa URL -- sua lista de tarefas continua lá.

        # Satisfeita, ela volta a dormir

    def test_trabalho_tdd(self):
        # Edith ouviu falar que agora a aplicação online de lista de tarefas
        # aceita definir prioridades nas tarefas do tipo baixa, média e alta
        # Ela decide verificar a homepage

        # Ela percebe que o título da página e o cabeçalho mencionam
        # listas de tarefas com prioridade (priority to-do)

        # Ela é convidada a inserir um item de tarefa e a prioridade da
        # mesma imediatamente

        # Ela digita "Comprar anzol" em uma nova caixa de texto
        # e assinala prioridade alta no campo de seleção de prioridades

        # Quando ela tecla enter, a página é atualizada, e agora
        # a página lista "1 - Comprar anzol - prioridade alta"
        # como um item em uma lista de tarefas

        # Ainda continua havendo uma caixa de texto convidando-a a
        # acrescentar outro item. Ela insere "Comprar cola instantâne"
        # e assinala prioridade baixa pois ela ainda tem cola suficiente
        # por algum tempo

        # A página é atualizada novamente e agora mostra os dois
        # itens em sua lista e as respectivas prioridades

        # Edith se pergunta se o site lembrará de sua lista. Então
        # ela nota que o site gerou um URL único para ela -- há um
        # pequeno texto explicativo para isso.

        # Ela acessa essa URL -- sua lista de tarefas continua lá.

        self.fail('Testes funcionaram!')

        ################################# FIM ####################################