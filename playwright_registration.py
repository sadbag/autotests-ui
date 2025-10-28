from playwright.sync_api import sync_playwright,expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    login_input = page.get_by_test_id('registration-form-username-input').locator('input')
    login_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    logging_button = page.get_by_test_id('registration-page-registration-button')
    logging_button.click()

    iscontain_dashboard = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(iscontain_dashboard).to_be_visible()
    expect(iscontain_dashboard).to_have_text('Dashboard')