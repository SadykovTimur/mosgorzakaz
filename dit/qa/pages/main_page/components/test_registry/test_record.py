from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

__all__ = ['TestRecord']


class TestRecordWrapper(ComponentWrapper):
    title = Text(css='[id*="header-title-text"]')
    close = Button(css='[class*="x-tool-close"]')
    save = Button(xpath='//span[text()="Сохранить"]')
    name = TextField(tag='input')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.title == 'Тестовая запись'
                assert self.close.visible
                assert self.save.visible

                return self.name.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Modal was not loaded')
        self.app.restore_implicitly_wait()


class TestRecord(Component):
    def __get__(self, instance, owner) -> TestRecordWrapper:
        return TestRecordWrapper(instance.app, self.find(instance), self._locator)
