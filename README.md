# valami

Tests marked with the following prefixes:

>test_0x_   UI TESTS
>test_1x_   API TESTS







# Setup

pip install playwright pytest
playwright install

## For GET and POST 

Type your API key into cli
>$env:REQRES_API_KEY="your_key_here"


















# cheat sheet

## -Page object model
-There is a clean separation between the test code and page-specific code, such as locators (or their use if you’re using a UI Map) and layout.
-There is a single repository for the services or operations the page offers rather than having these services scattered throughout the tests.

Within your web app’s UI, there are areas where your tests interact with. A Page Object only models these as objects within the test code. This reduces the amount of duplicated code and means that if the UI changes, the fix needs only to be applied in one place.

-tests must not depend on state left behind by previous tests.




## -Pridať CI pipeline (napr. GitHub Actions) na automatické spúšťanie testov pri push/PR a naučiť sa pracovať so secrets.

## -Zachytávať screenshoty a logy pri zlyhaní testov

## Pridať linters a tooling: flake8, black, type hints, ideálne aj pre-commit hooky.



