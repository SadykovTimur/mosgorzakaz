from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from selenium.common.exceptions import NoSuchElementException

__all__ = ['ChooseOrgForm']


class ChooseOrgFormWrapper(ComponentWrapper):
    title = Component(xpath='//div[text()="Выбор орг. формы"]')
    close = Component(css='[class*="x-tool-close"]')
    choose = Components(xpath='//span[text()="Выбрать"]')
    items = Components(css='[class*="x-grid-item"]')

    def choose_form(self, name: str) -> None:
        for item in self.items:
            if item.webelement.text == name:
                item.wait_for_clickability()
                item.webelement.click()

                self.choose[-1].wait_for_clickability()
                self.choose[-1].webelement.click()

                return

        raise AttributeError('Org form was not found')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.title.visible
                assert self.close.visible
                assert self.choose[-1].visible

                return len(self.items) > 0

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Form was not loaded')
        self.app.restore_implicitly_wait()


class ChooseOrgForm(Component):
    def __get__(self, instance, owner) -> ChooseOrgFormWrapper:
        return ChooseOrgFormWrapper(instance.app, self.find(instance), self._locator)
