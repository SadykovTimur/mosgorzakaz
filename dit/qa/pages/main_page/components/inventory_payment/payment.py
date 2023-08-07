from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.main_page.components.fields import Fields

__all__ = ['Payment']


class PaymentWrapper(ComponentWrapper):
    title = Component(xpath='//div[text()="Платеж"]')
    close = Button(css='[class*="x-tool-close"]')
    maximize = Button(css='[class*="x-tool-maximize"]')
    save = Button(xpath='//span[text()="Сохранить"]')
    print = Button(xpath='//span[text()="Печать"]')
    state_contract = Button(xpath='//span[text()="Гос. контракт"]')
    fields = Fields(css='[class*="x-form-type-text"]')

    def field_value(self, name: str) -> str:
        for f in self.fields:
            if f.label == name:
                return f.value_field.value

        raise AttributeError('Field was not found')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.title.visible
                assert self.close.visible
                assert self.maximize.visible
                assert self.save.visible
                assert self.print.visible
                assert self.state_contract.visible
                assert self.field_value('Объект ГК/договора:') != ''
                assert self.field_value('ГК/договор:') != ''

                return self.field_value('Дата:') != ''

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Modal was not loaded')
        self.app.restore_implicitly_wait()


class Payment(Component):
    def __get__(self, instance, owner) -> PaymentWrapper:
        return PaymentWrapper(instance.app, self.find(instance), self._locator)
