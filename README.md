---

# IP-Checker

Export open port intelligence for IP addresses using Shodan and Censys.

This tool reads a list of IPs from a CSV file, queries both platforms, and generates a unified output file for quick reconnaissance and attack-surface visibility.

---

## Features

* Query Shodan and Censys simultaneously
* Extract open ports only (noise-free output)
* Automatically removes duplicate IPs
* Handles API errors gracefully
* Clean CSV output for reporting or further automation

---

## Requirements

Install dependencies:

```bash
pip install shodan censys
```

You will also need API credentials from both platforms.

Set them inside the script:

```python
SHODAN_API_KEY = "YOUR_SHODAN_KEY"
CENSYS_ID = "YOUR_ID"
CENSYS_SECRET = "YOUR_SECRET"
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

⚠️ One IP per line — no headers required.

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
ip,censys_result,shodan_result
8.8.8.8,53,53
1.1.1.1,53,53
10.10.10.10,none,443
```

---

## Output Meaning

| Value   | Description                                  |
| ------- | -------------------------------------------- |
| `none`  | No open ports detected                       |
| `error` | API query failed (rate limit, timeout, etc.) |

---

## Important Notes

### Rate Limiting

The script includes a short delay between requests to avoid API throttling.
Reducing the delay may speed up scans but increases the risk of temporary bans.

### Scan Duration

Execution time depends on:

* Number of IPs
* Network latency
* API response speed

Expect roughly **2–3 seconds per IP** in sequential mode.

---

## Recommended Improvements (Optional)

If you plan to evolve this into a production-grade reconnaissance tool, consider adding:

* Threading (5 workers is usually a safe starting point)
* Retry logic for transient API failures
* Change detection between scans
* JSON output for pipeline ingestion
* Alerting when new ports appear

---

## Disclaimer

Use this tool responsibly and only against assets you own or are authorized to assess. Always follow applicable laws, platform policies, and ethical security practices.

---

If you want later, this README can be pushed one level higher into “serious open‑source project” territory by adding badges, a sample architecture diagram, Docker support, or a threaded version benchmark — the kinds of small signals that make a repository feel trustworthy within seconds.
