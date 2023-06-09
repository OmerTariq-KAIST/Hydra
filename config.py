#this file describes the structure of the configuration
from dataclasses import dataclass


@dataclass
class Paths:
    log: str
    data: str


@dataclass
class Files:
    train_data: str
    train_labels: str
    test_data: str
    test_labels: str


@dataclass
class Params:
    epoch_count: int
    lr: float
    batch_size: int


#this simply groups the above class instances
@dataclass
class MNISTConfig:
    paths: Paths
    files: Files
    params: Params