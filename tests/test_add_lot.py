from typing import Callable

import allure
import pytest
from _pytest.fixtures import FixtureRequest
from coms.qa.fixtures.application import Application
from coms.qa.frontend.constants import CLIENT_BROWSERS, CLIENT_DEVICE_TYPE

from tests.steps import (
    close_add_object,
    close_choose_object,
    close_purchase,
    open_add_object_to_lot,
    open_add_participant_to_lot,
    open_auth_page,
    open_choose_object,
    open_choose_organization,
    open_edit_lots_modal,
    open_lots,
    open_purchase,
    open_section,
    sign_in,
    wait_and_close_modals,
    wait_auth_page,
    wait_lots_register_tab,
    wait_main_page,
)


@allure.label('owner', 'a.seregin')
@allure.label('component', 'DIT')
@allure.epic('Mosgorzakaz Interface')
@allure.story('Главная страница')
@allure.title('Доступность добавления лота')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.parametrize('browser', CLIENT_BROWSERS)
@pytest.mark.parametrize('device_type', CLIENT_DEVICE_TYPE)
def test_add_lot(request: FixtureRequest, make_app: Callable[..., Application], browser: str, device_type: str) -> None:
    username = request.config.option.username

    app = make_app(browser, device_type)

    open_auth_page(app)
    wait_auth_page(app)

    sign_in(app, username, request.config.option.password)
    wait_main_page(app, username)

    wait_and_close_modals(app)

    open_section(app, 'Закупки', 'Реестр лотов')
    wait_lots_register_tab(app, username)

    open_lots(app)
    open_purchase(app)
    close_purchase(app)

    open_edit_lots_modal(app)
    open_add_object_to_lot(app)
    open_choose_object(app)
    close_choose_object(app)
    close_add_object(app)

    open_add_participant_to_lot(app)
    open_choose_organization(app)
