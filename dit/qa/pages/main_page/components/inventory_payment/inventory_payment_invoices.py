import time
from typing import Any, Dict, List

import selenium.webdriver.support.expected_conditions as ec
from coms.qa.core.helpers import wait_for
from coms.qa.frontend.helpers.custom_wait_conditions import ElementToBeClickable
from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

__all__ = ['InventoryPaymentInvoices']


class TopWrapper(ComponentWrapper):
    add = Button(xpath='//span[text()="Добавить"]')
    update = Button(xpath='//span[text()="Обновить"]')
    print = Button(xpath='//span[text()="Печать"]')
    clear_filter = Button(xpath='//span[text()="Очистить фильтр"]')
    reset_settings = Button(xpath='//span[text()="Сбросить настройки"]')


class Tops(Components):
    def __get__(self, instance, owner) -> List[TopWrapper]:
        ret: List[TopWrapper] = []

        for webelement in self.finds(instance):
            ret.append(TopWrapper(instance.app, webelement, self._locator))

        return ret


class InputSelectorWrapper(ComponentWrapper):
    input = TextField(tag='input')
    select = Button(css='[id*="trigger-picker"]')


class InputSelectors(Components):
    def __get__(self, instance, owner) -> List[InputSelectorWrapper]:
        ret: List[InputSelectorWrapper] = []

        for webelement in self.finds(instance):
            ret.append(InputSelectorWrapper(instance.app, webelement, self._locator))

        return ret


class FilterFormWrapper(ComponentWrapper):
    submit = Button(xpath='//span[text()="Применить фильтр"]')
    clear = Button(xpath='//span[text()="Очистить фильтр"]')
    saved_filters = InputSelectors(
        xpath='//input[contains(@id, "eascombobox")]/ancestor::div[contains(@id, "triggerWrap")]'
    )
    fields = InputSelectors(
        xpath='//input[@placeholder="Выберите поле..."]/ancestor::div[contains(@id, "triggerWrap")]'
    )
    operations = InputSelectors(
        xpath='//input[@placeholder="Выберите операцию..."]/ancestor::div[contains(@id, "triggerWrap")'
    )
    negatives = Components(css='[data-qtip="Отрицание"]')
    value_fields = Components(css='[placeholder="Введите значение..."]')
    add_condition = Components(css='[data-qtip="Добавить условие"]')

    def choose_item(self, name: str) -> None:
        items = self.driver.find_elements(By.CLASS_NAME, 'x-boundlist-item')
        for item in items:
            if item.text == name:
                self.wait.until(ElementToBeClickable(element=item))
                item.click()

                return

        raise AttributeError('Item was not found')

    def choose_menu_item(self, name: str) -> None:
        items = self.driver.find_elements(By.CSS_SELECTOR, '[class*="x-menu-item-text"]')
        for item in items:
            if item.text == name:
                self.wait.until(ElementToBeClickable(element=item))
                item.click()

                return

        raise AttributeError('Item was not found')

    def fill_filter(self, filters: Dict[str, Any]) -> None:
        items = filters.items()

        for i, f in enumerate(items, 1):
            self.fields[-1].select.wait_for_clickability().click()
            time.sleep(0.5)
            self.choose_item(f[0])
            time.sleep(0.5)
            self.value_fields[-1].webelement.send_keys(f[1])

            if i != len(items):
                tip = self.driver.find_element(By.ID, 'ext-quicktips-tip-innerCt')
                self.add_condition[-1].wait_for_clickability().click()
                self.wait.until(ec.invisibility_of_element(tip))  # type: ignore
                self.choose_menu_item('И')


class FilterForm(Component):
    def __get__(self, instance, owner) -> FilterFormWrapper:
        return FilterFormWrapper(instance.app, self.find(instance), self._locator)


class RowWrapper(ComponentWrapper):
    edit = Button(css='[data-qtip="Редактировать"]')
    remove = Button(css='[data-qtip="Удалить"]')


class Rows(Components):
    def __get__(self, instance, owner) -> List[RowWrapper]:
        ret: List[RowWrapper] = []

        for webelement in self.finds(instance):
            ret.append(RowWrapper(instance.app, webelement, self._locator))

        return ret


class BodyWrapper(ComponentWrapper):
    rows = Rows(css='[class*="x-grid-row"]')

    def check_found_inventories(self, number: int, summ: int) -> None:
        def condition() -> bool:
            try:
                assert len(self.rows) > 0

                for row in self.rows:
                    assert str(number) in row.webelement.text
                    assert str(summ) in row.webelement.text.replace(' ', '')

                return True
            except NoSuchElementException:
                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Inventories was not found')
        self.app.restore_implicitly_wait()


class Body(Component):
    def __get__(self, instance, owner) -> BodyWrapper:
        return BodyWrapper(instance.app, self.find(instance), self._locator)


class InventoryPaymentInvoicesWrapper(ComponentWrapper):
    tops = Tops(css='[class*="toolbar-docked-top"]')
    head = Component(css='[class*="x-box-item"] [class*="x-grid-head"]')
    body = Body(css='[class*="x-summary-bottom"]')
    bottom = Component(css='[class*="x-box-item"] [class*="toolbar-docked-bottom"]')
    filter_btn = Button(xpath='//div[text()="Фильтр"]')
    filter_form = FilterForm(css='[class*="queryBuilder"]')

    @property
    def filter_form_is_expanded(self) -> bool:
        return bool(self.filter_form.webelement.get_attribute('aria-expanded'))

    def expand_filter_form(self) -> None:
        if not self.filter_form_is_expanded:
            self.filter_btn.wait_for_clickability().click()


class InventoryPaymentInvoices(Component):
    def __get__(self, instance, owner) -> InventoryPaymentInvoicesWrapper:
        return InventoryPaymentInvoicesWrapper(instance.app, self.find(instance), self._locator)
