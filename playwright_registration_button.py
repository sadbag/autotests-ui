from playwright.sync_api import sync_api, expect

with sync_playwright as playwright():
    browser = playwrught.chromium.launch(headless = False)