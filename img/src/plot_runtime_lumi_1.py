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
import click
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
from typing import Literal

from common import Bar, DATA_DIR, IMG_DIR, NUM_COLS
from plot_runtime_daint import fill_ax_x0, fill_ax_x1, fill_ax_x2


# config: start
FIGSIZE_IN_INCH: tuple[int, int] = (40, 14)
NUM_THREADS: int = 7
# config: end


def get_data(precision: Literal["double", "single"]) -> tuple[list[Bar], list[Bar], list[Bar]]:
    data_0 = [
        Bar(
            ds_name=os.path.join(DATA_DIR, "cloudsc/lumi/cray-gpu/14.0.2/release/performance.csv"),
            col_name="runtime_mean",
            constraints={
                "variant": "fortran",
                "num_cols": NUM_COLS,
                "num_threads": NUM_THREADS,
                "precision": precision,
            },
            x=1,
            color="grey",
            label="Fortran: OpenMP (CPU)",
        ),
        Bar(
            ds_name=os.path.join(
                DATA_DIR, "cloudsc/lumi/lumi/23.03/cray/8.3.3/cce/15.0.1/performance.csv"
            ),
            col_name="runtime_mean",
            constraints={
                "variant": "gt:cpu_kfirst",
                "num_cols": NUM_COLS,
                "num_threads": NUM_THREADS,
                "precision": precision,
            },
            x=2,
            color="cornflowerblue",
            label="GT4Py: CPU k-first",
        ),
        Bar(
            ds_name=os.path.join(DATA_DIR, "cloudsc/lumi/cray-gpu/14.0.2/release/performance.csv"),
            col_name="runtime_mean",
            constraints={
                "variant": "gpu-scc-k-caching",
                "num_cols": NUM_COLS,
                "precision": precision,
            },
            x=3,
            color="palegreen",
            label="Fortran: OpenACC (GPU)",
        ),
        Bar(
            ds_name=os.path.join(DATA_DIR, "cloudsc/lumi/cray-gpu/14.0.2/release/performance.csv"),
            col_name="runtime_mean",
            constraints={
                "variant": "loki-scc-hoist",
                "num_cols": NUM_COLS,
                "precision": precision,
            },
            x=4,
            color="khaki",
            label="Fortran: source-to-source translator Loki (GPU)",
        ),
        Bar(
            ds_name=os.path.join(DATA_DIR, "cloudsc/lumi/cray-gpu/15.0.1/release/performance.csv"),
            col_name="runtime_mean",
            constraints={
                "variant": "hip-k-caching",
                "num_cols": NUM_COLS,
                "precision": precision,
            },
            x=5,
            color="green",
            label="C: HIP (GPU)",
        ),
        Bar(
            ds_name=os.path.join(
                DATA_DIR, "cloudsc/lumi/lumi/23.03/cray/8.3.3/cce/15.0.1/performance.csv"
            ),
            col_name="runtime_mean",
            constraints={"variant": "dace:gpu", "num_cols": NUM_COLS, "precision": precision},
            x=6,
            color="coral",
            label="GT4Py: DaCe (GPU)",
        ),
    ]
    data_1 = [
        Bar(
            ds_name=os.path.join(DATA_DIR, "cloudsc2/lumi/cray-gpu/14.0.2/release/performance.csv"),
            col_name="runtime_mean",
            constraints={
                "variant": "nl",
                "num_cols": NUM_COLS,
                "num_threads": NUM_THREADS,
                "precision": precision,
            },
            x=1,
            color="grey",
        ),
        Bar(
            ds_name=os.path.join(DATA_DIR, "cloudsc2/lumi/cray-gpu/14.0.2/release/performance.csv"),
            col_name="runtime_mean",
            constraints={
                "variant": "nl-loki-scc-hoist",
                "num_cols": NUM_COLS,
                "precision": precision,
            },
            x=4,
            color="khaki",
        ),
        Bar(
            ds_name=os.path.join(
                DATA_DIR, "cloudsc2/lumi/lumi/23.03/cray/8.3.3/cce/15.0.1/performance.csv"
            ),
            col_name="runtime_mean",
            constraints={
                "variant": "nl-gt:cpu_kfirst",
                "num_cols": NUM_COLS,
                "num_threads": NUM_THREADS,
                "precision": precision,
            },
            x=2,
            color="cornflowerblue",
        ),
        Bar(
            ds_name=os.path.join(
                DATA_DIR, "cloudsc2/lumi/lumi/23.03/cray/8.3.3/cce/15.0.1/performance.csv"
            ),
            col_name="runtime_mean",
            constraints={"variant": "nl-dace:gpu", "num_cols": NUM_COLS, "precision": precision},
            x=6,
            color="coral",
        ),
    ]
    data_2 = [
        Bar(
            ds_name=os.path.join(DATA_DIR, "cloudsc2/lumi/cray-gpu/14.0.2/release/performance.csv"),
            col_name="runtime_mean",
            constraints={
                "variant": "ad",
                "num_cols": NUM_COLS,
                "num_threads": NUM_THREADS,
                "precision": precision,
            },
            x=1,
            color="grey",
        ),
        # Bar(
        #     ds_name=os.path.join(DATA_DIR, "cloudsc2/lumi/cray-gpu/14.0.2/bit/performance.csv"),
        #     col_name="runtime_mean",
        #     constraints={
        #         "variant": "ad-loki-scc-hoist",
        #         "num_cols": NUM_COLS,
        #         "precision": precision,
        #     },
        #     x=4,
        #     color="khaki",
        # ),
        Bar(
            ds_name=os.path.join(
                DATA_DIR, "cloudsc2/lumi/lumi/23.03/cray/8.3.3/cce/15.0.1/performance.csv"
            ),
            col_name="runtime_mean",
            constraints={
                "variant": "ad-gt:cpu_kfirst",
                "num_cols": NUM_COLS,
                "num_threads": NUM_THREADS,
                "precision": precision,
            },
            x=2,
            color="cornflowerblue",
        ),
        Bar(
            ds_name=os.path.join(
                DATA_DIR, "cloudsc2/lumi/lumi/23.03/cray/8.3.3/cce/15.0.1/performance.csv"
            ),
            col_name="runtime_mean",
            constraints={"variant": "ad-dace:gpu", "num_cols": NUM_COLS, "precision": precision},
            x=6,
            color="coral",
        ),
    ]
    return data_0, data_1, data_2


