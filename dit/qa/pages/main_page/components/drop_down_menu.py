from typing import List

from coms.qa.frontend.pages.component import Components, ComponentWrapper

__all__ = ['DropDownMenus']


class DropDownMenuWrapper(ComponentWrapper):
    items = Components(css='[class*="x-menu-item-text"]')

    def choose_item(self, name: str) -> ComponentWrapper:
        for item in self.items:
            if item.webelement.text == name:
                item.wait_for_clickability()

                return item

        raise AttributeError('Menu item was not found')


class DropDownMenus(Components):
    def __get__(self, instance, owner) -> List[DropDownMenuWrapper]:
        ret: List[DropDownMenuWrapper] = []

        for webelement in self.finds(instance):
            ret.append(DropDownMenuWrapper(instance.app, webelement, self._locator))

        return ret
