from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

__all__ = ['ObjectAIP']


class ObjectAIPWrapper(ComponentWrapper):
    title = Text(css='[class*="object-aip-caption"]')
    chapters = Component(xpath='//div[text()="Разделы"]')
    general_info = Component(xpath='//span[text()="Общие сведения"]')

    def wait_for_loading(self, object_name: str) -> None:
        def condition() -> bool:
            try:
                assert object_name in self.title
                assert self.chapters.visible

                return self.general_info.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Tab was not loaded')
        self.app.restore_implicitly_wait()


class ObjectAIP(Component):
    def __get__(self, instance, owner) -> ObjectAIPWrapper:
        return ObjectAIPWrapper(instance.app, self.find(instance), self._locator)
