from datetime import datetime

import allure
from coms.qa.core.helpers import wait_for
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from dit.qa.pages.auth_page import AuthPage
from dit.qa.pages.main_page import MainPage

__all__ = [
    'open_auth_page',
    'sign_in',
    'wait_and_close_modals',
    'open_section',
    'open_org_form_modal',
    'open_organization_modal',
    'open_add_object_aip_modal',
    'close_add_object_aip_modal',
    'find_inventory_invoices',
    'open_add_inventory_invoice_modal',
    'open_edit_inventory_invoice_modal',
    'open_payment_modal',
    'open_object_aip',
    'open_report_params',
    'open_choose_element',
    'open_add_property_object',
    'fill_report_params',
    'choose_report',
    'check_download_report',
    'choose_program',
    'choose_subprogram',
    'choose_element',
    'open_lots',
    'open_purchase',
    'close_purchase',
    'open_edit_lots_modal',
    'open_add_object_to_lot',
    'open_add_participant_to_lot',
    'open_choose_object',
    'close_choose_object',
    'close_add_object',
    'open_choose_organization',
    'open_import_titles',
    'open_test_record',
    'close_test_record',
    'remove_test_record',
    'fill_test_record',
    'wait_auth_page',
    'wait_main_page',
    'wait_organizations_tab',
    'wait_registry_object_aip_tab',
    'wait_inventory_payment_invoices_tab',
    'wait_reports_tab',
    'wait_financial_objects_tab',
    'wait_for_downloading_report',
    'wait_arm_aip_tab',
    'wait_balance_transfer_tab',
    'wait_lots_register_tab',
    'wait_titles_tab',
    'wait_test_registry_tab',
]


def open_auth_page(app: Application) -> None:
    AuthPage(app).open()


