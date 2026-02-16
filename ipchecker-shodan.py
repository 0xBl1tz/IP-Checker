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

with open(output_file, "w", newline="", encoding="utf-8") as out:
    writer = csv.writer(out)
    writer.writerow(["ip", "ports", "services"])

    for ip in ips:
        try:
            host = api.host(ip)

            ports = []
            services = []

            for item in host.get("data", []):
                port = item.get("port")

                product = item.get("product")

                if not product:
                    product = item.get("transport") or item.get("devicetype") or "unknown"

                if port:
                    ports.append(str(port))
                    services.append(f"{port}:{product}")

            ports_str = ",".join(sorted(set(ports))) if ports else "none"
            services_str = " | ".join(sorted(set(services))) if services else "none"

        except Exception as e:
            ports_str = "error"
            services_str = "error"

        writer.writerow([ip, ports_str, services_str])

        print(f"Checked {ip}")
        time.sleep(1)
