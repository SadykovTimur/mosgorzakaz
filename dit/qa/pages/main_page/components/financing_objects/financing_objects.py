from typing import List

from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['FinancingObjects']


class TopWrapper(ComponentWrapper):
    update = Button(xpath='//span[text()="Обновить"]')
    print = Button(xpath='//span[text()="Печать"]')
    reports = Button(xpath='//span[text()="Отчёты"]')
    processing = Button(xpath='//span[text()="Обработка"]')
    reset_settings = Button(xpath='//span[text()="Сбросить настройки"]')
    clear_filter = Button(xpath='//span[text()="Очистить фильтр"]')
    grouping = Button(xpath='//span[text()="Группировка"]')


class Tops(Components):
    def __get__(self, instance, owner) -> List[TopWrapper]:
        ret: List[TopWrapper] = []

        for webelement in self.finds(instance):
            ret.append(TopWrapper(instance.app, webelement, self._locator))

        return ret


class FinancingObjectsWrapper(ComponentWrapper):
    tops = Tops(css='[class*="toolbar-docked-top"]')
    header = Component(css='[class*="grid-header"]')
    body = Component(css='[class*="grid-body"]')
    bottom = Component(css='[class*="toolbar-docked-bottom"]')
    filter_btn = Button(xpath='//div[text()="Фильтр"]')


class FinancingObjects(Component):
    def __get__(self, instance, owner) -> FinancingObjectsWrapper:
        return FinancingObjectsWrapper(instance.app, self.find(instance), self._locator)
