from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['BalanceTransferARM']


class PanelWrapper(ComponentWrapper):
    clear_filter = Button(css='[class*="icon-filterclear"]')
    save = Button(css='[class*="icon-disk"]')
    refresh = Button(css='[class*="icon-arrow-refresh"]')
    print = Button(css='[class*="icon-printer"]')
    config_columns = Button(css='[class*="icon-application-view-columns"]')
    create_oi = Button(css='[class*="icon-house-plus"]')
    create_oaip = Button(xpath='//b[text()="Создать ОАИП"]')
    choose_color = Button(css='[class*="icon-color"]')
    copy_oi = Button(xpath='//b[text()="Копировать ОИ"]')
    comment = Button(css='[class*="icon-comment"]')
    copy_values = Button(css='[class*="icon-copy"]')
    transfer_oi = Button(css='[class*="icon-arrow-right"]')
    operations = Button(css='[class*="icon-cog"]')
    scripts = Button(css='[class*="icon-script-go"]')
    info = Button(css='[class*="icon-information"]')


class Panel(Components):
    def __get__(self, instance, owner) -> PanelWrapper:
        return PanelWrapper(instance.app, self.find(instance), self._locator)


class BalanceTransferARMWrapper(ComponentWrapper):
    panel = Panel(css='[class*="mosks-balance-arm"] [class*="x3-panel-tbar"]')
    header = Component(class_name='x3-grid3-header')
    body = Component(class_name='x3-grid3-body')
    bottom = Component(class_name='x3-panel-bbar')
    filter_btn = Button(xpath='//div[contains(@class, "x3-panel-header-rotated")]/span[text()="Фильтр"]')


class BalanceTransferARM(Component):
    def __get__(self, instance, owner) -> BalanceTransferARMWrapper:
        return BalanceTransferARMWrapper(instance.app, self.find(instance), self._locator)
