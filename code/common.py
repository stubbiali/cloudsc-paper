# -*- coding: utf-8 -*-
from __future__ import annotations
import os
import pandas as pd
from pydantic import BaseModel, Field, field_validator
from typing import Optional, Union
from typing_extensions import Annotated


project_root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def get_time(ds_name: str, **constraints) -> float:
    if os.path.exists(ds_name):
        ds = pd.read_csv(ds_name)
        for key, value in constraints.items():
            ds.query(f"{key} == @value", inplace=True)
        if len(ds) == 0:
            return 0
        elif len(ds) > 1:
            raise RuntimeError(f"Multiple rows matching the constraints {constraints}.")
        else:
            return ds["runtime_mean"].item()
    else:
        return 0


class Bar(BaseModel):
    ds_name: str
    constraints: dict[str, Union[int, str]]
    color: str
    x: int
    label: Optional[str] = None
    y: Annotated[int, Field(validate_default=True)] = -1
    width: float = 0.5

    @field_validator("y", mode="after")
    @classmethod
    def set_y(cls, v, info):
        return get_time(info.data["ds_name"], **info.data["constraints"])
