---

# IP-Checker

Export open port and service information for IP addresses using **Shodan**.

This tool reads a list of IPs from a CSV file, queries Shodan, and generates a structured CSV output for reconnaissance, security assessment, or reporting purposes.

---

## Features

* Query Shodan for each IP
* Extract open ports and detected services
* Automatically removes duplicate IPs
* Handles API errors gracefully
* Generates a clean CSV output, easy to analyze

---

## Requirements

Install dependencies:

```bash
pip install shodan
```

You will also need a **Shodan API key**.

Set it inside the script:

```python
SHODAN_API_KEY = "YOUR_SHODAN_API_KEY"
```

---

## Usage

### 1. Prepare IP List

Create a file named:

```
ips.csv
```

Place it in the same directory as the Python script.

Example:

```csv
8.8.8.8
1.0.0.1
1.1.1.1
10.10.10.10
```

⚠️ One IP per line — no header required.

---

### 2. Run the Script

```bash
python ipchecker.py
```

---

### 3. Check the Output

After execution, a file named:

```
results.csv
```

will be generated.

Example output:

```csv
ip,ports,services
8.8.8.8,53,53:DNS
1.1.1.1,53,53:DNS
10.10.10.10,80,80:Apache | 443:nginx
```

---

## Output Meaning

| Column     | Description                                     |
| ---------- | ----------------------------------------------- |
| `ports`    | List of open ports                              |
| `services` | Detected service for each port (`port:product`) |
| `none`     | No open ports detected                          |
| `error`    | API query failed (rate limit, timeout, etc.)    |

---

## Important Notes

* **Rate Limiting**: The script includes a short delay (`time.sleep(1)`) between requests to avoid throttling. Reducing this delay may increase speed but risks temporary bans.
* **Scan Duration**: Expect ~2–3 seconds per IP in sequential mode.
* **Unknown Services**: If a service could not be identified, `unknown` will appear. This often indicates custom, hidden, or misconfigured services.

---

## Recommended Improvements (Optional)

For a more advanced reconnaissance workflow:

* Threading (e.g., 5 workers) for faster scans
* Retry logic for transient API failures
* Include additional Shodan fields like `org`, `country`, or `timestamp`
* Change detection between scans
* JSON output for pipeline integration
* Alerting on new or changed services

---

## Disclaimer

Use this tool responsibly and only on IPs you own or are authorized to scan. Always comply with applicable laws, platform policies, and ethical security practices.