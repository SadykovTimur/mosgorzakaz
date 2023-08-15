from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.main_page.components.fields import Fields, FieldWrapper

__all__ = ['PurchaseParticipant']


class PurchaseParticipantWrapper(ComponentWrapper):
    title = Component(class_name='x3-window-header-text')
    close = Button(css='[class*="x3-tool-close"]')
    save = Button(css='[class*="icon-accept"]')
    fields = Fields(css='[class*="x3-form-item"]')

    def choose_field(self, name: str) -> FieldWrapper:
        for field in self.fields:
            if field.label == name:
                return field

        raise AttributeError('Field was not found')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.title.visible
                assert self.close.visible
                assert self.fields[0].visible

                return self.save.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Modal was not loaded')
        self.app.restore_implicitly_wait()


class PurchaseParticipant(Component):
    def __get__(self, instance, owner) -> PurchaseParticipantWrapper:
        return PurchaseParticipantWrapper(instance.app, self.find(instance), self._locator)
