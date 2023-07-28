from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

__all__ = ['AuthPage']


class AuthPage(Page):
    right = Component(class_name='login-page__right')
    logo = Component(css='[class*="logo"]')
    title = Text(css='[class*="form__caption"]')
    login = TextField(id='login')
    password = TextField(name='password')
    submit = Button(id='commit')
    sudir = Button(class_name='sudir')
    help = Component(css='[class*="help"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.right.visible
                assert self.logo.visible
                assert self.title == 'ЕИС «МОСГОРЗАКАЗ»'
                assert self.login.visible
                assert self.password.visible
                assert self.submit.visible
                assert self.sudir.visible

                return self.help.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
