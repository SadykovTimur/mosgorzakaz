from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component, Components
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from dit.qa.pages.main_page.components.add_oi import AddOI
from dit.qa.pages.main_page.components.arm_aip.arm_aip import ARMAIP
from dit.qa.pages.main_page.components.balance_transfer_arm.balance_transfer_arm import BalanceTransferARM
from dit.qa.pages.main_page.components.choose_element import ChooseElement
from dit.qa.pages.main_page.components.choose_org_form import ChooseOrgForm
from dit.qa.pages.main_page.components.drop_down_menu import DropDownMenus
from dit.qa.pages.main_page.components.financing_objects.financing_objects import FinancingObjects
from dit.qa.pages.main_page.components.financing_objects.financing_report_params import FinancingReportParams
from dit.qa.pages.main_page.components.footer import Footer
from dit.qa.pages.main_page.components.inventory_payment.inventory_payment_invoice import InventoryPaymentInvoice
from dit.qa.pages.main_page.components.inventory_payment.inventory_payment_invoices import InventoryPaymentInvoices
from dit.qa.pages.main_page.components.inventory_payment.payment import Payment
from dit.qa.pages.main_page.components.lots_register.lots import Lots
from dit.qa.pages.main_page.components.lots_register.lots_register import LotsRegister
from dit.qa.pages.main_page.components.lots_register.purchase import Purchase
from dit.qa.pages.main_page.components.lots_register.purchase_participant import PurchaseParticipant
from dit.qa.pages.main_page.components.main_menu import MainMenu
from dit.qa.pages.main_page.components.news import News
from dit.qa.pages.main_page.components.notification import Notification
from dit.qa.pages.main_page.components.objects_aip.add_object_aip import AddObjectAIP
from dit.qa.pages.main_page.components.objects_aip.object_aip import ObjectAIP
from dit.qa.pages.main_page.components.objects_aip.object_register_aip import ObjectRegisterAIP
from dit.qa.pages.main_page.components.organization.organization import Organization
from dit.qa.pages.main_page.components.organization.organizations import Organizations
from dit.qa.pages.main_page.components.reports.reports import Reports, ReportsMenu
from dit.qa.pages.main_page.components.reports.reports_queue import ReportsQueue
from dit.qa.pages.main_page.components.test_registry.remove import Remove
from dit.qa.pages.main_page.components.test_registry.test_record import TestRecord
from dit.qa.pages.main_page.components.test_registry.test_registry import TestRegistry
from dit.qa.pages.main_page.components.titles.import_titles import ImportTitles
from dit.qa.pages.main_page.components.titles.titles import Titles
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
    control = Component(css='[tabid="Контроль"]')
    employment = Component(css='[tabid="Занятость"]')
    footer = Footer(id='desktop-footer')
    news_modal = News(id='NewsWindowId')
    update_modal = UpdateMessage(css='[class*="x-message-box "]')
    notification_modal = Notification(xpath='//div[text()="Оповещение"]/ancestor::div[contains(@class, "x-window ")]')
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
    second_loaders = Components(css='[id*="loadmask"]')
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
    arm_aip_tab = Component(xpath='//span[text()="Рабочее место руководителя (АИП)"]')
    arm_aip = ARMAIP(css='[data-testid="Рабочее место руководителя (АИП)"]')
    balance_transfer_arm_tab = Component(xpath='//span[text()="Передача на баланс: АРМ"]')
    balance_transfer_arm = BalanceTransferARM(css='[data-testid="Передача на баланс: АРМ"]')
    add_oi_modal = AddOI(
        xpath='//span[text()="Добавить объект имущества"]/ancestor::div[contains(@class, "x3-window ")]'
    )
    choose_element_modal = ChooseElement(
        xpath='//span[text()="Выбор элемента..."]/ancestor::div[contains(@class, "x3-window ")]'
    )
    lots_register_tab = Component(xpath='//span[text()="Реестр лотов"]')
    lots_register = LotsRegister(css='[data-testid="Реестр лотов"]')
    lots_modal = Lots(xpath='//span[text()="Лоты"]/ancestor::div[contains(@class, "x3-window ")]')
    purchase_modal = Purchase(xpath='//span[text()="Закупка"]/ancestor::div[contains(@class, "x3-window ")]')
    objects_modal = AddOI(xpath='//span[text()="Объекты"]/ancestor::div[contains(@class, "x3-form-label-top")]')
    objects_aip_modal = ChooseElement(
        xpath='//span[text()="Объекты АИП"]/ancestor::div[contains(@class, "x3-window ")]'
    )
    purchase_participant_modal = PurchaseParticipant(
        xpath='//span[text()="Участник закупки"]/ancestor::div[contains(@class, "x3-window ")]'
    )
    organizations_modal = ChooseElement(
        xpath='//span[text()="Организации"]/ancestor::div[contains(@class, "x3-window ")]'
    )
    titles_tab = Component(xpath='//span[text()="Титулы"]')
    titles = Titles(css='[data-testid="Титулы"]')
    import_titles_modal = ImportTitles(
        xpath='//div[text()="Импорт Титулов (.dbf)"]/ancestor::div[contains(@class, "x-window ")]'
    )
    test_registry_tab = Component(xpath='//span[text()="Тест реестр"]')
    test_registry = TestRegistry(css='[data-testid="Тест реестр"]')
    test_record_modal = TestRecord(xpath='//div[text()="Тестовая запись"]/ancestor::div[contains(@class, "x-window ")]')
    remove_modal = Remove(xpath='//div[text()="Удаление"]/ancestor::div[contains(@class, "x-window ")]')

    def is_loaders_hidden(self) -> bool:
        try:
            for loader in self.loaders:
                if loader.visible:
                    return False

            for loader in self.second_loaders:
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

    @property
    def is_notification_modal_hide(self) -> bool:
        try:
            return not self.notification_modal.visible
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

    def close_notification_modal(self) -> None:
        try:
            self.notification_modal.read.wait_for_clickability().click()
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
                assert self.control.visible
                assert self.employment.visible

                assert self.footer.object_aip == 'Объекты АИП'
                assert self.footer.general_access == 'Рабочее место руководителя'

                return self.footer.arm_org == 'АРМ по\nорганизациям'

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
            if self.is_notification_modal_hide:
                return True

            # if self.is_news_modal_hide and self.is_update_modal_hide and self.is_notification_modal_hide:
            #     return True

            self.close_update_modal()
            self.close_news_modal()
            self.close_notification_modal()

            return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Modals was not closed', timeout=70)
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

    def wait_arm_aip_for_loading(self, login: str) -> None:
        def condition() -> bool:
            try:
                assert self.is_loaders_hidden()
                assert self.main_menu_btn.visible
                assert self.desktop_tab.visible
                assert self.arm_aip_tab.visible
                assert self.user_name == login
                assert self.feedback == 'Обратная связь'
                assert self.settings == 'Настройки'
                assert self.logout == 'Выход'

                assert self.arm_aip.panel.finance.visible
                assert self.arm_aip.panel.year.visible
                assert self.arm_aip.panel.objects.visible
                assert self.arm_aip.panel.prefectures.visible
                assert self.arm_aip.panel.developer.visible
                assert self.arm_aip.panel.financing.visible
                assert self.arm_aip.panel.aip.visible
                assert self.arm_aip.panel.column_chart.visible
                assert self.arm_aip.panel.pie_chart.visible
                assert self.arm_aip.panel.search.visible
                assert self.arm_aip.panel.excel.visible
                assert self.arm_aip.panel.map.visible
                assert self.arm_aip.panel.reset_filters.visible

                assert self.arm_aip.headers[0].visible
                assert self.arm_aip.bodys[0].visible

                return self.arm_aip.bodys[0].rows[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Tab was not loaded')
        self.app.restore_implicitly_wait()

    def wait_arm_aip_program_for_loading(self, login: str, program_name: str) -> None:
        def condition() -> bool:
            try:
                assert self.is_loaders_hidden()
                assert self.main_menu_btn.visible
                assert self.desktop_tab.visible
                assert self.arm_aip_tab.visible
                assert self.user_name == login
                assert self.feedback == 'Обратная связь'
                assert self.settings == 'Настройки'
                assert self.logout == 'Выход'

                assert self.arm_aip.panel.finance.visible
                assert self.arm_aip.panel.year.visible
                assert self.arm_aip.panel.objects.visible
                assert self.arm_aip.panel.prefectures.visible
                assert self.arm_aip.panel.developer.visible
                assert self.arm_aip.panel.financing.visible
                assert self.arm_aip.panel.aip.visible
                assert self.arm_aip.panel.search.visible
                assert self.arm_aip.panel.map.visible
                assert self.arm_aip.panel.reset_filters.visible
                assert self.arm_aip.panel.back_btn.visible

                assert self.arm_aip.headers[1].visible
                assert self.arm_aip.bodys[1].visible
                assert self.arm_aip.bodys[1].rows[0].visible

                assert self.arm_aip.titles[-1].webelement.text == program_name
                assert self.arm_aip.object_state[-1].visible
                assert self.arm_aip.object_state[-1].chart.visible
                assert self.arm_aip.exec_and_payment[-1].visible

                return self.arm_aip.exec_and_payment[-1].chart.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Tab was not loaded')
        self.app.restore_implicitly_wait()

    def wait_arm_aip_subprogram_for_loading(self, login: str, subprogram_name: str) -> None:
        def condition() -> bool:
            try:
                assert self.is_loaders_hidden()
                assert self.main_menu_btn.visible
                assert self.desktop_tab.visible
                assert self.arm_aip_tab.visible
                assert self.user_name == login
                assert self.feedback == 'Обратная связь'
                assert self.settings == 'Настройки'
                assert self.logout == 'Выход'

                assert self.arm_aip.panel.finance.visible
                assert self.arm_aip.panel.year.visible
                assert self.arm_aip.panel.objects.visible
                assert self.arm_aip.panel.prefectures.visible
                assert self.arm_aip.panel.developer.visible
                assert self.arm_aip.panel.financing.visible
                assert self.arm_aip.panel.aip.visible
                assert self.arm_aip.panel.search.visible
                assert self.arm_aip.panel.map.visible
                assert self.arm_aip.panel.reset_filters.visible
                assert self.arm_aip.panel.back_btn.visible

                assert self.arm_aip.headers[2].visible
                assert self.arm_aip.bodys[2].visible
                assert self.arm_aip.bodys[2].rows[0].visible

                assert self.arm_aip.titles[-1].webelement.text == subprogram_name
                assert self.arm_aip.object_state[-1].visible
                assert self.arm_aip.object_state[-1].chart.visible
                assert self.arm_aip.exec_and_payment[-1].visible
                assert self.arm_aip.exec_and_payment[-1].chart.visible

                assert self.arm_aip.objects_panel.aip.visible
                assert self.arm_aip.objects_panel.search.visible
                assert self.arm_aip.objects_panel.object_state.visible

                assert self.arm_aip.objects_body.visible

                return self.arm_aip.objects_body.rows[0].visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Tab was not loaded')
        self.app.restore_implicitly_wait()

    def wait_balance_transfer_arm_for_loading(self, login: str) -> None:
        def condition() -> bool:
            try:
                assert self.is_loaders_hidden()
                assert self.main_menu_btn.visible
                assert self.desktop_tab.visible
                assert self.balance_transfer_arm_tab.visible
                assert self.user_name == login
                assert self.feedback == 'Обратная связь'
                assert self.settings == 'Настройки'
                assert self.logout == 'Выход'

                assert self.balance_transfer_arm.panel.clear_filter.visible
                assert self.balance_transfer_arm.panel.save.visible
                assert self.balance_transfer_arm.panel.refresh.visible
                assert self.balance_transfer_arm.panel.print.visible
                assert self.balance_transfer_arm.panel.config_columns.visible
                assert self.balance_transfer_arm.panel.create_oi.visible
                assert self.balance_transfer_arm.panel.create_oaip.visible
                assert self.balance_transfer_arm.panel.choose_color.visible
                assert self.balance_transfer_arm.panel.copy_oi.visible
                assert self.balance_transfer_arm.panel.comment.visible
                assert self.balance_transfer_arm.panel.copy_values.visible
                assert self.balance_transfer_arm.panel.transfer_oi.visible
                assert self.balance_transfer_arm.panel.operations.visible
                assert self.balance_transfer_arm.panel.scripts.visible
                assert self.balance_transfer_arm.panel.info.visible

                assert self.balance_transfer_arm.header.visible
                assert self.balance_transfer_arm.body.visible
                assert self.balance_transfer_arm.filter_btn.visible

                return self.balance_transfer_arm.bottom.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Tab was not loaded')
        self.app.restore_implicitly_wait()

    def wait_lots_register_for_loading(self, login: str) -> None:
        def condition() -> bool:
            try:
                assert self.is_loaders_hidden()
                assert self.main_menu_btn.visible
                assert self.desktop_tab.visible
                assert self.lots_register_tab.visible
                assert self.user_name == login
                assert self.feedback == 'Обратная связь'
                assert self.settings == 'Настройки'
                assert self.logout == 'Выход'

                assert self.lots_register.panel.add.visible
                assert self.lots_register.panel.refresh.visible
                assert self.lots_register.panel.print.visible
                assert self.lots_register.panel.clear_filter.visible
                assert self.lots_register.panel.reset_config.visible
                assert self.lots_register.panel.object_aip.visible
                assert self.lots_register.panel.program_aip.visible
                assert self.lots_register.panel.status.visible
                assert self.lots_register.panel.sort.visible

                assert self.lots_register.header.visible
                assert self.lots_register.body.visible
                assert self.lots_register.filter_btn.visible

                return self.lots_register.bottom.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Tab was not loaded')
        self.app.restore_implicitly_wait()

    def wait_titles_for_loading(self, login: str) -> None:
        def condition() -> bool:
            try:
                assert self.is_loaders_hidden()
                assert self.main_menu_btn.visible
                assert self.desktop_tab.visible
                assert self.titles_tab.visible
                assert self.user_name == login
                assert self.feedback == 'Обратная связь'
                assert self.settings == 'Настройки'
                assert self.logout == 'Выход'

                assert self.titles.panel.print.visible
                assert self.titles.panel.import_btn.visible
                assert self.titles.panel.export.visible
                assert self.titles.panel.refresh.visible
                assert self.titles.panel.clear_filter.visible
                assert self.titles.panel.reset_config.visible
                assert self.titles.panel.group.visible
                assert self.titles.panel.sort.visible

                assert self.titles.header.visible
                assert self.titles.body.visible
                assert self.titles.filter_btn.visible

                return self.titles.bottom.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Tab was not loaded')
        self.app.restore_implicitly_wait()

    def wait_test_registry_for_loading(self, login: str) -> None:
        def condition() -> bool:
            try:
                assert self.is_loaders_hidden()
                assert self.main_menu_btn.visible
                assert self.desktop_tab.visible
                assert self.test_registry_tab.visible
                assert self.user_name == login
                assert self.feedback == 'Обратная связь'
                assert self.settings == 'Настройки'
                assert self.logout == 'Выход'

                assert self.test_registry.panel.add.visible
                assert self.test_registry.panel.refresh.visible
                assert self.test_registry.header.visible
                assert self.test_registry.body.visible

                return self.test_registry.footer.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Tab was not loaded')
        self.app.restore_implicitly_wait()
