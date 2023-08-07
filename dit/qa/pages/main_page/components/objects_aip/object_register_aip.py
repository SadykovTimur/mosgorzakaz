from typing import List

from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text

__all__ = ['ObjectRegisterAIP']


class TopWrapper(ComponentWrapper):
    add = Button(xpath='//span[text()="Добавить"]')
    update = Button(xpath='//span[text()="Обновить"]')
    print = Button(xpath='//span[text()="Печать"]')
    operations = Button(xpath='//span[text()="Операции"]')
    map = Button(xpath='//span[text()="Карта"]')
    electoral_map = Button(xpath='//span[text()="Карта избирательных участков   "]')
    clear_filter = Button(xpath='//span[text()="Очистить фильтр"]')
    sort = Button(xpath='//span[text()="Сортировка"]')
    reset_settings = Button(xpath='//span[text()="Сбросить настройки"]')


class Top(Component):
    def __get__(self, instance, owner) -> TopWrapper:
        return TopWrapper(instance.app, self.find(instance), self._locator)


class RowWrapper(ComponentWrapper):
    attributes = Button(css='[class*="ShowAttributeWindow"]')
    edit = Button(css='[data-qtip="Редактировать"]')
    kg = Component(css='[class*="ShowSchedule"]')
    name = Text(css='[data-columnid="columnName"]')


class Rows(Components):
    def __get__(self, instance, owner) -> List[RowWrapper]:
        ret: List[RowWrapper] = []

        for webelement in self.finds(instance):
            ret.append(RowWrapper(instance.app, webelement, self._locator))

        return ret


class BodyLockedWrapper(ComponentWrapper):
    rows = Rows(css='[class*="x-grid-row"]')


class BodyLocked(Component):
    def __get__(self, instance, owner) -> BodyLockedWrapper:
        return BodyLockedWrapper(instance.app, self.find(instance), self._locator)


class ObjectRegisterAIPWrapper(ComponentWrapper):
    top = Top(css='[class*="x-tree-lines"] [class*="toolbar-docked-top"]')
    body_normal = Component(css='[class*="grid-inner-normal"]')
    body_locked = BodyLocked(css='[class*="grid-inner-locked"]')
    bottom = Component(css='[class*="toolbar-docked-bottom"]')


class ObjectRegisterAIP(Component):
    def __get__(self, instance, owner) -> ObjectRegisterAIPWrapper:
        return ObjectRegisterAIPWrapper(instance.app, self.find(instance), self._locator)
