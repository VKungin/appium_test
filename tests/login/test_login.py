import pytest

@pytest.mark.parametrize(
    ("username", "password", "expected_result"),
    [
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "qa_automation_password",
            True,
            id="test valid data"
        ),
        pytest.param(
            "qa.ajax.app.automation@gmail.com",
            "invalid pass",
            False,
            id="test invalid password"
        ),
        pytest.param(
            "invalid username",
            "qa_automation_password",
            False,
            id="test invalid username"
        ),
        pytest.param(
            "invalid username",
            "invalid pass",
            False,
            id="test invalid all data"
        ),

    ]
)
def test_user_login(
        user_login_fixture,
        username,
        password,
        expected_result
):
    login_page = user_login_fixture

    login_page.click_auth_button()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()

    assert login_page.is_element_present("com.ajaxsystems:id/authLogin") == expected_result
