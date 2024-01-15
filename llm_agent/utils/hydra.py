from pathlib import Path
from hydra import initialize, compose
from hydra.utils import instantiate as hydra_instantiate
from omegaconf import OmegaConf


def get_agent_config():
    with initialize(version_base="1.3", config_path="../../configs"):
        cfg = compose(config_name="agent.yaml")
        OmegaConf.resolve(cfg)
    return hydra_instantiate(cfg)
