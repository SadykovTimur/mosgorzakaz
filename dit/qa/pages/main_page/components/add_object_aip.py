from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

__all__ = ['AddObjectAIP']


class AddObjectAIPWrapper(ComponentWrapper):
    title = Component(xpath='//div[text()="Добавить объект АИП"]')
    close = Button(css='[class*="x-tool-close"]')
    save = Button(xpath='//span[text()="Сохранить"]')
    parent_object = Component(xpath='//span[text()="Объект - родитель:"]')
    copy_data = Component(xpath='//label[text()="Скопировать данные"]')
    project_head = Component(xpath='//label[text()="Руководитель проекта"]')
    industry = Component(xpath='//label[text()="Отрасль"]')
    organizations = Component(xpath='//label[text()="Организации"]')
    name = Components(xpath='//span[text()="Наименование:"]')
    address = Components(xpath='//span[text()="Адрес:"]')
    prefect = Components(xpath='//span[text()="Префектура:"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.title.visible
                assert self.close.visible
                assert self.save.visible
                assert self.parent_object.visible
                assert self.copy_data.visible
                assert self.project_head.visible
                assert self.industry.visible
                assert self.organizations.visible
                assert self.name[-1].visible
                assert self.address[-1].visible

                return self.prefect[1].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Modal was not loaded')
        self.app.restore_implicitly_wait()


class AddObjectAIP(Component):
    def __get__(self, instance, owner) -> AddObjectAIPWrapper:
        return AddObjectAIPWrapper(instance.app, self.find(instance), self._locator)
