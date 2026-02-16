from censys.search import CensysHosts
import csv
import os
import time

CENSYS_ID = "YOUR_ID"
CENSYS_SECRET = "YOUR_SECRET"

api = CensysHosts(api_id=CENSYS_ID, api_secret=CENSYS_SECRET)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(BASE_DIR, "ips.csv")
output_file = os.path.join(BASE_DIR, "censys_results.csv")

with open(input_file, "r") as f:
    ips = list(set(line.strip() for line in f if line.strip()))

with open(output_file, "w", newline="") as out:
    writer = csv.writer(out)
    writer.writerow(["ip", "censys_result"])

    total = len(ips)

    for i, ip in enumerate(ips, start=1):
        print(f"[{i}/{total}] Checking {ip}")

        try:
            result = api.view(ip)

            services = result.get("services", [])
            ports = sorted(
                set(str(service.get("port")) for service in services if service.get("port"))
            )

            ports_str = ",".join(ports) if ports else "none"

        except Exception as e:
            ports_str = "error"

        writer.writerow([ip, ports_str])

        time.sleep(1)
