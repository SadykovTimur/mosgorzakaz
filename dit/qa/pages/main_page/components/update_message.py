from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['UpdateMessage']


class UpdateMessageWrapper(ComponentWrapper):
    title = Component(xpath='//div[text()="Оповещение об обновлении системы!"]')
    message = Component(css='[class*="x-window-text"]')
    read = Button(xpath='//span[text()="Прочтено"]')
    move_to_msg = Button(xpath='//span[text()="Перейти к сообщению"]')
    close = Button(xpath='//span[text()="Закрыть"]')


class UpdateMessage(Component):
    def __get__(self, instance, owner) -> UpdateMessageWrapper:
        return UpdateMessageWrapper(instance.app, self.find(instance), self._locator)
