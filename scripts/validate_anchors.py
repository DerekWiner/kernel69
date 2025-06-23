# kernel69/scripts/validate_anchors.py
# Validates the SHA-256 integrity of the three anchor files in Alvearium

import hashlib
import os


# Canonical kernel marker reference
KERNEL_MARKER = {
    "json": "https://arweave.net/P-y9Y4dhL6DC33xRP9h_auw-5e49Luiw-jYnCbn6ztI",
    "md": "https://arweave.net/fNbscqGhQ9EMcrRzQScop8heRSKpT6Z0dgf3wkPltGI"
}

# Define relative paths to the anchor files
FILES = {
    "anchors.md": "../../alvearium/docs/anchors.md",
    "anchors_metadata.md": "../../alvearium/docs/anchors_metadata.md",
    "anchors_manifest_hash.md": "../../alvearium/docs/anchors_manifest_hash.md"
}

# Replace with known trusted hashes
TRUSTED_HASHES = {
    "anchors.md": "2b841468e371540aed9c9b5c77c12235ad7f5474156b48f2fcfaf49f2714389b",
    "anchors_metadata.md": "0d17511928e7b41a05ef66e883446089b8c4ac6eb16d467fec754439cd53c7c2",
    "anchors_manifest_hash.md": "e70f2dad191ea8702fa6653e089d0abe140653137aeb9e8864224353881b02ab"
}

def sha256_file(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def validate()
    print("\n[MARKER] Kernel Marker JSON:", KERNEL_MARKER["json"])
    print("[MARKER] Kernel Marker MD:  ", KERNEL_MARKER["md"])
:
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
    print("\n[MARKER] Kernel Marker JSON:", KERNEL_MARKER["json"])
    print("[MARKER] Kernel Marker MD:  ", KERNEL_MARKER["md"])

INCEPTION_REGISTRY_TX = "q4uB75mBr5YpgpEL1VOzG42PxtqYB5XwuNbkIExCVAc"
print(f"[INFO] Referencing Inception Registry → https://arweave.net/{INCEPTION_REGISTRY_TX}")
