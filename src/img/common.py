# -*- coding: utf-8 -*-
#
# Copyright 2022-2024 ETH Zurich
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations
import os
import pandas as pd
from pydantic import BaseModel, Field, field_validator
from typing import Optional, Union
from typing_extensions import Annotated


NUM_COLS: int = 65536
PROJECT_ROOT_DIR: str = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
DATA_DIR: str = os.path.join(PROJECT_ROOT_DIR, "data")
IMG_DIR: str = os.path.join(PROJECT_ROOT_DIR, "out/img")


def get_value_from_dataset(ds_name: str, col_name: str, **constraints) -> float:
    if os.path.exists(ds_name):
        ds = pd.read_csv(ds_name)
        for key, value in constraints.items():
            ds.query(f"{key} == @value", inplace=True)
        if len(ds) == 0:
            return 0
        elif len(ds) > 1:
            raise RuntimeError(f"Multiple rows matching the constraints {constraints}.")
        else:
            return ds[col_name].item()
    else:
        return 0


class Bar(BaseModel):
    ds_name: str
    col_name: str
    constraints: dict[str, Union[int, str]]
    color: str
    x: float
    label: Optional[str] = None
    y: Annotated[float, Field(validate_default=True)] = -1
    bottom: Optional[Bar] = None
    width: float = 0.5

    @field_validator("y", mode="after")
    @classmethod
    def set_y(cls, v, info):
        return get_value_from_dataset(
            info.data["ds_name"], info.data["col_name"], **info.data["constraints"]
        )
