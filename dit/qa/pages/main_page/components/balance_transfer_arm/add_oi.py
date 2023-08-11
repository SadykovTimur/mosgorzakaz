from typing import List

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

__all__ = ['AddOI']


class FieldWrapper(ComponentWrapper):
    title = Text(tag='label')
    input = Component(tag='input')
    search = Button(css='[class*="x3-form-search-trigger"]')
    clear = Button(css='[class*="x3-form-clear-trigger"]')


class Fields(Components):
    def __get__(self, instance, owner) -> List[FieldWrapper]:
        ret: List[FieldWrapper] = []

        for webelement in self.finds(instance):
            ret.append(FieldWrapper(instance.app, webelement, self._locator))

        return ret


class AddOIWrapper(ComponentWrapper):
    title = Text(class_name='x3-window-header-text')
    close = Button(css='[class*="x3-tool-close"]')
    save = Button(css='[class*="icon-accept"]')
    fields = Fields(class_name='x3-form-item ')

    def choose_field(self, name: str) -> FieldWrapper:
        for field in self.fields:
            if field.title == name:
                return field

        raise AttributeError('Field was not found')

    def wait_for_filling(self, field_name: str, field_value: str) -> None:
        def condition() -> bool:
            try:
                return self.choose_field(field_name).input.value == field_value

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Field was not filled')
        self.app.restore_implicitly_wait()

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.title == 'Добавить объект имущества'
                assert self.close.visible
                assert self.save.visible

                return self.fields[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Modal was not loaded')
        self.app.restore_implicitly_wait()


class AddOI(Component):
    def __get__(self, instance, owner) -> AddOIWrapper:
        return AddOIWrapper(instance.app, self.find(instance), self._locator)
