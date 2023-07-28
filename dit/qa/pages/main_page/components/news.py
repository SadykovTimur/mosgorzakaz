from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['News']


class NewsWrapper(ComponentWrapper):
    title = Component(xpath='//span[text()="Новость"]')
    message = Component(tag='textarea')
    mark_as_read = Button(xpath='//button[text()="Пометить прочтенным"]')


class News(Component):
    def __get__(self, instance, owner) -> NewsWrapper:
        return NewsWrapper(instance.app, self.find(instance), self._locator)
