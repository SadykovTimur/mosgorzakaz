from typing import Optional

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.main_page.components.fields import Fields, FieldWrapper

__all__ = ['Lots']


class LotsWrapper(ComponentWrapper):
    title = Component(class_name='x3-window-header-text')
    close = Button(css='[class*="x3-tool-close"]')
    maximize = Button(css='[class*="x3-tool-maximize"]')
    save = Button(css='[class*="icon-accept"]')
    purchase = Button(xpath='//button[text()="Закупка"]')
    fields = Fields(css='[class*="x3-form-item"]')
    objects_tab = Component(xpath='//span[text()="Объекты"]/ancestor::li')
    participants_tab = Component(xpath='//span[text()="Участники"]/ancestor::li')
    contracts_tab = Component(xpath='//span[text()="Контракты"]/ancestor::li')
    add = Components(css='[class*="icon-add"]')
    refresh = Button(css='[class*="icon-arrow-refresh"]')

    @property
    def is_objects_tab_active(self) -> bool:
        return 'active' in self.objects_tab.webelement.get_attribute('class')

    @property
    def is_participants_tab_active(self) -> bool:
        return 'active' in self.participants_tab.webelement.get_attribute('class')

    def open_add_object(self) -> None:
        if not self.is_objects_tab_active:
            self.objects_tab.click()

        self.wait_for_object_tab_active()

        el = self.add[0]
        el.wait_for_clickability()
        el.webelement.click()

    def open_add_participant(self) -> None:
        if not self.is_participants_tab_active:
            self.participants_tab.click()

        self.wait_for_participant_tab_active()

        el = self.add[1]
        el.wait_for_clickability()
        el.webelement.click()

    def choose_field(self, name: str) -> FieldWrapper:
        for field in self.fields:
            if field.label == name:
                return field

        raise AttributeError('Field was not found')

    def wait_for_loading(self, lot_number: Optional[str] = None) -> None:
        def condition() -> bool:
            try:
                assert self.title.visible
                assert self.close.visible
                assert self.maximize.visible
                assert self.save.visible
                assert self.purchase.visible
                assert self.fields[0].visible
                assert self.objects_tab.visible
                assert self.participants_tab.visible

                if lot_number:
                    assert self.choose_field('Реестровый номер закупки:').value_field.value == lot_number

                return self.contracts_tab.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Modal was not loaded')
        self.app.restore_implicitly_wait()

    def wait_for_object_tab_active(self) -> None:
        def condition() -> bool:
            try:
                return self.is_objects_tab_active

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Object tab is not active')
        self.app.restore_implicitly_wait()

    def wait_for_participant_tab_active(self) -> None:
        def condition() -> bool:
            try:
                return self.is_participants_tab_active

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Participant tab is not active')
        self.app.restore_implicitly_wait()


class Lots(Component):
    def __get__(self, instance, owner) -> LotsWrapper:
        return LotsWrapper(instance.app, self.find(instance), self._locator)
