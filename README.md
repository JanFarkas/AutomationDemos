# README

The tests are marked with the following prefixes:

UI TESTS      `test_0x_`

API TESTS      `test_1x_`

# Setup

1. Install requirements.
   
   `pip install -r requirements.txt`
3. Create a Virtual Enviroment.

   `python -m venv .venv`

   
    `.venv\Scripts\activate`


4. Insert your API Key

   `$env:REQRES_API_KEY="your_key_here"`

6. Run pytest

   `pytest -v`



# Conclusion
The following points have been adressed based on feedback:

-Implemented a simple `Page Object Model`. There is now a clean separation between the test code and page-specific code. Tests now don't depend on the a state left behind by previous tests.

-Implemented `pytest fictures` for proper webdriver setup and cleanup

-Implemented `Screenshots` only when a test fails.

-Implemented a more secure way to input the user's `API KEY`

-Finished the two remaining test cases.


