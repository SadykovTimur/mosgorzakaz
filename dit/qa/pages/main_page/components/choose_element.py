from typing import List

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

__all__ = ['ChooseElement']


class BodyWrapper(ComponentWrapper):
    rows = Components(class_name='x3-grid3-row-table')

    def choose_item(self, name: str) -> None:
        for row in self.rows:
            if name in row.webelement.text:

                row.wait_for_clickability()
                row.webelement.click()

                return

        raise AttributeError('Element was not found')


class Body(Components):
    def __get__(self, instance, owner) -> BodyWrapper:
        return BodyWrapper(instance.app, self.find(instance), self._locator)


class ChooseElementWrapper(ComponentWrapper):
    title = Component(class_name='x3-window-header-text')
    close = Button(css='[class*="x3-tool-close"]')
    maximize = Button(css='[class*="x3-tool-maximize"]')
    choose = Button(css='[class*="icon-accept"]')
    search = TextField(css='input[class*="x3-form-text"]')
    body = Body(css='[class*="x3-grid3-body"]')
    bottom = Component(css='[class*="x3-panel-bbar"]')

    def search_element(self, name: str) -> None:
        self.search.send_keys(name)
        self.search.webelement.send_keys(Keys.ENTER)
        self.wait_for_loading()

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.title.visible
                assert self.close.visible
                assert self.maximize.visible
                assert self.choose.visible
                assert self.search.visible

                assert self.body.visible
                assert self.body.rows[0].visible

                return self.bottom.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Modal was not loaded')
        self.app.restore_implicitly_wait()


class ChooseElement(Components):
    def __get__(self, instance, owner) -> List[ChooseElementWrapper]:
        ret: List[ChooseElementWrapper] = []

        for webelement in self.finds(instance):
            ret.append(ChooseElementWrapper(instance.app, webelement, self._locator))

        return ret
