from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Organizations']


class TopWrapper(ComponentWrapper):
    add = Button(xpath='//span[text()="Добавить"]')
    update = Button(xpath='//span[text()="Обновить"]')
    union = Button(xpath='//span[text()="Объединение организаций"]')
    import_btn = Button(xpath='//span[text()="Импорт"]')
    change_org_form = Button(xpath='//span[text()="Смена орг.формы"]')
    clear_filter = Button(xpath='//span[text()="Очистить фильтр"]')


class Top(Component):
    def __get__(self, instance, owner) -> TopWrapper:
        return TopWrapper(instance.app, self.find(instance), self._locator)


class OrganizationsWrapper(ComponentWrapper):
    top = Top(css='[class*="toolbar-docked-top"]')
    header = Component(css='[class*="grid-header"]')
    body = Component(css='[class*="grid-body"]')
    bottom = Component(css='[class*="toolbar-docked-bottom"]')


class Organizations(Component):
    def __get__(self, instance, owner) -> OrganizationsWrapper:
        return OrganizationsWrapper(instance.app, self.find(instance), self._locator)
