# kernel69/scripts/kernel_gate.py
# Ritual validator: checks if trust triangle and agent linkages are valid before allowing action

import hashlib
import os
import json

ANCHOR_PATH = "../../alvearium/docs/anchors_manifest_hash.md"
TRUSTED_HASH = "079750372369569155c237157400a53d49df62550e3a5a57b3c30a9026f5c74b"
AGENTS_REGISTRY = "../../hive.bnb/scripts/agents_sample.json"

# Simulated ritual input (in reality, this would be parsed or received on-chain)
ritual_input = {
    "agent": "0xBEEf1234567890abcdef1234567890abcdefBEEF",
    "action": "spawn_drone",
    "manifest": "YK4h0pepnRw5lFmxwA9-61ODxEbnlyCSFznH9DUfhyQ"
}

def sha256_file(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def validate_anchor():
    if not os.path.exists(ANCHOR_PATH):
        print("[FAIL] anchors_manifest_hash.md not found.")
        return False

    local_hash = sha256_file(ANCHOR_PATH)
    return local_hash == TRUSTED_HASH

def validate_agent(agent_address):
    if not os.path.exists(AGENTS_REGISTRY):
        print("[FAIL] agents_sample.json not found.")
        return False

    with open(AGENTS_REGISTRY, 'r') as f:
        agents = json.load(f)

    agent = agents.get(agent_address)
    if not agent:
        print(f"[FAIL] Unknown agent {agent_address}")
        return False
    if not agent['active']:
        print(f"[FAIL] Agent {agent_address} is inactive")
        return False

    return True

def kernel_gate():
    print("[+] Kernel Gate Initiated")

    if not validate_anchor():
        print("❌ Trust triangle invalid. Ritual rejected.")
        return

    if not validate_agent(ritual_input['agent']):
        print("❌ Agent invalid. Ritual rejected.")
        return

    print(f"✅ Ritual '{ritual_input['action']}' approved for agent {ritual_input['agent']}")

if __name__ == "__main__":
    kernel_gate()
