Project Title: labsoucetest
Overview
This project utilizes Playwright with Python to automate testing for a web application, specifically targeting the Sauce Labs website. The tests are organized using the Pytest framework, providing a structured and efficient way to manage and execute test cases.
Features
Automated testing of various functionalities of the Sauce Labs website.
Utilization of Playwright's powerful features for browser automation.
Implementation of Pytest for writing and organizing test cases.
Ability to easily expand and maintain test suite as the application evolves.
Installation
Clone the repository to your local machine.
Install the required dependencies using pip:
pip install playwright
pip install pytest
pip install pandas
Usage
Navigate to the project directory.
Execute individual test scripts or the entire test suite using Pytest:
pytest /.test_file
View the test results in the console or generate detailed reports as needed.
Directory Structure
tests: Contains the test scripts written using Pytest.
pages: Contains page object models (POM) for different pages of the Sauce Labs website.
data: Optionally, store test data for parameterized testing.
