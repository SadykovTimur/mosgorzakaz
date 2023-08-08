from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from dit.qa.pages.main_page.components.choose_org_form import ChooseOrgForm
from dit.qa.pages.main_page.components.drop_down_menu import DropDownMenus
from dit.qa.pages.main_page.components.financing_objects.financing_objects import FinancingObjects
from dit.qa.pages.main_page.components.financing_objects.financing_report_params import FinancingReportParams
from dit.qa.pages.main_page.components.footer import Footer
from dit.qa.pages.main_page.components.inventory_payment.inventory_payment_invoice import InventoryPaymentInvoice
from dit.qa.pages.main_page.components.inventory_payment.inventory_payment_invoices import InventoryPaymentInvoices
from dit.qa.pages.main_page.components.inventory_payment.payment import Payment
from dit.qa.pages.main_page.components.main_menu import MainMenu
from dit.qa.pages.main_page.components.news import News
from dit.qa.pages.main_page.components.objects_aip.add_object_aip import AddObjectAIP
from dit.qa.pages.main_page.components.objects_aip.object_aip import ObjectAIP
from dit.qa.pages.main_page.components.objects_aip.object_register_aip import ObjectRegisterAIP
from dit.qa.pages.main_page.components.organization.organization import Organization
from dit.qa.pages.main_page.components.organization.organizations import Organizations
from dit.qa.pages.main_page.components.reports.reports import Reports, ReportsMenu
from dit.qa.pages.main_page.components.reports.reports_queue import ReportsQueue
from dit.qa.pages.main_page.components.update_message import UpdateMessage

__all__ = ['MainPage']


