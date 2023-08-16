from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

__all__ = ['Remove']


class RemoveWrapper(ComponentWrapper):
    title = Text(css='[class*="x-title-text"]')
    close = Button(css='[class*="x-tool-close"]')
    yes = Button(xpath='//span[text()="Да"]')
    no = Button(xpath='//span[text()="Нет"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.title == 'Удаление'
                assert self.close.visible
                assert self.yes.visible

                return self.no.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Modal was not loaded')
        self.app.restore_implicitly_wait()


class Remove(Component):
    def __get__(self, instance, owner) -> RemoveWrapper:
        return RemoveWrapper(instance.app, self.find(instance), self._locator)
