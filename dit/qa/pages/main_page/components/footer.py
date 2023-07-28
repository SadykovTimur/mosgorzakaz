from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.text import Text

__all__ = ['Footer']


class FooterWrapper(ComponentWrapper):
    object_aip = Text(css='[class*="object-aip"]')
    general_access = Text(css='[class*="general-access"]')
    arm_org = Text(css='[class*="armOrg"]')
    support_info = Component(class_name='support__info__text')


class Footer(Component):
    def __get__(self, instance, owner) -> FooterWrapper:
        return FooterWrapper(instance.app, self.find(instance), self._locator)
