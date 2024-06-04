import pytest
import re
from playwright.sync_api import Page, expect, Browser


@pytest.mark.basic
def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))


@pytest.mark.basic
def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


@pytest.mark.search
def test_duckduckgo_search(page: Page, browser: Browser):

    context = browser.new_context(record_video_dir="videos/")
    page = context.new_page()

    # Go to the DuckDuckGo homepage.
    page.goto("https://duckduckgo.com/")

    # Type "Pytest with Eric" into the search box and press Enter.
    page.get_by_placeholder("Search without being tracked").fill("Pytest with Eric")

    # Press Enter to submit the search.
    page.locator('button[aria-label="Search"]').click()

    # Get the first search result using get_by_role
    first_result = page.get_by_role("link", name=re.compile("Pytest")).first

    # Expect the first result to contain the text "Pytest"
    expect(first_result).to_have_text(re.compile("Pytest With Eric"))

    # Make sure to close, so that videos are saved.
    context.close()


@pytest.mark.login
def test_login(page: Page):
    page.goto("https://practicetestautomation.com/practice-test-login/")

    # Fill in the login form
    page.get_by_label("username").fill("student")
    page.get_by_label("password").fill("Password123")

    # Submit the form
    page.get_by_role("button", name="Submit").click()

    # Look for "Congratulations Message" text
    expect(page.get_by_text(re.compile("Congratulations"))).to_be_visible()

    # Look for a Logout Button
    expect(page.get_by_text(re.compile("Log out"))).to_be_visible()

    # Take screenshot
    page.screenshot(path="screenshot.png")
