import shodan
from censys.search import CensysHosts
import csv
import os
import time

SHODAN_API_KEY = "YOUR_SHODAN_KEY"
CENSYS_ID = "YOUR_ID"
CENSYS_SECRET = "YOUR_SECRET"

shodan_api = shodan.Shodan(SHODAN_API_KEY)
censys_api = CensysHosts(api_id=CENSYS_ID, api_secret=CENSYS_SECRET)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(BASE_DIR, "ips.csv")
output_file = os.path.join(BASE_DIR, "results.csv")

with open(input_file, "r") as f:
    ips = sorted(set(line.strip() for line in f if line.strip()))

with open(output_file, "w", newline="") as out:
    writer = csv.writer(out)
    writer.writerow(["ip", "censys_result", "shodan_result"])

    total = len(ips)

    for i, ip in enumerate(ips, start=1):

        print(f"[{i}/{total}] Checking {ip}")

        # -------- SHODAN --------
        try:
            host = shodan_api.host(ip)
            shodan_ports = ",".join(map(str, host.get("ports", [])))
            if not shodan_ports:
                shodan_ports = "none"

        except Exception:
            shodan_ports = "error"

        # -------- CENSYS --------
        try:
            result = censys_api.view(ip)
            services = result.get("services", [])

            ports = sorted(
                set(str(s.get("port")) for s in services if s.get("port"))
            )

            censys_ports = ",".join(ports) if ports else "none"

        except Exception:
            censys_ports = "error"

        writer.writerow([ip, censys_ports, shodan_ports])

        time.sleep(1)
