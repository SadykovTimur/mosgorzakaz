from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

__all__ = ['ImportTitles']


class ImportTitlesWrapper(ComponentWrapper):
    title = Text(css='[id*="header-title-text"]')
    close = Button(css='[class*="x-tool-close"]')
    maximize = Button(css='[class*="x-tool-maximize"]')
    import_btn = Button(xpath='//span[text()="Импорт"]')
    download = Button(xpath='//span[text()="Загрузить из шины"]')
    refresh = Button(xpath='//span[text()="Обновить"]')
    fields = Components(css='[class*="x-form-item"]')
    rows = Components(css='[class*="x-grid-item"]')
    bottom = Component(css='[class*="x-toolbar-docked-bottom"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.title == 'Импорт Титулов (.dbf)'
                assert self.close.visible
                assert self.maximize.visible
                assert self.import_btn.visible
                assert self.download.visible
                assert self.refresh.visible
                assert self.fields[0].visible
                assert self.rows[0].visible

                return self.bottom.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Modal was not loaded')
        self.app.restore_implicitly_wait()


class ImportTitles(Component):
    def __get__(self, instance, owner) -> ImportTitlesWrapper:
        return ImportTitlesWrapper(instance.app, self.find(instance), self._locator)
