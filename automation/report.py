# automation/report.py

import datetime

def generate_report():
    # Create a timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Example vulnerability findings (you can replace with real scan results later)
    findings = [
        {"id": "SMB-001", "vulnerability": "SMB Null Session Enabled", "severity": "High", "recommendation": "Disable null sessions and enforce authentication."},
        {"id": "MSRPC-002", "vulnerability": "MSRPC Anonymous Access", "severity": "Medium", "recommendation": "Restrict RPC access and apply patches."},
        {"id": "WEBDAV-003", "vulnerability": "WebDAV Misconfiguration", "severity": "High", "recommendation": "Disable write access and enforce authentication."}
    ]

    # Write report to a markdown file
    with open("report.md", "w") as f:
        f.write(f"# Vulnerability Report\n\nGenerated on: {timestamp}\n\n")
        for finding in findings:
            f.write(f"## {finding['id']} - {finding['vulnerability']}\n")
            f.write(f"- Severity: {finding['severity']}\n")
            f.write(f"- Recommendation: {finding['recommendation']}\n\n")

    print("Report generated: report.md")

if __name__ == "__main__":
    generate_report()
