#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (c) Huawei Technologies Co., Ltd. 2022-2022. All rights reserved.
Description: Data types for data exchange between modules
Author: MindX SDK
Create: 2022
History: NA
"""

from dataclasses import dataclass, field

import numpy as np


@dataclass
class ProcessData:
    # infer_test info
    sub_image_total: int = 0
    image_total: int = 0
    infer_result: list = field(default_factory=lambda: [])
    skip: bool = False

    # image basic info
    image_path: str = ''
    image_name: str = ''
    image_id: int = ''
    frame: np.ndarray = None

    original_width: int = 0
    original_height: int = 0
    resize_h: int = 0
    resize_w: int = 0
    sub_image_list: list = field(default_factory=lambda: [])
    sub_image_size: int = 0
    input_array: np.ndarray = None
    output_array: np.ndarray = None

    max_wh_ratio: float = 0.


@dataclass
class StopData:
    skip: bool = True
    image_total: int = 0
