import allure
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.common.exceptions import NoSuchElementException

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
    'wait_auth_page',
    'wait_main_page',
    'wait_organizations_tab',
    'wait_registry_object_aip_tab',
    'wait_inventory_payment_invoices_tab',
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
