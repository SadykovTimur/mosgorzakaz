from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from selenium.common.exceptions import NoSuchElementException

__all__ = ['MainMenu']


class MenuWrapper(ComponentWrapper):
    items = Components(css='div[class*="main-menu-item"]')

    def choose_item(self, name: str) -> None:
        for item in self.items:
            if item.webelement.text == name.upper():
                item.wait_for_clickability()
                item.webelement.click()

                return

        raise AttributeError('Menu item was not found')


class Menu(Component):
    def __get__(self, instance, owner) -> MenuWrapper:
        return MenuWrapper(instance.app, self.find(instance), self._locator)


class SubMenuWrapper(ComponentWrapper):
    items = Components(css='a[class*="main-menu-submenu-item"]')

    def choose_item(self, name: str) -> None:
        for item in self.items:
            if item.webelement.text == name:
                item.wait_for_clickability()
                item.webelement.click()

                return

        raise AttributeError('Submenu item was not found')


class SubMenu(Component):
    def __get__(self, instance, owner) -> SubMenuWrapper:
        return SubMenuWrapper(instance.app, self.find(instance), self._locator)


class MainMenuWrapper(ComponentWrapper):
    menu = Menu(css='[data-componentid="topmenuPanel"]')
    submenu = SubMenu(css='[class*="main-menu-submenu-body"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.menu.visible

                return self.submenu.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Menu was not loaded')
        self.app.restore_implicitly_wait()


class MainMenu(Component):
    def __get__(self, instance, owner) -> MainMenuWrapper:
        return MainMenuWrapper(instance.app, self.find(instance), self._locator)
