from typing import List

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

__all__ = ['Reports', 'ReportsMenu']


class TopWrapper(ComponentWrapper):
    add = Button(xpath='//button[text()="Добавить"]')
    update = Button(xpath='//button[text()="Обновить"]')
    clear_filter = Button(xpath='//button[text()="Очистить фильтр"]')
    group = Button(xpath='//button[text()="Группировка"]')


class Tops(Components):
    def __get__(self, instance, owner) -> List[TopWrapper]:
        ret: List[TopWrapper] = []

        for webelement in self.finds(instance):
            ret.append(TopWrapper(instance.app, webelement, self._locator))

        return ret


class RowWrapper(ComponentWrapper):
    edit = Button(css='[ext:qtip="Редактировать"]')
    remove = Button(css='[ext:qtip="Удалить"]')

    def open_report_menu(self) -> None:
        self.wait_for_clickability()
        actions = ActionChains(self.driver)  # type: ignore
        actions.double_click(self.webelement).perform()  # type: ignore


class Rows(Components):
    def __get__(self, instance, owner) -> List[RowWrapper]:
        ret: List[RowWrapper] = []

        for webelement in self.finds(instance):
            ret.append(RowWrapper(instance.app, webelement, self._locator))

        return ret


class ReportsMenuWrapper(ComponentWrapper):
    items = Components(class_name='x3-menu-list-item')

    def choose_item(self, name: str) -> None:
        for item in self.items:
            if item.text == name:
                item.wait_for_clickability()
                item.webelement.click()

                return

        raise AttributeError('Item was not found')


class ReportsMenu(Component):
    def __get__(self, instance, owner) -> ReportsMenuWrapper:
        return ReportsMenuWrapper(instance.app, self.find(instance), self._locator)


class BodyWrapper(ComponentWrapper):
    rows = Rows(css='[class*="x3-grid3-row"]')

    def check_found_reports(self, report_name: str) -> None:
        def condition() -> bool:
            try:
                assert len(self.rows) > 0

                for row in self.rows:
                    assert str(report_name) in row.webelement.text

                return True
            except NoSuchElementException:
                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Reports was not found')
        self.app.restore_implicitly_wait()


class Body(Component):
    def __get__(self, instance, owner) -> BodyWrapper:
        return BodyWrapper(instance.app, self.find(instance), self._locator)


class TableFilterWrapper(ComponentWrapper):
    title = Text(css='[class*="hd-columnName"]')
    input = TextField(tag='input')


class TableFilter(Component):
    def __get__(self, instance, owner) -> TableFilterWrapper:
        return TableFilterWrapper(instance.app, self.find(instance), self._locator)


class TableHeaderWrapper(ComponentWrapper):
    name = TableFilter(css='[class*="td-columnName"]')


class TableHeader(Component):
    def __get__(self, instance, owner) -> TableHeaderWrapper:
        return TableHeaderWrapper(instance.app, self.find(instance), self._locator)


class ReportsWrapper(ComponentWrapper):
    tops = Tops(css='[class*="panel-tbar"]')
    header = TableHeader(class_name='x3-grid3-header')
    body = Body(css='[class="x3-grid3-body"]')
    bottom = Component(class_name='x3-panel-bbar')
    filter_btn = Button(xpath='//div[contains(@class, "panel-header-rotated")]')


class Reports(Component):
    def __get__(self, instance, owner) -> ReportsWrapper:
        return ReportsWrapper(instance.app, self.find(instance), self._locator)
