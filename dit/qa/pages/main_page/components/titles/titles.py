from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Titles']


class PanelWrapper(ComponentWrapper):
    print = Button(xpath='//span[text()="Печать"]')
    import_btn = Button(xpath='//span[text()="Импорт"]')
    export = Button(xpath='//span[text()="Экспорт"]')
    refresh = Button(xpath='//span[text()="Обновить"]')
    clear_filter = Button(css='[id*="easclearfilterbutton"]')
    reset_config = Button(xpath='//span[text()="Сбросить настройки"]')
    group = Button(xpath='//span[text()="Группировка"]')
    sort = Button(xpath='//span[text()="Сортировка"]')


class Panel(Components):
    def __get__(self, instance, owner) -> PanelWrapper:
        return PanelWrapper(instance.app, self.find(instance), self._locator)


class TitlesWrapper(ComponentWrapper):
    panel = Panel(css='[class*="tree-wrap"] [class*="x-toolbar-docked-top"]')
    header = Component(css='[class*="x-grid-header"]')
    body = Component(class_name='x-grid-item-container')
    bottom = Component(css='[id*="pagingtoolbar"]')
    filter_btn = Button(xpath='//div[contains(@class, "x-panel-header")]/div[text()="Фильтр"]')


class Titles(Component):
    def __get__(self, instance, owner) -> TitlesWrapper:
        return TitlesWrapper(instance.app, self.find(instance), self._locator)
