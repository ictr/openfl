# Copyright (C) 2020-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
"""
Shard Descriptor template.

It is recommended to perform tensor manipulations using numpy.
"""

from datasets import load_dataset, ClassLabel
from openfl.interface.interactive_api.shard_descriptor import ShardDescriptor


class LocalShardDescriptor(ShardDescriptor):
    """Shard descriptor subclass."""

    def __init__(self, train_valid_path: str, test_path: str) -> None:
        """
        Initialize local Shard Descriptor.

        Parameters are arbitrary, set up the ShardDescriptor-related part
        of the envoy_config.yaml as you need.
        """

        self.data_by_type = {"train": None, "test": None}

        if train_valid_path:
            self.data_by_type["train"] = (
                load_dataset("csv", data_files=train_valid_path)["train"]
                .rename_column("label", "labels")
                .cast_column("labels", ClassLabel(num_classes=2))
                .train_test_split(
                    train_size=0.8, shuffle=True, seed=12345, stratify_by_column="labels"
                )
            )

        if test_path:
            self.data_by_type["test"] = (
                load_dataset("csv", data_files=test_path)["train"]
                .rename_column("label", "labels")
                .cast_column("labels", ClassLabel(num_classes=2))
            )

    def get_dataset(self, dataset_type: str):
        return self.data_by_type[dataset_type]

    @property
    def sample_shape(self):
        return [""]

    @property
    def target_shape(self):
        return [""]
