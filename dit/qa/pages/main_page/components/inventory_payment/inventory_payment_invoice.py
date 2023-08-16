from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.main_page.components.fields import Fields

__all__ = ['InventoryPaymentInvoice']


class InventoryPaymentInvoiceWrapper(ComponentWrapper):
    title = Component(xpath='//div[contains(@class, "x-title-item") and text()="Опись счетов на оплату"]')
    close = Button(css='[class*="x-tool-close"]')
    save = Button(xpath='//span[text()="Сохранить"]')
    print = Button(xpath='//span[text()="Печать"]')
    give_to_payment = Button(xpath='//span[text()="Передать на оплату"]')
    fields = Fields(css='[class*="x-form-type-text"]')
    invoices_for_payment = Component(xpath='//div[text()="Счета на оплату"]')
    invoices = Components(css='[class*="OpenPayment"]')

    def field_value(self, name: str) -> str:
        for f in self.fields:
            if f.label == name:
                return f.value_field.value

        raise AttributeError('Field was not found')

    def wait_for_loading(self, new: bool = True) -> None:
        def condition() -> bool:
            try:
                assert self.title.visible
                assert self.close.visible
                assert self.save.visible
                assert self.print.visible
                assert self.give_to_payment.visible

                doc_number = self.field_value('Номер документа:')
                doc_date = self.field_value('Дата документа:')

                if new:
                    assert doc_number == ''
                    assert doc_date != ''
                else:
                    assert doc_number != ''
                    assert doc_date != ''
                    assert self.invoices[0].visible

                return self.invoices_for_payment.visible

            except NoSuchElementException:
                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Modal was not loaded', timeout=40)
        self.app.restore_implicitly_wait()


class InventoryPaymentInvoice(Component):
    def __get__(self, instance, owner) -> InventoryPaymentInvoiceWrapper:
        return InventoryPaymentInvoiceWrapper(instance.app, self.find(instance), self._locator)
