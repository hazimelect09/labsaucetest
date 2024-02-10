import asyncio
import time

from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)

        # Create a browser context with SSL certificate verification disabled
        context = await browser.new_context(ignore_https_errors=True)
        page = await context.new_page()

        # Navigate to the page with a longer timeout duration
        await page.goto('https://10.10.233.2/registration/signup', timeout=60000)  # Timeout set to 60 seconds

        # Wait until the page is loaded
        await page.wait_for_load_state("load")
        input_element = await page.query_selector('input.signup-text.email-only')

        if input_element:
            print("Input element found!")
            # You can interact with the input element here, such as typing text into it:
            await input_element.type("ropin23124@tospage.com")
        else:
            print("Input element not found!")
        element = await page.query_selector('#SignupViewModel_SubscribeToNewsLetter')
        await  element.click()
        element = await page.query_selector('#SignupViewModel_AgreeToTermsAndCondition')
        await  element.click()

        select2_container = await page.query_selector('#select2-SignupViewModel_CountryResidenceId-container')

        if select2_container:
            print("Select2 container found!")

            # Click on the container to open the dropdown
           # await select2_container.click()

            # Assuming the dropdown is now visible, you can select an option
            # For example, if you want to select an option with the text "United States":
            await page.select_option('#SignupViewModel_CountryResidenceId', value='United States of America')
        els =await page.query_selector('#chkResidenceCountry')
        await  els.click()
        submit_button = await page.query_selector('input.btn.btn-main.px-5.mt-5.w-100')
        await submit_button.click()
        otp = await  page.query_selector_all('#otp-inputs input ')
        for ot in otp:
            await ot.type('3')
        password_selector = '#CreatePasswordViewModel_Password'
        try:
            password = await page.wait_for_selector(password_selector)
            await password.type('Test@1234')  # Type the password
            print("Password textbox found and typed.")
        except Exception as e:
            print(f"Error: {e}")
            return

        confirmpass = await page.query_selector('#CreatePasswordViewModel_PasswordConfirmation')
        await confirmpass.type('Test@1234')  # Type the confirmation password
        print("Confirmation password typed.")

        print('Successfully completed the automation.')
        # Your automation code here

        # Close the page and browser context when done
        #await page.close()
        #await context.close()


if __name__ == "__main__":
       asyncio.run(main())
