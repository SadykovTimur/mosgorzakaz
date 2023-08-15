from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

__all__ = ['Purchase']


class PurchaseWrapper(ComponentWrapper):
    title = Component(class_name='x3-window-header-text')
    close = Button(css='[class*="x3-tool-close"]')
    maximize = Button(css='[class*="x3-tool-maximize"]')
    save = Button(css='[class*="icon-accept"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.title.visible
                assert self.close.visible
                assert self.maximize.visible

                return self.save.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Modal was not loaded')
        self.app.restore_implicitly_wait()


class Purchase(Component):
    def __get__(self, instance, owner) -> PurchaseWrapper:
        return PurchaseWrapper(instance.app, self.find(instance), self._locator)
