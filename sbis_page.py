from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os
class locators:
    CONTACTS=(By.CSS_SELECTOR, "div.js-ContactsMenu")
    MORE_CONTACTS=(By.CSS_SELECTOR, "a.sbisru-link[href='/contacts']")
    TIMEOUT=10
    BANNER_TENSOR=(By.CSS_SELECTOR, "div.sbisru-Contacts__border-left--border-xm a")
    POWER_IN_MEN=(By.XPATH, "//p[text()='Сила в людях']")
    TO_TENSOR_ABOUT=(By.CSS_SELECTOR, "a.tensor_ru-Index__link[href='/about']")
    OUR_WORK=(By.XPATH, "//h2[text()='Работаем']")
    IMG=(By.CSS_SELECTOR, "img.tensor_ru-About__block3-image.loaded")
    CONTACTS_PARTNERS=(By.CSS_SELECTOR, "div.sbisru-Contacts-List__col")
    REGION_CHOOSE=(By.CSS_SELECTOR, "div.s-Grid-col--xm12 span.sbis_ru-Region-Chooser__text.sbis_ru-link")
    KAMCHATKA=(By.CSS_SELECTOR, "span[title='Камчатский край']")
    FOOTAGE_DOWNLOAD=(By.CSS_SELECTOR, "a.sbisru-Footer__link[href='/download']")
    DOWNLOAD_PLUGIN_WEB_BUTTON=(By.CSS_SELECTOR, "a[href='https://update.saby.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']")
class SbisPage(BasePage):
    def go_to_contacts(self):
        contact_button=self.element_clickable(locators.CONTACTS, locators.TIMEOUT)
        contact_button.click()
        contact_button=self.element_clickable(locators.MORE_CONTACTS, locators.TIMEOUT)
        contact_button.click()
    def go_to_tensor(self):
        time.sleep(3)
        tensor_button=self.element_clickable(locators.BANNER_TENSOR, locators.TIMEOUT)
        tensor_button.click()
        new_window=self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
    def go_to_about_in_block_power_in_men(self):
        button_about=self.element_is_visible(locators.POWER_IN_MEN, locators.TIMEOUT)
        self.scroll_to(button_about)
        about_button=self.element_clickable(locators.TO_TENSOR_ABOUT, locators.TIMEOUT)
        about_button.click()
    def go_to_our_work(self):
        elem_our_work=self.element_is_located(locators.OUR_WORK, locators.TIMEOUT)
        self.scroll_to(elem_our_work)
    def size_of_img(self):
        sizes={}
        arr_of_img=self.find_elements(locators.IMG, locators.TIMEOUT)
        for img in arr_of_img:
            width=img.get_attribute('width')
            height=img.get_attribute('height')
            sizes[img]=(width, height)
        for i in range(len(arr_of_img)-1):
            if sizes[arr_of_img[i]]!=sizes[arr_of_img[i+1]]:
                print(f"Некорректные {i}/{i+1}")
                return False
        return True
    def is_region_correct(self):
        current_region=self.element_is_visible(locators.REGION_CHOOSE, locators.TIMEOUT)
        return current_region.text
    def is_contacts_present(self):
        return self.element_is_visible(locators.CONTACTS_PARTNERS, locators.TIMEOUT)
    def go_to_choose_region(self):
        region_change=self.element_clickable(locators.REGION_CHOOSE, locators.TIMEOUT)
        region_change.click()
        kamchatka=self.element_clickable(locators.KAMCHATKA, locators.TIMEOUT)
        kamchatka.click()
        self.element_clickable(locators.REGION_CHOOSE, locators.TIMEOUT)
    def go_to_footage_download(self):
        footage_download_button=self.element_is_located(locators.FOOTAGE_DOWNLOAD, locators.TIMEOUT)
        self.scroll_to(footage_download_button)
        footage_download_button=self.element_clickable(locators.FOOTAGE_DOWNLOAD, locators.TIMEOUT)
        footage_download_button.click()
    def download_web_plugin(self):
        download_web_plugin_button=self.element_clickable(locators.DOWNLOAD_PLUGIN_WEB_BUTTON, locators.TIMEOUT)
        download_web_plugin_button.click()
    def getsize_plugin_page(self):
        element=self.element_clickable(locators.DOWNLOAD_PLUGIN_WEB_BUTTON, locators.TIMEOUT)
        size=element.text
        size=size[size.find('Exe')+3:size.find('МБ')]
        return size
    def check_plugin_size(self):
        path_plugin=os.path.dirname(os.path.abspath(__file__))
        path_plugin=path_plugin+'/sbisplugin-setup-web.exe'
        try:
            assert os.path.exists(path_plugin), 'Не скачался за разумное время'
        except:
            return False
        current_size=round(os.path.getsize(path_plugin)/(1024*1024), 2)
        size_from_site=self.getsize_plugin_page() 
        try:
            assert size_from_site==current_size, 'Некорректный размер'
        except:
            return False
        return True
    def check_region_kamchatka_in_title(self):
        try:
            assert 'Камчатский' in self.driver.title, 'Отсутствует информация о регионе в заголовке'
        except:
            return False
        return True
    def check_region_kamchatka(self):
        try:
            assert self.is_region_correct()=='Камчатский край'
        except:
            return False
        return True