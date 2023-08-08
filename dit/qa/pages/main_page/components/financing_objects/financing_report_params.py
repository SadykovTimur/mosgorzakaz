import time
from datetime import datetime
from typing import Optional

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.helpers.custom_wait_conditions import ElementToBeClickable
from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from dit.qa.helpers.date_helper import today
from dit.qa.pages.main_page.components.fields import Field, Fields

__all__ = ['FinancingReportParams']


class FinancingReportParamsWrapper(ComponentWrapper):
    title = Component(xpath='//div[text()="Параметры отчёта"]')
    close = Button(css='[class*="x-tool-close"]')
    print = Button(xpath='//span[text()="Печать" and contains(@class, "x-btn-inner-default-small")]')
    date_field = Field(xpath='//span[text()="Дата отчёта:"]/ancestor::div[contains(@class, "x-field")]')
    fields = Fields(css='[class*="eas4-form-selectfield"]')

    def field_value(self, name: str) -> str:
        for f in self.fields:
            if f.label == name:
                return f.value_field.value

        raise AttributeError('Field was not found')

    def fill_field(self, field_name: str, field_value: str) -> None:
        for f in self.fields:
            if f.label == field_name:
                f.value_field.webelement.clear()
                f.value_field.webelement.send_keys(field_value)
                time.sleep(0.5)
                el = self.driver.find_element(By.XPATH, f'//div[text()="{field_value}"]/ancestor::tr')
                self.wait.until(ElementToBeClickable(element=el))
                el.click()

                return

        raise AttributeError('Field was not found')

    def wait_for_loading(self, report_date: datetime = today(), params: Optional[dict] = None) -> None:
        def condition() -> bool:
            try:
                assert self.title.visible
                assert self.close.visible
                assert self.print.visible
                assert report_date.strftime('%d.%m.%Y') == self.date_field.value_field.value

                if params:
                    for key, value in params.items():
                        assert value in self.field_value(key)

                return True

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Modal was not loaded')
        self.app.restore_implicitly_wait()


class FinancingReportParams(Component):
    def __get__(self, instance, owner) -> FinancingReportParamsWrapper:
        return FinancingReportParamsWrapper(instance.app, self.find(instance), self._locator)
