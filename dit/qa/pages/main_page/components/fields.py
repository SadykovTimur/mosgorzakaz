from typing import List

from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Fields', 'Field', 'FieldWrapper']


class FieldWrapper(ComponentWrapper):
    label = Text(tag='label')
    value_field = Component(tag='input')
    search = Button(css='[class*="x3-form-search-trigger"]')
    clear = Button(css='[class*="x3-form-clear-trigger"]')


class Field(Component):
    def __get__(self, instance, owner) -> FieldWrapper:
        return FieldWrapper(instance.app, self.find(instance), self._locator)


class Fields(Components):
    def __get__(self, instance, owner) -> List[FieldWrapper]:
        ret: List[FieldWrapper] = []

        for webelement in self.finds(instance):
            ret.append(FieldWrapper(instance.app, webelement, self._locator))

        return ret
