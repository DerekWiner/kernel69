# kernel69/scripts/validate_anchors.py
# Validates the SHA-256 integrity of the three anchor files in Alvearium

import hashlib
import os

# Define relative paths to the anchor files
FILES = {
    "anchors.md": "../../alvearium/docs/anchors.md",
    "anchors_metadata.md": "../../alvearium/docs/anchors_metadata.md",
    "anchors_manifest_hash.md": "../../alvearium/docs/anchors_manifest_hash.md"
}

# Replace with known trusted hashes
TRUSTED_HASHES = {
    "anchors.md": "gU742_NxFAZ_WC2XNyYZzwWEddfgyIR4kezHPAG-EQk",
    "anchors_metadata.md": "72JHE_62L8OU3OPnHiNsiapF2gWlvay-lMNlPFUX3iQ",
    "anchors_manifest_hash.md": "YK4h0pepnRw5lFmxwA9-61ODxEbnlyCSFznH9DUfhyQ"
}

def sha256_file(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def validate():
    print("[+] Validating Alvearium Anchors")
    for label, path in FILES.items():
        if not os.path.exists(path):
            print(f"[ERROR] Missing file: {label} → {path}")
            continue

        local_hash = sha256_file(path)
        expected = TRUSTED_HASHES.get(label, None)

        print(f"\n🔹 {label}")
        print(f"    → Expected : {expected}")
        print(f"    → Actual   : {local_hash}")

        if expected and not local_hash.startswith(expected[:8]):
            print("    ✗ FAILED integrity check")
        else:
            print("    ✓ PASSED")

if __name__ == "__main__":
    validate()
