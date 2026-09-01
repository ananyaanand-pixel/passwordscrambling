# 👩🏻‍💻 URL Safety Detector
A simple, lightweight Python command-line utility designed to check the fundamental protocol security of a given URL. 

It evaluates whether a URL uses secure encryption, lacks basic protocols, or presents potential formatting risks.

# 🌟 Features:

* Protocol Verification: Instantly identifies if a URL uses a secure (https://) or insecure (http://) protocol.
  
* Format Inspection: Detects incomplete URLs missing necessary protocols (e.g., starting directly with www.).
  
* Input Sanitization: Automatically strips leading/trailing spaces and normalizes inputs to lowercase for consistent validation.
  
# 🚀 How It Works

The script prompts the user for a URL and processes it through a sequence of conditional checks:

Safe: If the URL starts with https://, it is flagged as safe.

Warning: If the URL starts with http://, it triggers a warning to double-check before proceeding.

Missing Protocol: If it contains a dot or starts with www. but lacks a protocol prefix, it is flagged as unsafe due to missing protocols.

Invalid Entry: Any other input structure is categorized as unsafe or invalid.

# ⚠️ Disclaimer

This script provides structural and protocol-level checking. It does not scan live web traffic, consult domain blacklists, or protect against advanced phishing pages hosted on secure https:// servers. Always practice safe browsing habits.
