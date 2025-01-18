from sbis_page import SbisPage, locators
import time
def test_tensor(browser):
    sbis_page=SbisPage(browser, 'https://saby.ru/')
    sbis_page.open()
    sbis_page.go_to_contacts()
    sbis_page.go_to_tensor()
    assert sbis_page.text_in_element_located(locators.POWER_IN_MEN, 'Сила в людях')!=False, 'Нет силы в людях...'
    sbis_page.go_to_about_in_block_power_in_men()
    assert sbis_page.check_url()=='https://tensor.ru/about', 'Попадаем не в https://tensor.ru/about'
    sbis_page.go_to_our_work()
    assert sbis_page.size_of_img()==True, 'Некорректные размеры картинок'
def test_partners_regions(browser):
    sbis_page=SbisPage(browser, 'https://saby.ru/')
    sbis_page.open()
    sbis_page.go_to_contacts()
    assert sbis_page.is_region_correct()=='Ярославская обл.'
    assert sbis_page.is_contacts_present()==True, 'Отсутствуют контакты партнеров'
    sbis_page.go_to_choose_region()
    assert sbis_page.check_region_kamchatka()==True, 'Не поменялся регион на Камчатский край'
    assert sbis_page.is_contacts_present()==True, 'Отсутствуют партнеры после смены региона'
    assert '41-kamchatskij-kraj' in sbis_page.check_url(), 'Некорректный url, нет информации о регионе'
    assert sbis_page.check_region_kamchatka_in_title()==True, 'Отсутствует информация о регионе в заголовке'
def test_plugin(browser_with_option):
    sbis_page=SbisPage(browser_with_option, 'https://saby.ru')
    sbis_page.open()
    sbis_page.go_to_footage_download()
    sbis_page.download_web_plugin()
    time.sleep(10)
    assert sbis_page.check_plugin_size()==True, 'Не найден нужный файл с нужным размером'
