from typing import List

from coms.qa.frontend.pages.component import Component, Components, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text

__all__ = ['ARMAIP']


class PanelWrapper(ComponentWrapper):
    finance = Component(xpath='//span[text()="Финансы"]')
    year = Component(xpath='//span[text()="Год"]')
    objects = Component(xpath='//span[text()="Объекты"]')
    prefectures = Component(xpath='//span[text()="Префектуры"]')
    developer = Component(xpath='//span[text()="Застройщик"]')
    financing = Component(xpath='//span[text()="Финансирование"]')
    aip = Component(xpath='//span[text()="АИП"]')
    column_chart = Button(css='[class*="column-chart"]')
    pie_chart = Button(css='[class*="pie-chart"]')
    search = Button(css='[class*="icon-zoom"]')
    excel = Button(css='[class*="page-white-excel"]')
    map = Button(css='[class*="icon-map"]')
    reset_filters = Button(css='[class*="anticlockwise"]')
    back_btn = Button(xpath='//button[text()="Назад"]')


class Panel(Components):
    def __get__(self, instance, owner) -> PanelWrapper:
        return PanelWrapper(instance.app, self.find(instance), self._locator)


class ObjectsPanelWrapper(ComponentWrapper):
    aip = Component(xpath='//span[text()="АИП"]')
    search = Button(css='[class*="icon-accept"]')
    object_state = Button(xpath='//button[text()="Состояние объекта"]')


class ObjectsPanel(Components):
    def __get__(self, instance, owner) -> ObjectsPanelWrapper:
        return ObjectsPanelWrapper(instance.app, self.find(instance), self._locator)


class RowWrapper(ComponentWrapper):
    code = Text(css='[class*="columnCode"]')
    name = Text(css='[class*="columnName"]')


class Rows(Components):
    def __get__(self, instance, owner) -> List[RowWrapper]:
        ret: List[RowWrapper] = []

        for webelement in self.finds(instance):
            ret.append(RowWrapper(instance.app, webelement, self._locator))

        return ret


class BodyWrapper(ComponentWrapper):
    rows = Rows(class_name='x3-grid3-row-table')

    def choose_first_item(self) -> str:
        row = self.rows[1]
        name = row.name

        row.wait_for_clickability()
        row.webelement.click()

        return name


class Body(Components):
    def __get__(self, instance, owner) -> BodyWrapper:
        return BodyWrapper(instance.app, self.find(instance), self._locator)


class Bodys(Components):
    def __get__(self, instance, owner) -> List[BodyWrapper]:
        ret: List[BodyWrapper] = []

        for webelement in self.finds(instance):
            ret.append(BodyWrapper(instance.app, webelement, self._locator))

        return ret


class GraphWrapper(ComponentWrapper):
    chart = Component(class_name='highcharts-container')


class Graphs(Components):
    def __get__(self, instance, owner) -> List[GraphWrapper]:
        ret: List[GraphWrapper] = []

        for webelement in self.finds(instance):
            ret.append(GraphWrapper(instance.app, webelement, self._locator))

        return ret


class ARMAIPWrapper(ComponentWrapper):
    panel = Panel(css='[class*="x3-panel-tbar"]')
    headers = Components(class_name='x3-grid3-header')
    bodys = Bodys(class_name='x3-grid3-body')
    titles = Components(css='[class*=x3-mosks-arm-large-panel-header]')
    object_state = Graphs(xpath='//span[text()="Состояние объектов"]/ancestor::div[@class=" x3-box-item"]')
    exec_and_payment = Graphs(
        xpath='//span[text()="Диаграмма выполнения и оплаты"]/ancestor::div[@class=" x3-box-item"]'
    )
    objects_panel = ObjectsPanel(css='[class*="x3-box-item"] [class*="x3-panel-tbar"]')
    objects_body = Body(xpath='//div[text()="Объект АИП"]/ancestor::div[@class="x3-grid3"]')


class ARMAIP(Component):
    def __get__(self, instance, owner) -> ARMAIPWrapper:
        return ARMAIPWrapper(instance.app, self.find(instance), self._locator)