@click.command()
@click.option("--show/--no-show", is_flag=True, default=True)
@click.option("--save", is_flag=True, default=False)
def main(show: bool, save: bool) -> None:
    mpl.rcParams["font.size"] = 16
    cm_to_inch = 1 / 2.54
    figsize_in_cm = tuple(dim * cm_to_inch for dim in FIGSIZE_IN_INCH)
    fig = plt.figure(figsize=figsize_in_cm)
    gs = fig.add_gridspec(2, 3, height_ratios=(1, 0.1))
    ax_00 = fig.add_subplot(gs[0, 0])
    ax_01 = fig.add_subplot(gs[0, 1])
    ax_02 = fig.add_subplot(gs[0, 2])
    ax_leg = fig.add_subplot(gs[1, :])

    data_00, data_01, data_02 = get_data("double")
    handles = fill_ax_x0(ax_00, data_00, ylim=(0, 1200))
    ax_00.set_title("(a) CLOUDSC", loc="center", fontsize=17, fontweight="bold")
    fill_ax_x1(ax_01, data_01, ylim=(0, 350))
    ax_01.set_title("(b) CLOUDSC2: Non-linear", loc="center", fontsize=17, fontweight="bold")
    fill_ax_x2(ax_02, data_02, ylim=(0, 1800))
    ax_02.set_title("(c) CLOUDSC2: Symmetry test", loc="center", fontsize=17, fontweight="bold")

    ax_leg.axis("off")
    labels = [item.label for item in data_00]
    ax_leg.legend(
        handles,
        labels,
        loc="center",
        framealpha=1,
        ncol=3,
        fontsize=16,
    )

    fig.tight_layout()
    # plt.subplots_adjust(hspace=0.32)
    if save:
        os.makedirs(IMG_DIR, exist_ok=True)
        fig.savefig(os.path.join(IMG_DIR, "performance_lumi_2.pdf"))
    if show:
        plt.show()


if __name__ == "__main__":
    main()
