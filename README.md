
# Currency Exchange Rate API Testing Suite

This project is a Python-based automated testing suite for validating a live currency exchange rate API. It demonstrates practical skills in API consumption, testing, error handling, and results reporting using Python, `requests`, and `unittest`. The project also includes outputting test results to a structured JSON file.

# Project Structure

```
exchange_rate_api_project/
│
├── api.env                       # Stores your API key (not tracked by Git)
├── api_client.py              # Python client for calling the exchange rate API
├── test_config.py             # Configuration variables (e.g., base URL and parameters)
├── test_exchange_api.py       # Test suite using unittest
├── test_results.json          # JSON-formatted output of test results
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/exchange_rate_api_project.git
cd exchange_rate_api_project
```

2. **Create a virtual environment (recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Configure API key:**

Create a `.env` file in the root directory and add your API key:

```
EXCHANGE_API_KEY=your_actual_api_key_here
```

5. **Run the tests:**

```bash
python test_exchange_api.py
```

The tests will output results in both the terminal and in `test_results.json`.

# Test Cases

The suite currently tests:

- API responds with a `200` status code
- Valid exchange rate is returned for a currency pair
- API handles invalid currency codes properly
- Response JSON includes important fields like `"time_last_update_utc"`



# Aims of this Project

This project was designed to showcase:

- API integration and error handling
- Automated testing using standard Python libraries
- JSON result logging for real-world testing documentation
- Foundation for future Postman + Python hybrid testing frameworks

# Next Steps

- Integrate with Postman test collection or CI pipelines
- Extend test coverage to include more currency scenarios



Donald Okorejior

