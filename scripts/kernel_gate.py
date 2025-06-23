# kernel69/scripts/kernel_gate.py
# Validates anchors and agents before allowing a ritual to proceed

import json
import hashlib
import os
import urllib.request

INCEPTION_REGISTRY = "https://arweave.net/q4uB75mBr5YpgpEL1VOzG42PxtqYB5XwuNbkIExCVAc"

# Path to anchors_manifest_hash.md (kernel trust hash file)
MANIFEST_PATH = "../../alvearium/docs/anchors_manifest_hash.md"
AGENTS_FILE = "../../hive.bnb/scripts/agents_sample.json"

# Trusted SHA-256 hash of anchors_manifest_hash.md
TRUSTED_HASH = "e70f2dad191ea8702fa6653e089d0abe140653137aeb9e8864224353881b02ab"

# Swarm Genesis Reference
SWARM_GENESIS = {
    "json": "https://arweave.net/IQcAm8Ql9xHX6dXZL28pdyWVdy2A72LxtESLm3cSO1o",
    "md": "https://arweave.net/cECar7wYfFsxjxGTLDBnyZoMZDQm6hUXQvPYLDBrhYY"
}

# Kernel Marker Declaration
KERNEL_MARKER = {
    "json": "https://arweave.net/P-y9Y4dhL6DC33xRP9h_auw-5e49Luiw-jYnCbn6ztI",
    "md": "https://arweave.net/fNbscqGhQ9EMcrRzQScop8heRSKpT6Z0dgf3wkPltGI"
}

def get_sha256(file_path):
    with open(file_path, "rb") as f:
        content = f.read()
    return hashlib.sha256(content).hexdigest()

def validate_anchors():
    print("[+] Validating Alvearium Anchors")
    if not os.path.exists(MANIFEST_PATH):
        print("[ERROR] Manifest file missing")
        return False

    actual = get_sha256(MANIFEST_PATH)
    print("Expected:", TRUSTED_HASH)
    print("Actual:  ", actual)
    return actual == TRUSTED_HASH

def load_agents():
    if not os.path.exists(AGENTS_FILE):
        print("[ERROR] Agent registry not found")
        return {}
    with open(AGENTS_FILE, "r") as f:
        return json.load(f)

def gate_ritual(ritual_input):
    print("[+] Gating Ritual:", ritual_input.get("ritual"))

    manifest_hash = ritual_input.get("manifest")
    if manifest_hash != TRUSTED_HASH:
        print("[FAIL] Ritual manifest does not match trusted hash.")
        return False

    agent = ritual_input.get("agent")
    agents = load_agents()
    if agent not in agents:
        print("[FAIL] Agent not found in registry")
        return False
    if not agents[agent].get("active", False):
        print("[FAIL] Agent is inactive")
        return False

    print("[OK] Ritual approved for:", agent)
    print("[REF] Genesis (JSON):", SWARM_GENESIS['json'])
    print("[REF] Genesis (MD)  :", SWARM_GENESIS['md'])
    print("[MARKER] Kernel Marker JSON:", KERNEL_MARKER['json'])
    print("[MARKER] Kernel Marker MD:  ", KERNEL_MARKER['md'])
    print("[INCEPTION] Registry:        ", INCEPTION_REGISTRY)
    return True

if __name__ == "__main__":
    if not validate_anchors():
        print("[FAIL] Anchor validation failed")
    else:
        # Simulated ritual request input
        ritual_input = {
            "ritual": "spawn_drone",
            "agent": "0xBEEf1234567890abcdef1234567890abcdefBEEF",
            "manifest": TRUSTED_HASH
        }
        gate_ritual(ritual_input)
