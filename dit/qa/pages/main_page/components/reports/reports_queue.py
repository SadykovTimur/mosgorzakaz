from datetime import datetime
from typing import List

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException

from dit.qa.helpers.date_helper import normalize

__all__ = ['ReportsQueue']


class TopWrapper(ComponentWrapper):
    update = Button(xpath='//span[text()="Обновить"]')
    cancel_all = Button(xpath='//span[text()="Отменить все"]')
    remove = Button(xpath='//span[text()="Удалить отмененные"]')
    restart = Button(xpath='//span[text()="Перезапустить приложение-исполнитель"]')


class Top(Components):
    def __get__(self, instance, owner) -> TopWrapper:
        return TopWrapper(instance.app, self.find(instance), self._locator)


class RowWrapper(ComponentWrapper):
    columns = Components(css='[data-columnid*="easwraptextcolumn"]')


class Rows(Components):
    def __get__(self, instance, owner) -> List[RowWrapper]:
        ret: List[RowWrapper] = []

        for webelement in self.finds(instance):
            ret.append(RowWrapper(instance.app, webelement, self._locator))

        return ret


class BodyWrapper(ComponentWrapper):
    rows = Rows(css='[class="  x-grid-row"]')

    def check_last_report(self, report_date_expected: datetime) -> None:
        def condition() -> bool:
            try:
                report_date_str = self.rows[0].columns[3].webelement.text
                report_date = normalize(report_date_str)
                status = self.rows[0].columns[4].webelement.text

                assert report_date_expected <= report_date
                assert report_date_expected.strftime('%d.%m.%Y') in report_date_str
                assert status != 'Завершен с ошибкой'

                return status in ['В очереди на формирование', 'Формируется', 'Сформирован > Загрузить']
            except NoSuchElementException:
                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Report was not finished')
        self.app.restore_implicitly_wait()


class Body(Component):
    def __get__(self, instance, owner) -> BodyWrapper:
        return BodyWrapper(instance.app, self.find(instance), self._locator)


class ReportsQueueWrapper(ComponentWrapper):
    top = Top(css='[class*="x-toolbar-docked-top"]')
    header = Component(css='[class*="x-grid-header"]')
    body = Body(css='[data-ref="body"]')
    bottom = Component(css='[id*="pagingtoolbar"]')


class ReportsQueue(Component):
    def __get__(self, instance, owner) -> ReportsQueueWrapper:
        return ReportsQueueWrapper(instance.app, self.find(instance), self._locator)
