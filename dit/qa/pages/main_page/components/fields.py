from typing import List

from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Fields']


class FieldWrapper(ComponentWrapper):
    label = Text(css='[class*="x-form-item-label"]')
    value_field = Component(tag='input')


class Fields(Components):
    def __get__(self, instance, owner) -> List[FieldWrapper]:
        ret: List[FieldWrapper] = []

        for webelement in self.finds(instance):
            ret.append(FieldWrapper(instance.app, webelement, self._locator))

        return ret
