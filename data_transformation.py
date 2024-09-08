"""
Sample module for data transformation operations including preprocessing and saving the 
preprocessor object.
"""

import os
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))


@dataclass
class DataTransformationConfig:
    """
    Configuration class for data transformation operations.
    """

    preprocessor_ob_file_path = os.path.join("artifacts", "preprocessor.pkl")