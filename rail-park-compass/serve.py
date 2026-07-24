#!/usr/bin/env python3
"""
Serve the Rail Park compass app over HTTPS on your local network.

iOS Safari only exposes the compass (DeviceOrientation) API on a *secure*
context. Plain http://<your-ip>:port will NOT work from your phone, so this
script serves over HTTPS using an auto-generated self-signed certificate.

Usage:
    python3 serve.py            # serves on https://0.0.0.0:8443
    python3 serve.py 9000       # custom port

Then on your iPhone (same Wi-Fi):
    1. Open Safari and go to  https://<your-mac-ip>:8443
    2. You'll get a certificate warning (expected for self-signed certs):
       tap "Show Details" -> "visit this website" -> "Visit Website".
    3. Tap "Enable Compass" and allow motion & orientation access.

Find your Mac's IP with:  ipconfig getifaddr en0
"""

import http.server
import ssl
import socket
import subprocess
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CERT = os.path.join(HERE, ".localhost.pem")


def ensure_cert():
    if os.path.exists(CERT):
        return
    print("Generating a self-signed certificate (one-time)...")
    subprocess.check_call([
        "openssl", "req", "-x509", "-newkey", "rsa:2048",
        "-keyout", CERT, "-out", CERT,
        "-days", "825", "-nodes",
        "-subj", "/CN=rail-park.local",
    ])


def local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"
    finally:
        s.close()


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8443
    ensure_cert()

    os.chdir(HERE)
    handler = http.server.SimpleHTTPRequestHandler
    httpd = http.server.HTTPServer(("0.0.0.0", port), handler)

    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(CERT)
    httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)

    ip = local_ip()
    print("\nRail Park compass is live:")
    print(f"  On this Mac:   https://localhost:{port}")
    print(f"  On your phone: https://{ip}:{port}   (same Wi-Fi network)")
    print("\nAccept the self-signed cert warning on the phone, then tap Enable Compass.")
    print("Press Ctrl+C to stop.\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
