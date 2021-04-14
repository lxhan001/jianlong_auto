import allure
from Base.base import Base
import Page


class PageLogin(Base):
    @allure.step(title='输入账号')
    def page_account(self, text):
        self.base_send_keys(Page.acount, text)

    @allure.step(title='输入密码')
    def page_pwd(self, text):
        self.base_send_keys(Page.pwd, text)

    @allure.step(title='点击登陆按钮')
    def page_loginbut(self):
        self.base_click_button(Page.loginbut)

    @allure.step(title='获取错误信息')
    def page_page_errtext(self):
        self.base_get_text(Page.errtext)

