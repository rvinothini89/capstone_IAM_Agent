import os 
import json
import re

MEMORY_FILE = "data/memory_store.json"

state = {
    "role": None,
    "access_type": None,
    "resource": None
}

conversation_memory = []

# ----------------------
# LOAD MEMORY (LONG-TERM)
# ----------------------
def load_memory():
    global conversation_memory, state

    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r") as f:
                data = json.load(f)
                conversation_memory = data.get("history", [])
                state.update(data.get("state", {}))
        except:
            conversation_memory = []
    else:
        conversation_memory = []

# ----------------------
# SAVE MEMORY (LONG-TERM)
# ----------------------
def save_memory():
    data = {
        "history": conversation_memory,
        "state": state
    }
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)


def update_state(user_input):
    text = user_input.lower()

    # Role detection using word boundaries

    if re.search(r"\bqa\b", text):
        state["role"] = "QA"

    elif re.search(r"\bdevops\b", text):
        state["role"] = "DevOps"

    elif re.search(r"\bdev\b", text) or re.search(r"\bdeveloper\b", text):
        state["role"] = "Developer"

    if "read" in text:
        state["access_type"] = "read"
    elif "write" in text:
        state["access_type"] = "write"

    if "production" in text:
        state["resource"] = "production_db"
    elif "test" in text:
        state["resource"] = "test_db"


def get_state():
    return state


def add_to_memory(user_input, agent_response):
    conversation_memory.append({
        "user": user_input,
        "agent": agent_response
    })

    save_memory()  # Persist after every update


def get_memory():
    return conversation_memory


def clear_memory():
    conversation_memory.clear()
    state["role"] = None
    state["access_type"] = None
    state["resource"] = None

    save_memory()   # reset persisted memory
