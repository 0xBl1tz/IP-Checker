import shodan
import csv
import time
import os

SHODAN_API_KEY = "YOUR_SHODAN_API_KEY"

api = shodan.Shodan(SHODAN_API_KEY)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(BASE_DIR, "ips.csv")
output_file = os.path.join(BASE_DIR, "results.csv")

with open(input_file, "r") as f:
    ips = [line.strip() for line in f if line.strip()]

with open(output_file, "w", newline="") as out:
    writer = csv.writer(out)
    writer.writerow(["ip", "shodan_result"])

    for ip in ips:
        try:
            host = api.host(ip)
            ports = host.get("ports", [])
            ports_str = ",".join(map(str, ports))

        except Exception:
            ports_str = "error"

        writer.writerow([ip, ports_str])

        time.sleep(1)