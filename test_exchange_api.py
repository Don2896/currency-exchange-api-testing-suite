import requests
import unittest
from test_config import BASE_URL, PARAMS
import json

class TestExchangeRateAPI(unittest.TestCase):
    def test_status_code(self):
        response = requests.get(BASE_URL, params=PARAMS)
        self.assertEqual(response.status_code, 200)

    def test_exchange_rate_positive(self):
        response = requests.get(BASE_URL, params=PARAMS)
        print("Response JSON:", response.json())
        rate = response.json()["conversion_rates"]["GBP"]
        self.assertTrue(rate > 0)


    def test_invalid_currency_code(self):
        # Modify the URL or params to use an invalid currency code
        invalid_url = BASE_URL.replace("USD", "XXX")
        response = requests.get(invalid_url, params=PARAMS)
        self.assertNotEqual(response.status_code, 200)

    def test_response_contains_expected_fields(self):
        response = requests.get(BASE_URL, params=PARAMS)
        data = response.json()
        print(data)
        self.assertIn("time_last_update_utc", data)


class JSONTestResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super(JSONTestResult, self).__init__(*args, **kwargs)
        self.test_results = []

    def addSuccess(self, test):
        super().addSuccess(test)
        self.test_results.append({'test': str(test), 'result': 'success'})

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.test_results.append({
            'test': str(test),
            'result': 'failure',
            'details': self._exc_info_to_string(err, test)
        })

    def addError(self, test, err):
        super().addError(test, err)
        self.test_results.append({
            'test': str(test),
            'result': 'error',
            'details': self._exc_info_to_string(err, test)
        })

    def stopTestRun(self):
        super().stopTestRun()
        with open('test_results.json', 'w') as f:
            json.dump(self.test_results, f, indent=4)


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestExchangeRateAPI)
    runner = unittest.TextTestRunner(resultclass=JSONTestResult)
    runner.run(suite)
