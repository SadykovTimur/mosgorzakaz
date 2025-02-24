from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.main_page.components.fields import Fields

__all__ = ['Organization']


class OrganizationWrapper(ComponentWrapper):
    title = Component(xpath='//div[text()="Организация"]')
    save = Button(xpath='//span[text()="Сохранить"]')
    fields = Fields(css='[class*="x-form-type-text"]')
    inn = Component(xpath='//span[text()="ИНН"]')
    kpp = Component(xpath='//span[text()="КПП"]')
    ogrn = Component(xpath='//span[text()="ОГРН:"]')

    def field_value(self, name: str) -> str:
        for f in self.fields:
            if f.label == name:
                return f.value_field.value

        raise AttributeError('Field was not found')

    def wait_for_loading(self, org_form: str) -> None:
        def condition() -> bool:
            try:
                assert self.title.visible
                assert self.save.visible
                assert self.field_value('Орг. форма:') == org_form
                assert self.inn.visible
                assert self.kpp.visible

                return self.ogrn.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Form was not loaded')
        self.app.restore_implicitly_wait()


class Organization(Component):
    def __get__(self, instance, owner) -> OrganizationWrapper:
        return OrganizationWrapper(instance.app, self.find(instance), self._locator)