class MainPage(Page):
    main_menu_btn = Button(css='[class*="main-menu-button"]')
    main_menu = MainMenu(id='mainMenuTab-body')
    desktop_tab = Component(xpath='//span[text()="Рабочий стол"]')
    user_name = Text(id='userNameLabel')
    feedback = Text(id='feedbackButton')
    settings = Text(id='settingsButton')
    logout = Text(id='logOutButton')
    tasks_status = Component(xpath='//div[text()="Состояние задач"]')
    tasks_control = Component(xpath='//div[text()="Контроль задач"]')
    footer = Footer(id='desktop-footer')
    news_modal = News(id='NewsWindowId')
    update_modal = UpdateMessage(css='[class*="x-message-box "]')
    choose_org_form_modal = ChooseOrgForm(
        xpath='//div[text()="Выбор орг. формы"]/ancestor::div[contains(@class,"x-window ")]'
    )
    organization_modal = Organization(xpath='//div[text()="Организация"]/ancestor::div[contains(@class, "x-window ")]')
    organizations_tab = Component(xpath='//span[text()="Организации"]')
    organizations = Organizations(css='[data-testid="Организации"]')
    object_register_aip_tab = Component(xpath='//span[text()="Реестр объектов АИП (новый)"]')
    object_register_aip = ObjectRegisterAIP(css='[data-testid="Реестр объектов АИП (новый)"]')
    add_object_aip_modal = AddObjectAIP(
        xpath='//div[text()="Добавить объект АИП"]/ancestor::div[contains(@class, "x-window ")]'
    )
    object_aip_tab = Component(xpath='//span[contains(text(), "Объект АИП"]')
    object_aip = ObjectAIP(css='[data-testid="Объект АИП"]')
    inventory_payment_invoices_tab = Component(xpath='//span[text()="Описи счетов на оплату"]')
    inventory_payment_invoices = InventoryPaymentInvoices(css='[data-testid="Описи счетов на оплату"]')
    inventory_payment_invoice_modal = InventoryPaymentInvoice(
        xpath='//div[text()="Опись счетов на оплату"]/ancestor::div[contains(@class,"x-window ")]'
    )
    payment_modal = Payment(xpath='//div[text()="Платеж"]/ancestor::div[contains(@class,"x-window ")]')
    loaders = Components(css='[class*="mask-loading"]')
    reports_tab = Component(xpath='//span[text()="Отчёты по показателям"]')
    reports = Reports(css='[data-testid="Отчёты по показателям"]')
    reports_queue_tab = Component(xpath='//span[text()="Очередь отчетов"]')
    reports_queue = ReportsQueue(css='[data-testid="Очередь отчетов"]')
    reports_menu = ReportsMenu(class_name='x3-menu-list')
    financing_objects_tab = Component(xpath='//span[text()="Объекты финансирования"]')
    financing_objects = FinancingObjects(css='[data-testid="Объекты финансирования"]')
    drop_down_menus = DropDownMenus(css='[class*="x-menu-body"]')
    financing_report_params_modal = FinancingReportParams(
        xpath='//div[text()="Параметры отчёта"]/ancestor::div[contains(@class, "x-window ")]'
    )

    def is_loaders_hidden(self) -> bool:
        try:
            for loader in self.loaders:
                if loader.visible:
                    return False

            return True
        except NoSuchElementException:
            return True

    @property
    def is_news_modal_hide(self) -> bool:
        try:
            return not self.news_modal.visible
        except (NoSuchElementException, StaleElementReferenceException):
            return True

    @property
    def is_update_modal_hide(self) -> bool:
        try:
            return not self.update_modal.visible
        except (NoSuchElementException, StaleElementReferenceException):
            return True

    def close_news_modal(self) -> None:
        try:
            self.news_modal.mark_as_read.wait_for_clickability().click()
        except NoSuchElementException:
            pass

    def close_update_modal(self) -> None:
        try:
            self.update_modal.read.wait_for_clickability().click()
        except NoSuchElementException:
            pass

    def wait_for_loading(self, login: str) -> None:
        def condition() -> bool:
            try:
                assert self.is_loaders_hidden()
                assert self.main_menu_btn.visible
                assert self.desktop_tab.visible
                assert self.user_name == login
                assert self.feedback == 'Обратная связь'
                assert self.settings == 'Настройки'
                assert self.logout == 'Выход'
                assert self.tasks_status.visible
                assert self.tasks_control.visible

                assert self.footer.object_aip == 'Объекты АИП'
                assert self.footer.general_access == 'Рабочее место руководителя'
                assert self.footer.arm_org == 'АРМ по\nорганизациям'

                return self.footer.support_info.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()

    def wait_organizations_for_loading(self, login: str) -> None:
        def condition() -> bool:
            try:
                assert self.is_loaders_hidden()
                assert self.main_menu_btn.visible
                assert self.desktop_tab.visible
                assert self.organizations_tab.visible
                assert self.user_name == login
                assert self.feedback == 'Обратная связь'
                assert self.settings == 'Настройки'
                assert self.logout == 'Выход'

                assert self.organizations.top.visible
                assert self.organizations.header.visible
                assert self.organizations.body.visible

                return self.organizations.bottom.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Tab was not loaded')
        self.app.restore_implicitly_wait()

    def wait_object_register_aip_for_loading(self, login: str) -> None:
        def condition() -> bool:
            try:
                assert self.is_loaders_hidden()
                assert self.main_menu_btn.visible
                assert self.desktop_tab.visible
                assert self.object_register_aip_tab.visible
                assert self.user_name == login
                assert self.feedback == 'Обратная связь'
                assert self.settings == 'Настройки'
                assert self.logout == 'Выход'

                assert self.object_register_aip.top.visible
                assert self.object_register_aip.body_locked.visible
                assert len(self.object_register_aip.body_locked.rows) > 0
                assert self.object_register_aip.body_normal.visible

                return self.object_register_aip.bottom.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Tab was not loaded')
        self.app.restore_implicitly_wait()

    def wait_and_close_modals(self) -> None:
        def condition() -> bool:
            if self.is_news_modal_hide and self.is_update_modal_hide:
                return True

            self.close_update_modal()
            self.close_news_modal()

            return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Modals was not closed')
        self.app.restore_implicitly_wait()

    def wait_for_add_object_aip_modal_closed(self) -> None:
        def condition() -> bool:
            try:
                return not self.add_object_aip_modal.visible
            except (NoSuchElementException, StaleElementReferenceException):
                return True

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Modal was not closed')
        self.app.restore_implicitly_wait()

    def wait_for_inventory_payment_invoice_modal_closed(self) -> None:
        def condition() -> bool:
            try:
                return not self.inventory_payment_invoice_modal.visible
            except (NoSuchElementException, StaleElementReferenceException):
                return True

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Modal was not closed')
        self.app.restore_implicitly_wait()

    def wait_inventory_payment_invoices_for_loading(self, login: str) -> None:
        def condition() -> bool:
            try:
                assert self.is_loaders_hidden()
                assert self.main_menu_btn.visible
                assert self.desktop_tab.visible
                assert self.inventory_payment_invoices_tab.visible
                assert self.user_name == login
                assert self.feedback == 'Обратная связь'
                assert self.settings == 'Настройки'
                assert self.logout == 'Выход'

                assert self.inventory_payment_invoices.tops[-1].visible
                assert self.inventory_payment_invoices.head.visible
                assert self.inventory_payment_invoices.body.visible
                assert self.inventory_payment_invoices.bottom.visible

                return self.inventory_payment_invoices.filter_btn.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Tab was not loaded')
        self.app.restore_implicitly_wait()

    def wait_reports_for_loading(self, login: str) -> None:
        def condition() -> bool:
            try:
                assert self.is_loaders_hidden()
                assert self.main_menu_btn.visible
                assert self.desktop_tab.visible
                assert self.reports_tab.visible
                assert self.user_name == login
                assert self.feedback == 'Обратная связь'
                assert self.settings == 'Настройки'
                assert self.logout == 'Выход'

                assert self.reports.tops[-1].visible
                assert self.reports.header.visible
                assert self.reports.body.visible
                assert self.reports.bottom.visible

                return self.reports.filter_btn.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Tab was not loaded')
        self.app.restore_implicitly_wait()

    def wait_reports_queue_for_loading(self, login: str) -> None:
        def condition() -> bool:
            try:
                assert self.is_loaders_hidden()
                assert self.main_menu_btn.visible
                assert self.desktop_tab.visible
                assert self.reports_queue_tab.visible
                assert self.user_name == login
                assert self.feedback == 'Обратная связь'
                assert self.settings == 'Настройки'
                assert self.logout == 'Выход'

                assert self.reports_queue.top.visible
                assert self.reports_queue.header.visible
                assert self.reports_queue.body.visible

                return self.reports_queue.bottom.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Tab was not loaded')
        self.app.restore_implicitly_wait()

    def wait_loader_is_hidden(self) -> None:
        def condition() -> bool:
            try:
                return self.is_loaders_hidden()

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Loader was not hidden')
        self.app.restore_implicitly_wait()

    def wait_for_loading_reports_menu(self) -> None:
        def condition() -> bool:
            try:
                assert self.reports_menu.visible

                return len(self.reports_menu.items) > 0
            except NoSuchElementException:
                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Reports menu was not loaded')
        self.app.restore_implicitly_wait()

    def wait_financial_objects_for_loading(self, login: str) -> None:
        def condition() -> bool:
            try:
                assert self.is_loaders_hidden()
                assert self.main_menu_btn.visible
                assert self.desktop_tab.visible
                assert self.financing_objects_tab.visible
                assert self.user_name == login
                assert self.feedback == 'Обратная связь'
                assert self.settings == 'Настройки'
                assert self.logout == 'Выход'

                assert self.financing_objects.tops[-1].visible
                assert self.financing_objects.header.visible
                assert self.financing_objects.body.visible
                assert self.financing_objects.bottom.visible

                return self.financing_objects.filter_btn.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Tab was not loaded')
        self.app.restore_implicitly_wait()
