from pathlib import Path


# Project paths
PROJECT_ROOT = Path("../").resolve()

# Config paths
CONFIGS_PATH = PROJECT_ROOT / "configs"
LLMS_CONFIG_PATH = CONFIGS_PATH / "llms"
PROMPTS_CONFIG_PATH = CONFIGS_PATH / "prompts"
VECTOR_STORE_CONFIG_PATH = CONFIGS_PATH / "vector_store"
