from typing import List

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

__all__ = ['TestRegistry']


class PanelWrapper(ComponentWrapper):
    add = Button(xpath='//span[text()="Добавить"]')
    refresh = Button(xpath='//span[text()="Обновить"]')


class Panel(Components):
    def __get__(self, instance, owner) -> PanelWrapper:
        return PanelWrapper(instance.app, self.find(instance), self._locator)


class RowWrapper(ComponentWrapper):
    edit = Button(css='[data-qtip="Редактировать"]')
    remove = Button(css='[data-qtip="Удалить"]')
    name = Text(css='[class*="text-column"]')
    date = Text(css='[data-columnId*="columnDate"]')


class Rows(Components):
    def __get__(self, instance, owner) -> List[RowWrapper]:
        ret: List[RowWrapper] = []

        for webelement in self.finds(instance):
            ret.append(RowWrapper(instance.app, webelement, self._locator))

        return ret


class BodyWrapper(ComponentWrapper):
    rows = Rows(css='[class*="x-grid-row"]')

    def get_records_name(self) -> List[str]:
        return [r.name for r in self.rows]


class Body(Component):
    def __get__(self, instance, owner) -> BodyWrapper:
        return BodyWrapper(instance.app, self.find(instance), self._locator)


class TestRegistryWrapper(ComponentWrapper):
    panel = Panel(css='[class*="x-toolbar-docked-top"]')
    header = Component(css='[class*="x-grid-header"]')
    body = Body(class_name='x-grid-item-container')

    def check_new_record(self, record_name: str) -> None:
        def condition() -> bool:
            try:
                return record_name in self.body.get_records_name()

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Record was not found')
        self.app.restore_implicitly_wait()

    def check_removed_record(self, records_count: int) -> None:
        def condition() -> bool:
            try:
                return records_count - 1 == len(self.body.rows)

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Record was not removed', timeout=50)
        self.app.restore_implicitly_wait()


class TestRegistry(Component):
    def __get__(self, instance, owner) -> TestRegistryWrapper:
        return TestRegistryWrapper(instance.app, self.find(instance), self._locator)
