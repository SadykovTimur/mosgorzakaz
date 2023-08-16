from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Notification']


class NotificationWrapper(ComponentWrapper):
    title = Component(xpath='//div[text()="Оповещение"]')
    message = Component(css='[class*="x-window-text"]')
    read = Button(xpath='//span[text()="Прочтено"]')
    move_to_msg = Button(xpath='//span[text()="Перейти к сообщению"]')
    close = Button(xpath='//span[text()="Закрыть"]')


class Notification(Component):
    def __get__(self, instance, owner) -> NotificationWrapper:
        return NotificationWrapper(instance.app, self.find(instance), self._locator)
