from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
    
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list

    
<<<<<<< HEAD
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
<<<<<<< HEAD
<<<<<<< HEAD
    tokenizer_name: Path
    
    
    
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int
=======
>>>>>>> parent of ddf1c49 (data transformation added in ipynb and main.py)
=======
    tokenizer_name: Path
>>>>>>> parent of d815990 (model training done in ipynb and main.py, didnot run due to memory issue)
=======
    tokenizer_name: Path
>>>>>>> parent of d815990 (model training done in ipynb and main.py, didnot run due to memory issue)
