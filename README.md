# Email Validator Pro API

Email validation with MX check, disposable detection and quality score.

**RapidAPI:** https://rapidapi.com/adunaev8419/api/email-validator-pro11

## Quick Start

```python
import requests

url = "https://email-validator-pro11.p.rapidapi.com/validate"
headers = {"X-RapidAPI-Key": "YOUR_KEY", "Content-Type": "application/json"}
r = requests.post(url, json={"email": "user@gmail.com"}, headers=headers)
print(r.json())
# {"is_valid": true, "mx_valid": true, "is_disposable": false, "quality_score": 100}
```

## Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| /validate | POST | Single email validation |
| /batch | POST | Batch up to 50 emails |

## Pricing

| Plan | Price | Requests/hr |
|------|-------|-------------|
| BASIC | Free | 30 |
| PRO | $9.99/mo | 500 |
| ULTRA | $24.99/mo | 5,000 |

See `examples/` for Python, JavaScript, cURL samples.