def sign_in(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            page = AuthPage(app)
            page.login.send_keys(login)
            page.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Entering data exception') from e

        page.submit.click()


def wait_and_close_modals(app: Application) -> None:
    with allure.step('Waiting and closing modals'):
        MainPage(app).wait_and_close_modals()


def open_section(app: Application, menu_name: str = 'Справочники', submenu_name: str = 'Организации') -> None:
    with allure.step(f'Opening section {menu_name}->{submenu_name}'):
        page = MainPage(app)
        page.main_menu_btn.click()

        main_menu = page.main_menu
        main_menu.wait_for_loading()
        main_menu.menu.choose_item(menu_name)
        main_menu.wait_for_loading()

        main_menu.submenu.choose_item(submenu_name)


def find_inventory_invoices(app: Application, number: int = 4268, summ: int = 21736748800) -> None:
    with allure.step('Finding inventory invoices'):
        tab = MainPage(app).inventory_payment_invoices

        try:
            tab.expand_filter_form()
            tab.filter_form.fill_filter({'Номер описи': number, 'Сумма по описи к оплате': summ})
            tab.filter_form.submit.wait_for_clickability().click()
            tab.body.check_found_inventories(number, summ)

            screenshot_attach(app, 'inventory_invoices')
        except Exception as e:
            screenshot_attach(app, 'inventory_invoices_error')

            raise TimeoutError('Inventory invoices was not found') from e


def open_add_inventory_invoice_modal(app: Application) -> None:
    with allure.step('Opening add inventory invoice'):
        page = MainPage(app)

        try:
            page.inventory_payment_invoices.tops[-1].add.wait_for_clickability().click()
            page.inventory_payment_invoice_modal.wait_for_loading()

            screenshot_attach(app, 'inventory_invoice_modal')
        except Exception as e:
            screenshot_attach(app, 'inventory_invoice_modal_error')

            raise TimeoutError('Inventory invoice modal was not loaded') from e

        page.inventory_payment_invoice_modal.close.wait_for_clickability().click()
        page.wait_for_inventory_payment_invoice_modal_closed()


def open_edit_inventory_invoice_modal(app: Application) -> None:
    with allure.step('Opening edit inventory invoice'):
        page = MainPage(app)

        try:
            page.inventory_payment_invoices.body.rows[0].edit.wait_for_clickability().click()
            page.inventory_payment_invoice_modal.wait_for_loading(False)

            screenshot_attach(app, 'inventory_invoice_modal')
        except Exception as e:
            screenshot_attach(app, 'inventory_invoice_modal_error')

            raise TimeoutError('Inventory invoice modal was not loaded') from e


def open_payment_modal(app: Application) -> None:
    with allure.step('Opening payment'):
        page = MainPage(app)

        try:
            invoice = page.inventory_payment_invoice_modal.invoices[0]
            invoice.wait_for_clickability()
            invoice.webelement.click()
            page.payment_modal.wait_for_loading()

            screenshot_attach(app, 'payment_modal')
        except Exception as e:
            screenshot_attach(app, 'payment_modal_error')

            raise TimeoutError('Payment modal was not loaded') from e


def open_org_form_modal(app: Application) -> None:
    with allure.step('Opening org form modal'):
        page = MainPage(app)

        try:
            page.organizations.top.add.click()
            page.choose_org_form_modal.wait_for_loading()

            screenshot_attach(app, 'org_form_modal')
        except Exception as e:
            screenshot_attach(app, 'org_form_modal_error')

            raise TimeoutError('Org form modal was not loaded') from e


def open_organization_modal(app: Application, org_form: str = 'АО') -> None:
    with allure.step('Opening organization modal'):
        page = MainPage(app)

        try:
            page.choose_org_form_modal.choose_form(org_form)
            page.organization_modal.wait_for_loading(org_form)

            screenshot_attach(app, 'organization_modal')
        except Exception as e:
            screenshot_attach(app, 'organization_modal_error')

            raise TimeoutError('Organization modal was not loaded') from e


def open_add_object_aip_modal(app: Application) -> None:
    with allure.step('Opening add object aip modal'):
        page = MainPage(app)

        try:
            page.object_register_aip.top.add.click()
            page.add_object_aip_modal.wait_for_loading()

            screenshot_attach(app, 'add_object_aip_modal')
        except Exception as e:
            screenshot_attach(app, 'add_object_aip_modal_error')

            raise TimeoutError('Add object aip modal was not loaded') from e


def close_add_object_aip_modal(app: Application) -> None:
    with allure.step('Closing add object aip modal'):
        page = MainPage(app)

        try:
            page.add_object_aip_modal.close.click()
            page.wait_for_add_object_aip_modal_closed()

            screenshot_attach(app, 'closed_add_object_aip_modal')
        except Exception as e:
            screenshot_attach(app, 'closed_add_object_aip_modal_error')

            raise TimeoutError('Add object aip modal was not closed') from e


def open_object_aip(app: Application) -> None:
    with allure.step('Opening object aip'):
        page = MainPage(app)
        row = page.object_register_aip.body_locked.rows[0]

        try:
            object_name = row.name
            row.edit.click()
            page.object_aip.wait_for_loading(object_name)

            screenshot_attach(app, 'object_aip')
        except Exception as e:
            screenshot_attach(app, 'object_aip_error')

            raise TimeoutError('Object aip was not loaded') from e


def open_report_params(app: Application) -> None:
    with allure.step('Opening report params modal'):
        page = MainPage(app)

        try:
            page.financing_objects.tops[-1].reports.click()
            app.move_to_element(page.drop_down_menus[-1].choose_item('Сводный отчет с ТДЦ').webelement)

            all_fields = page.drop_down_menus[-1].choose_item('Все поля')
            all_fields.wait_for_clickability()
            all_fields.webelement.click()

            page.financing_report_params_modal.wait_for_loading()

            screenshot_attach(app, 'report_params')
        except Exception as e:
            screenshot_attach(app, 'report_params_error')

            raise TimeoutError('Report params modal was not loaded') from e


def fill_report_params(app: Application, params: dict) -> None:
    with allure.step('Filling report params modal'):
        modal = MainPage(app).financing_report_params_modal

        try:
            for key, value in params.items():
                modal.fill_field(key, value)

            modal.wait_for_loading(params=params)

            screenshot_attach(app, 'report_params')
        except Exception as e:
            screenshot_attach(app, 'report_params_error')

            raise TimeoutError('Report params was not filled') from e

        modal.print.click()


def choose_report(
    app: Application, login: str, report_name: str = '190314', report_type: str = 'MS Excel 2007'
) -> None:
    with allure.step('Choosing report'):
        page = MainPage(app)

        try:
            inp = page.reports.header.name.input
            inp.send_keys(report_name)
            inp.webelement.send_keys(Keys.ENTER)
            page.wait_loader_is_hidden()

            body = page.reports.body
            body.check_found_reports(report_name)

            body.rows[0].open_report_menu()
            page.wait_for_loading_reports_menu()

            page.reports_menu.choose_item(report_type)
            page.wait_reports_queue_for_loading(login)

            screenshot_attach(app, 'report')
        except Exception as e:
            screenshot_attach(app, 'report_error')

            raise TimeoutError('Problems with report') from e


def check_download_report(app: Application, report_date: datetime) -> None:
    with allure.step('Checking downloading report'):
        page = MainPage(app)

        try:
            page.reports_queue.body.check_last_report(report_date)

            screenshot_attach(app, 'report')
        except Exception as e:
            screenshot_attach(app, 'report_error')

            raise TimeoutError('Downloading report was not finished') from e


def choose_program(
    app: Application,
    login: str,
) -> None:
    with allure.step('Choosing arm program'):
        page = MainPage(app)

        try:
            program_name = page.arm_aip.bodys[0].choose_first_item()
            page.wait_arm_aip_program_for_loading(login, program_name)

            screenshot_attach(app, 'program')
        except Exception as e:
            screenshot_attach(app, 'program_error')

            raise TimeoutError('Program was not loaded') from e


def choose_subprogram(app: Application, login: str) -> None:
    with allure.step('Choosing arm subprogram'):
        page = MainPage(app)

        try:
            subprogram_name = page.arm_aip.bodys[1].choose_first_item()
            page.wait_arm_aip_subprogram_for_loading(login, subprogram_name)

            screenshot_attach(app, 'subprogram')
        except Exception as e:
            screenshot_attach(app, 'subprogram_error')

            raise TimeoutError('Subprogram was not loaded') from e


def choose_element(app: Application, field_name: str, element_name: str) -> None:
    with allure.step('Choosing element'):
        page = MainPage(app)

        try:
            modal = page.choose_element_modal[-1]
            modal.search_element(element_name)
            modal.body.choose_item(element_name)
            modal.choose.click()
            page.add_oi_modal.wait_for_filling(field_name, element_name)

            screenshot_attach(app, 'choose_element')
        except Exception as e:
            screenshot_attach(app, 'choose_element_error')

            raise TimeoutError('Choose element was not loaded') from e


def open_lots(app: Application) -> None:
    with allure.step('Opening lots modal'):
        page = MainPage(app)

        try:
            page.lots_register.panel.add.click()
            page.lots_modal.wait_for_loading()

            screenshot_attach(app, 'lots_modal')
        except Exception as e:
            screenshot_attach(app, 'lots_modal_error')

            raise TimeoutError('Lots modal was not loaded') from e


def open_purchase(app: Application) -> None:
    with allure.step('Opening Purchase modal'):
        page = MainPage(app)

        try:
            page.lots_modal.purchase.click()
            page.purchase_modal.wait_for_loading()

            screenshot_attach(app, 'purchase_modal')
        except Exception as e:
            screenshot_attach(app, 'purchase_modal_error')

            raise TimeoutError('Purchase modal was not loaded') from e


def close_purchase(app: Application) -> None:
    with allure.step('Closing Purchase modal'):
        page = MainPage(app)

        try:
            page.purchase_modal.close.click()
            page.purchase_modal.wait_for_invisibility()

            screenshot_attach(app, 'purchase_modal')
        except Exception as e:
            screenshot_attach(app, 'purchase_modal_error')

            raise TimeoutError('Purchase modal was not closed') from e


def open_edit_lots_modal(app: Application) -> None:
    with allure.step('Opening Lots modal'):
        page = MainPage(app)

        try:
            page.lots_modal.close.click()
            page.lots_modal.wait_for_invisibility()

            row = page.lots_register.body.rows[0]
            lot_number = row.lot_number
            row.edit.click()

            page.lots_modal.wait_for_loading(lot_number)

            screenshot_attach(app, 'lots_modal')
        except Exception as e:
            screenshot_attach(app, 'lots_modal_error')

            raise TimeoutError('Lots modal was not loaded') from e


def open_add_object_to_lot(app: Application) -> None:
    with allure.step('Opening Add object to lot modal'):
        page = MainPage(app)

        try:
            page.lots_modal.open_add_object()
            page.objects_modal.wait_for_loading()

            screenshot_attach(app, 'add_object_to_lot_modal')
        except Exception as e:
            screenshot_attach(app, 'add_object_to_lot_modal_error')

            raise TimeoutError('Add object to lot modal was not loaded') from e


def close_add_object(app: Application) -> None:
    with allure.step('Closing Add object to lot modal'):
        page = MainPage(app)

        try:
            page.objects_modal.close.click()
            page.objects_modal.wait_for_invisibility()

            screenshot_attach(app, 'add_object_to_lot_modal')
        except Exception as e:
            screenshot_attach(app, 'add_object_to_lot_modal_error')

            raise TimeoutError('Add object to lot modal was not closed') from e


def open_choose_object(app: Application) -> None:
    with allure.step('Opening Choose object modal'):
        page = MainPage(app)

        try:
            page.objects_modal.choose_field('Объект АИП:').search.click()
            page.objects_aip_modal[-1].wait_for_loading()

            screenshot_attach(app, 'choose_object_modal')
        except Exception as e:
            screenshot_attach(app, 'choose_object_modal_error')

            raise TimeoutError('Choose object modal was not loaded') from e


def close_choose_object(app: Application) -> None:
    with allure.step('Closing Choose object modal'):
        page = MainPage(app)

        try:
            page.objects_aip_modal[-1].close.click()
            page.objects_aip_modal[-1].wait_for_invisibility()

            screenshot_attach(app, 'choose_object_modal')
        except Exception as e:
            screenshot_attach(app, 'choose_object_modal_error')

            raise TimeoutError('Choose object modal was not closed') from e


def open_add_participant_to_lot(app: Application) -> None:
    with allure.step('Opening Add participant to lot modal'):
        page = MainPage(app)

        try:
            page.lots_modal.open_add_participant()
            page.purchase_participant_modal.wait_for_loading()

            screenshot_attach(app, 'add_participant_to_lot_modal')
        except Exception as e:
            screenshot_attach(app, 'add_participant_to_lot_modal_error')

            raise TimeoutError('Add participant to lot modal was not loaded') from e


def open_choose_organization(app: Application) -> None:
    with allure.step('Opening Choose organization modal'):
        page = MainPage(app)

        try:
            page.purchase_participant_modal.choose_field('Организация:').search.click()
            page.organizations_modal[-1].wait_for_loading()

            screenshot_attach(app, 'choose_organization_modal')
        except Exception as e:
            screenshot_attach(app, 'choose_organization_modal_error')

            raise TimeoutError('Choose organization modal was not loaded') from e


def open_add_property_object(app: Application) -> None:
    with allure.step('Opening Add property object modal'):
        page = MainPage(app)

        try:
            page.balance_transfer_arm.panel.create_oi.click()
            page.add_oi_modal.wait_for_loading()

            screenshot_attach(app, 'add_property_object_modal')
        except Exception as e:
            screenshot_attach(app, 'add_property_object_modal_error')

            raise TimeoutError('Add property object modal was not loaded') from e


def open_choose_element(app: Application, field_name: str) -> None:
    with allure.step('Opening Choose element modal'):
        page = MainPage(app)

        try:
            page.add_oi_modal.choose_field(field_name).search.click()
            page.choose_element_modal[-1].wait_for_loading()

            screenshot_attach(app, 'choose_element_modal')
        except Exception as e:
            screenshot_attach(app, 'choose_element_modal_error')

            raise TimeoutError('Choose element modal was not loaded') from e


def open_import_titles(app: Application) -> None:
    with allure.step('Opening Import titles modal'):
        page = MainPage(app)

        try:
            page.titles.panel.import_btn.click()
            page.import_titles_modal.wait_for_loading()

            screenshot_attach(app, 'import_titles_modal')
        except Exception as e:
            screenshot_attach(app, 'import_titles_modal_error')

            raise TimeoutError('Import titles modal was not loaded') from e


def open_test_record(app: Application) -> None:
    with allure.step('Opening Test record modal'):
        page = MainPage(app)

        try:
            page.test_registry.panel.add.click()
            page.test_record_modal.wait_for_loading()

            screenshot_attach(app, 'test_record_modal')
        except Exception as e:
            screenshot_attach(app, 'test_record_modal_error')

            raise TimeoutError('Test record modal was not loaded') from e


def fill_test_record(app: Application, record_name: str) -> None:
    with allure.step('Filling Test record modal'):
        page = MainPage(app)

        try:
            page.test_record_modal.name.send_keys(record_name)
            page.test_record_modal.save.click()

            screenshot_attach(app, 'test_record_modal')
        except Exception as e:
            screenshot_attach(app, 'test_record_modal_error')

            raise TimeoutError('Test record name was not filled') from e


def remove_test_record(app: Application, login: str) -> None:
    with allure.step('Removing Test record'):
        page = MainPage(app)

        try:
            rows = page.test_registry.body.rows
            records_count = len(rows)
            rows[0].remove.click()

            modal = page.remove_modal
            modal.wait_for_loading()
            modal.yes.click()

            page.wait_test_registry_for_loading(login)
            page.test_registry.check_removed_record(records_count)

            screenshot_attach(app, 'remove_test_record')
        except Exception as e:
            screenshot_attach(app, 'remove_test_record_error')

            raise TimeoutError('Test record name was not removed') from e


def close_test_record(app: Application, record_name: str) -> None:
    with allure.step('Closing Test record modal'):
        page = MainPage(app)

        try:
            page.test_record_modal.close.click()
            page.test_record_modal.wait_for_invisibility()
            page.test_registry.check_new_record(record_name)

            screenshot_attach(app, 'close_test_record_modal')
        except Exception as e:
            screenshot_attach(app, 'close_test_record_modal_error')

            raise TimeoutError('Test record name was not closed') from e


def wait_auth_page(app: Application) -> None:
    with allure.step('Wait for loading Auth page'):
        try:
            AuthPage(app).wait_for_loading()

            screenshot_attach(app, 'auth_page')
        except Exception as e:
            screenshot_attach(app, 'auth_page_error')

            raise TimeoutError('Auth page was not loaded') from e


def wait_main_page(app: Application, login: str) -> None:
    with allure.step('Wait for loading Main page'):
        try:
            MainPage(app).wait_for_loading(login)

            screenshot_attach(app, 'main_page')
        except Exception as e:
            screenshot_attach(app, 'main_page_error')

            raise TimeoutError('Main page was not loaded') from e


def wait_organizations_tab(app: Application, login: str) -> None:
    with allure.step('Wait for loading Organizations tab'):
        try:
            MainPage(app).wait_organizations_for_loading(login)

            screenshot_attach(app, 'organizations_tab')
        except Exception as e:
            screenshot_attach(app, 'organizations_tab_error')

            raise TimeoutError('Organizations tab was not loaded') from e


def wait_registry_object_aip_tab(app: Application, login: str) -> None:
    with allure.step('Wait for loading Registry object aip tab'):
        try:
            MainPage(app).wait_object_register_aip_for_loading(login)

            screenshot_attach(app, 'registry_object_aip_tab')
        except Exception as e:
            screenshot_attach(app, 'registry_object_aip_tab_error')

            raise TimeoutError('Registry object aip tab was not loaded') from e


def wait_inventory_payment_invoices_tab(app: Application, login: str) -> None:
    with allure.step('Wait for loading Inventory payment invoices tab'):
        try:
            MainPage(app).wait_inventory_payment_invoices_for_loading(login)

            screenshot_attach(app, 'inventory_payment_invoices_tab')
        except Exception as e:
            screenshot_attach(app, 'inventory_payment_invoices_tab_error')

            raise TimeoutError('Inventory payment invoices tab was not loaded') from e


def wait_reports_tab(app: Application, login: str) -> None:
    with allure.step('Wait for loading Reports tab'):
        try:
            MainPage(app).wait_reports_for_loading(login)

            screenshot_attach(app, 'reports_tab')
        except Exception as e:
            screenshot_attach(app, 'reports_tab_error')

            raise TimeoutError('Reports tab was not loaded') from e


def wait_financial_objects_tab(app: Application, login: str) -> None:
    with allure.step('Wait for loading Financial objects tab'):
        try:
            MainPage(app).wait_financial_objects_for_loading(login)

            screenshot_attach(app, 'financial_objects_tab')
        except Exception as e:
            screenshot_attach(app, 'financial_objects_tab_error')

            raise TimeoutError('Financial objects tab was not loaded') from e


def wait_for_downloading_report(app: Application) -> None:
    with allure.step('Wait for downloading Financial report'):
        page = MainPage(app)
        try:
            wait_browser_tabs(app, 2)
            wait_browser_tabs(app, 1)
            page.financing_report_params_modal.wait_for_invisibility()

            screenshot_attach(app, 'financial_report')
        except Exception as e:
            screenshot_attach(app, 'financial_report_error')

            raise TimeoutError('Financial report was not downloaded') from e


def wait_browser_tabs(app: Application, tabs: int) -> None:
    def condition() -> bool:
        return len(app.driver.window_handles) == tabs

    wait_for(condition, msg='Tabs was not loaded', timeout=190)


def wait_arm_aip_tab(app: Application, login: str) -> None:
    with allure.step('Wait for loading ARM AIP tab'):
        try:
            MainPage(app).wait_arm_aip_for_loading(login)

            screenshot_attach(app, 'arm_aip_tab')
        except Exception as e:
            screenshot_attach(app, 'arm_aip_tab_error')

            raise TimeoutError('ARM AIP tab was not loaded') from e


def wait_balance_transfer_tab(app: Application, login: str) -> None:
    with allure.step('Wait for loading Balance transfer ARM tab'):
        try:
            MainPage(app).wait_balance_transfer_arm_for_loading(login)

            screenshot_attach(app, 'balance_transfer_arm_tab')
        except Exception as e:
            screenshot_attach(app, 'balance_transfer_arm_tab_error')

            raise TimeoutError('Balance transfer ARM tab was not loaded') from e


def wait_lots_register_tab(app: Application, login: str) -> None:
    with allure.step('Wait for loading Lots register tab'):
        try:
            MainPage(app).wait_lots_register_for_loading(login)

            screenshot_attach(app, 'lots_register_tab')
        except Exception as e:
            screenshot_attach(app, 'lots_register_tab_error')

            raise TimeoutError('Lots register tab was not loaded') from e


def wait_titles_tab(app: Application, login: str) -> None:
    with allure.step('Wait for loading Titles tab'):
        try:
            MainPage(app).wait_titles_for_loading(login)

            screenshot_attach(app, 'titles_tab')
        except Exception as e:
            screenshot_attach(app, 'titles_tab_error')

            raise TimeoutError('Titles tab was not loaded') from e


def wait_test_registry_tab(app: Application, login: str) -> None:
    with allure.step('Wait for loading Test registry tab'):
        try:
            MainPage(app).wait_test_registry_for_loading(login)

            screenshot_attach(app, 'test_registry_tab')
        except Exception as e:
            screenshot_attach(app, 'test_registry_tab_error')

            raise TimeoutError('Test registry tab was not loaded') from e
