from Page.page_login import PageLogin
import pytest
from Base.read_yaml import get_data


class TestLogin:
    def setup(self):
        self.login = PageLogin()

    def teardown(self):
        self.login.driver.quit()

    @pytest.mark.parametrize('args', get_data('login_data.yaml', 'test_login'))
    def test_login(self, args):
        self.login.page_account(args['account'])
        self.login.page_pwd(args['pwd'])
        self.login.page_loginbut()
        self.login.page_page_errtext()
        assert self.login.page_page_errtext == '账号密码错误!!'  # 断言二者是否相等，若相等通过，不相等则不通过




