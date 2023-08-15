from typing import List

from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text

__all__ = ['LotsRegister']


class PanelWrapper(ComponentWrapper):
    add = Button(css='[class*="icon-add"]')
    refresh = Button(css='[class*="icon-arrow-refresh"]')
    print = Button(css='[class*="icon-printer"]')
    clear_filter = Button(css='[class*="icon-filterclear"]')
    reset_config = Button(css='[class*="icon-arrow-rotate-anticlockwise"]')
    sort = Button(css='[class*="icon-sorting"]')
    object_aip = Component(xpath='//label[text()="Объект АИП:"]')
    program_aip = Component(xpath='//label[text()="Программа АИП:"]')
    status = Component(xpath='//label[text()="Статус:"]')


class Panel(Components):
    def __get__(self, instance, owner) -> PanelWrapper:
        return PanelWrapper(instance.app, self.find(instance), self._locator)


class RowWrapper(ComponentWrapper):
    edit = Button(css='[class*="icon-pencil"]')
    remove = Button(css='[class*="icon-delete"]')
    lot_number = Text(css='[class*="columnLotNumber"]')


class Rows(Components):
    def __get__(self, instance, owner) -> List[RowWrapper]:
        ret: List[RowWrapper] = []

        for webelement in self.finds(instance):
            ret.append(RowWrapper(instance.app, webelement, self._locator))

        return ret


class BodyWrapper(ComponentWrapper):
    rows = Rows(css='[class*="x3-grid3-row"]')


class Body(Component):
    def __get__(self, instance, owner) -> BodyWrapper:
        return BodyWrapper(instance.app, self.find(instance), self._locator)


class LotsRegisterWrapper(ComponentWrapper):
    panel = Panel(css='[class*="x3-grid-panel"] [class*="x3-panel-tbar"]')
    header = Component(class_name='x3-grid3-header')
    body = Body(class_name='x3-grid3-body')
    bottom = Component(class_name='x3-panel-bbar')
    filter_btn = Button(xpath='//div[contains(@class, "x3-panel-header-rotated")]/span[text()="Фильтр"]')


class LotsRegister(Component):
    def __get__(self, instance, owner) -> LotsRegisterWrapper:
        return LotsRegisterWrapper(instance.app, self.find(instance), self._locator)
