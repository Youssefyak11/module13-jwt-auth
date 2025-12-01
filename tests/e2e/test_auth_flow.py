import uuid
from playwright.sync_api import Page, expect

BASE_URL = "http://localhost:8000"

def random_email():
    return f"user_{uuid.uuid4().hex[:8]}@example.com"

def test_register_success(page: Page):
    email = random_email()
    page.goto(f"{BASE_URL}/static/register.html")

    page.fill("#email", email)
    page.fill("#password", "strongpass")
    page.fill("#confirm-password", "strongpass")
    page.click("button[type=submit]")

    message = page.locator("#message")
    expect(message).to_have_text("Registration successful!")

def test_register_short_password_frontend(page: Page):
    email = random_email()
    page.goto(f"{BASE_URL}/static/register.html")

    page.fill("#email", email)
    page.fill("#password", "123")
    page.fill("#confirm-password", "123")
    page.click("button[type=submit]")

    message = page.locator("#message")
    expect(message).to_contain_text("Password must be at least 8")

def test_login_success(page: Page):
    email = random_email()
    page.goto(f"{BASE_URL}/static/register.html")
    page.fill("#email", email)
    page.fill("#password", "strongpass")
    page.fill("#confirm-password", "strongpass")
    page.click("button[type=submit]")
    expect(page.locator("#message")).to_have_text("Registration successful!")

    page.goto(f"{BASE_URL}/static/login.html")
    page.fill("#email", email)
    page.fill("#password", "strongpass")
    page.click("button[type=submit]")

    expect(page.locator("#message")).to_have_text("Login successful!")

def test_login_wrong_password(page: Page):
    email = random_email()
    page.goto(f"{BASE_URL}/static/register.html")
    page.fill("#email", email)
    page.fill("#password", "strongpass")
    page.fill("#confirm-password", "strongpass")
    page.click("button[type=submit]")
    expect(page.locator("#message")).to_have_text("Registration successful!")

    page.goto(f"{BASE_URL}/static/login.html")
    page.fill("#email", email)
    page.fill("#password", "wrongpass")
    page.click("button[type=submit]")

    expect(page.locator("#message")).to_contain_text("Invalid")
