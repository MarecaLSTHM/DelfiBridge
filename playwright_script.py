from playwright.sync_api import sync_playwright
import time

DELFI_URL = "https://southsfrica.cad4tb.care/winny-solutions/ahri/series/"  # change to real URL

def run_delfi_search(patient_id: str):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True,   # IMPORTANT: set True in production if needed
            slow_mo=200
        )

        context = browser.new_context()
        page = context.new_page()

        # 1. Open DELFI
        page.goto(DELFI_URL)

        # 2. LOGIN STEP (if required)
        # Uncomment and fill if DELFI requires login
        """
        page.fill("#username", "your_user")
        page.fill("#password", "your_pass")
        page.click("#login")
        page.wait_for_timeout(3000)
        """

        # 3. Wait for search bar
        page.wait_for_selector("#search_bar")

        # 4. Enable search system (if required by DELFI)
        try:
            page.evaluate("""
                browser_tools.enable_search($('#search_bar'));
            """)
        except:
            pass

        # 5. Inject patient ID
        page.fill("#search_bar", patient_id)

        # 6. Trigger search
        page.evaluate("""
            browser_tools.search_from_url();
        """)

        # 7. Let user see result
        page.wait_for_timeout(5000)

        # OPTIONAL: keep browser open for user
        # browser.close()

        return "search_executed"