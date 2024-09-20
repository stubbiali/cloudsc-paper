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
import matplotlib.pyplot as plt
import os
from typing import Any, Literal

from common import Bar, DATA_DIR, IMG_DIR, NUM_COLS
from plot_runtime_lumi import NUM_THREADS as NUM_THREADS_LUMI
from plot_runtime_mlux import NUM_THREADS as NUM_THREADS_MLUX


# config: start
FIGSIZE_IN_INCH: tuple[int, int] = (40, 14)
# config: end


def get_data(
    ds_name: str, col_name: str, precision: Literal["double", "single"]
) -> tuple[list[Bar], list[Bar], list[Bar]]:
    data_0 = [
        Bar(
            ds_name=os.path.join(DATA_DIR, f"cloudsc/daint/gnu/6.0.10/{ds_name}"),
            col_name=col_name,
            constraints={"variant": "gt:cpu_kfirst", "num_cols": NUM_COLS, "precision": precision},
            x=1,
            color="cornflowerblue",
            label="CPU k-first",
        ),
        Bar(
            ds_name=os.path.join(DATA_DIR, f"cloudsc/daint/gnu/6.0.10/{ds_name}"),
            col_name=col_name,
            constraints={"variant": "dace:gpu", "num_cols": NUM_COLS, "precision": precision},
            x=1.5,
            color="coral",
            label="DaCe (GPU)",
        ),
        Bar(
            ds_name=os.path.join(DATA_DIR, f"cloudsc/mlux/release/2022.1/gnu/11.3.0/{ds_name}"),
            col_name=col_name,
            constraints={
                "variant": "gt:cpu_kfirst",
                "num_cols": NUM_COLS,
                "num_threads": NUM_THREADS_MLUX,
                "precision": precision,
            },
            x=2.5,
            color="cornflowerblue",
        ),
        Bar(
            ds_name=os.path.join(DATA_DIR, f"cloudsc/mlux/release/2022.1/gnu/11.3.0/{ds_name}"),
            col_name=col_name,
            constraints={"variant": "dace:gpu", "num_cols": NUM_COLS, "precision": precision},
            x=3,
            color="coral",
        ),
        Bar(
            ds_name=os.path.join(
                DATA_DIR, f"cloudsc/lumi/lumi/23.03/cray/8.3.3/cce/15.0.1/{ds_name}"
            ),
            col_name=col_name,
            constraints={
                "variant": "gt:cpu_kfirst",
                "num_cols": NUM_COLS,
                "num_threads": NUM_THREADS_LUMI,
                "precision": precision,
            },
            x=4,
            color="cornflowerblue",
        ),
        Bar(
            ds_name=os.path.join(
                DATA_DIR, f"cloudsc/lumi/lumi/23.03/cray/8.3.3/cce/15.0.1/{ds_name}"
            ),
            col_name=col_name,
            constraints={"variant": "dace:gpu", "num_cols": NUM_COLS, "precision": precision},
            x=4.5,
            color="coral",
        ),
    ]
    data_1 = [
        Bar(
            ds_name=os.path.join(DATA_DIR, f"cloudsc2/daint/gnu/6.0.10/{ds_name}"),
            col_name=col_name,
            constraints={
                "variant": "nl-gt:cpu_kfirst",
                "num_cols": NUM_COLS,
                "precision": precision,
            },
            x=1,
            color="cornflowerblue",
        ),
        Bar(
            ds_name=os.path.join(DATA_DIR, f"cloudsc2/daint/gnu/6.0.10/{ds_name}"),
            col_name=col_name,
            constraints={"variant": "nl-dace:gpu", "num_cols": NUM_COLS, "precision": precision},
            x=1.5,
            color="coral",
        ),
        Bar(
            ds_name=os.path.join(DATA_DIR, f"cloudsc2/mlux/release/2022.1/gnu/11.3.0/{ds_name}"),
            col_name=col_name,
            constraints={
                "variant": "nl-gt:cpu_kfirst",
                "num_cols": NUM_COLS,
                "num_threads": NUM_THREADS_MLUX,
                "precision": precision,
            },
            x=2.5,
            color="cornflowerblue",
        ),
        Bar(
            ds_name=os.path.join(DATA_DIR, f"cloudsc2/mlux/release/2022.1/gnu/11.3.0/{ds_name}"),
            col_name=col_name,
            constraints={"variant": "nl-dace:gpu", "num_cols": NUM_COLS, "precision": precision},
            x=3,
            color="coral",
        ),
        Bar(
            ds_name=os.path.join(
                DATA_DIR, f"cloudsc2/lumi/lumi/23.03/cray/8.3.3/cce/15.0.1/{ds_name}"
            ),
            col_name=col_name,
            constraints={
                "variant": "nl-gt:cpu_kfirst",
                "num_cols": NUM_COLS,
                "num_threads": NUM_THREADS_LUMI,
                "precision": precision,
            },
            x=4,
            color="cornflowerblue",
        ),
        Bar(
            ds_name=os.path.join(
                DATA_DIR, f"cloudsc2/lumi/lumi/23.03/cray/8.3.3/cce/15.0.1/{ds_name}"
            ),
            col_name=col_name,
            constraints={"variant": "nl-dace:gpu", "num_cols": NUM_COLS, "precision": precision},
            x=4.5,
            color="coral",
        ),
    ]
    data_2 = [
        Bar(
            ds_name=os.path.join(DATA_DIR, f"cloudsc2/daint/gnu/6.0.10/{ds_name}"),
            col_name=col_name,
            constraints={
                "variant": "ad-gt:cpu_kfirst",
                "num_cols": NUM_COLS,
                "precision": precision,
            },
            x=1,
            color="cornflowerblue",
        ),
        Bar(
            ds_name=os.path.join(DATA_DIR, f"cloudsc2/daint/gnu/6.0.10/{ds_name}"),
            col_name=col_name,
            constraints={"variant": "ad-dace:gpu", "num_cols": NUM_COLS, "precision": precision},
            x=1.5,
            color="coral",
        ),
        Bar(
            ds_name=os.path.join(DATA_DIR, f"cloudsc2/mlux/release/2022.1/gnu/11.3.0/{ds_name}"),
            col_name=col_name,
            constraints={
                "variant": "ad-gt:cpu_kfirst",
                "num_cols": NUM_COLS,
                "num_threads": NUM_THREADS_MLUX,
                "precision": precision,
            },
            x=2.5,
            color="cornflowerblue",
        ),
        Bar(
            ds_name=os.path.join(DATA_DIR, f"cloudsc2/mlux/release/2022.1/gnu/11.3.0/{ds_name}"),
            col_name=col_name,
            constraints={"variant": "ad-dace:gpu", "num_cols": NUM_COLS, "precision": precision},
            x=3,
            color="coral",
        ),
        Bar(
            ds_name=os.path.join(
                DATA_DIR, f"cloudsc2/lumi/lumi/23.03/cray/8.3.3/cce/15.0.1/{ds_name}"
            ),
            col_name=col_name,
            constraints={
                "variant": "ad-gt:cpu_kfirst",
                "num_cols": NUM_COLS,
                "num_threads": NUM_THREADS_LUMI,
                "precision": precision,
            },
            x=4,
            color="cornflowerblue",
        ),
        Bar(
            ds_name=os.path.join(
                DATA_DIR, f"cloudsc2/lumi/lumi/23.03/cray/8.3.3/cce/15.0.1/{ds_name}"
            ),
            col_name=col_name,
            constraints={"variant": "ad-dace:gpu", "num_cols": NUM_COLS, "precision": precision},
            x=4.5,
            color="coral",
        ),
    ]
    return data_0, data_1, data_2


def fill_ax_x0(ax: plt.Axes, data: list[Bar], data_stencils: list[Bar]) -> list[Any]:
    handles = []
    for bar, bar_stencil in zip(data, data_stencils):
        y1 = bar_stencil.y / bar.y
        y2 = 1 - y1
        # print(f"{100*y1=:.4f} {100*y2=:.4f}")
        h1 = ax.bar(bar.x, y1, width=bar.width, color=bar.color, edgecolor="black")
        ax.bar(bar.x, y2, bottom=y1, width=bar.width, color=bar.color, hatch="//")
        ax.bar(bar.x, y2, bottom=y1, width=bar.width, color="none", edgecolor="black")
        if len(handles) < 2:
            handles.append(h1)
    handles.append(ax.bar(0, 0, color="none", edgecolor="black"))
    handles.append(ax.bar(0, 0, color="none", edgecolor="black", hatch="//"))

    ax.set_xlim([0.25, 5.25])
    ax.xaxis.set_ticks([1.25, 2.75, 4.25])
    ax.xaxis.set_ticklabels(["Piz Daint", "MeluXina", "LUMI"])
    ax.xaxis.set_tick_params(length=0)

    ax.set_ylim([0, 1.1])
    ax.yaxis.set_ticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, linestyle=":")
    ax.set_ylabel("Fraction of runtime [-]")

    precision = data[0].constraints.get("precision", "double")
    if precision == "double":
        letter = "a"
        dtype = "FP64"
    else:
        letter = "d"
        dtype = "FP32"
    ax.set_title("$\\mathbf{(" + letter + ")}$ CLOUDSC (" + dtype + ")", loc="center", fontsize=16)

    return handles


def fill_ax_x1(ax: plt.Axes, data: list[Bar], data_stencils: list[Bar]) -> None:
    for bar, bar_stencil in zip(data, data_stencils):
        y1 = bar_stencil.y / bar.y
        y2 = 1 - y1
        # print(f"{100*y1=:.4f} {100*y2=:.4f}")
        ax.bar(bar.x, y1, width=bar.width, color=bar.color, edgecolor="black")
        ax.bar(bar.x, y2, bottom=y1, width=bar.width, color=bar.color, hatch="//")
        ax.bar(bar.x, y2, bottom=y1, width=bar.width, color="none", edgecolor="black")

    ax.set_xlim([0.25, 5.25])
    ax.xaxis.set_ticks([1.25, 2.75, 4.25])
    ax.xaxis.set_ticklabels(["Piz Daint", "MeluXina", "LUMI"])
    ax.xaxis.set_tick_params(length=0)

    ax.set_ylim([0, 1.1])
    ax.yaxis.set_ticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax.yaxis.set_ticklabels([])
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, linestyle=":")

    precision = data[0].constraints.get("precision", "double")
    if precision == "double":
        letter = "b"
        dtype = "FP64"
    else:
        letter = "e"
        dtype = "FP32"
    ax.set_title(
        "$\\mathbf{(" + letter + ")}$ CLOUDSC2: Non-linear (" + dtype + ")",
        loc="center",
        fontsize=16,
    )


def fill_ax_x2(ax: plt.Axes, data: list[Bar], data_stencils: list[Bar]) -> None:
    for bar, bar_stencil in zip(data, data_stencils):
        y1 = bar_stencil.y / bar.y
        y2 = 1 - y1
        # print(f"{100*y1=:.4f} {100*y2=:.4f}")
        ax.bar(bar.x, y1, width=bar.width, color=bar.color, edgecolor="black")
        ax.bar(bar.x, y2, bottom=y1, width=bar.width, color=bar.color, hatch="//")
        ax.bar(bar.x, y2, bottom=y1, width=bar.width, color="none", edgecolor="black")

    ax.set_xlim([0.25, 5.25])
    ax.xaxis.set_ticks([1.25, 2.75, 4.25])
    ax.xaxis.set_ticklabels(["Piz Daint", "MeluXina", "LUMI"])
    ax.xaxis.set_tick_params(length=0)

    ax.set_ylim([0, 1.1])
    ax.yaxis.set_ticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax.yaxis.set_ticklabels([])
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, linestyle=":")

    precision = data[0].constraints.get("precision", "double")
    if precision == "double":
        letter = "c"
        dtype = "FP64"
    else:
        letter = "f"
        dtype = "FP32"
    ax.set_title(
        "$\\mathbf{(" + letter + ")}$ CLOUDSC2: Symmetry test (" + dtype + ")",
        loc="center",
        fontsize=16,
    )


@click.command()
@click.option("--show/--no-show", is_flag=True, default=True)
@click.option("--save", is_flag=True, default=False)
def main(show: bool, save: bool) -> None:
    plt.rcParams["font.size"] = 16
    plt.rcParams["hatch.color"] = "white"
    plt.rcParams["hatch.linewidth"] = 3

    cm_to_inch = 1 / 2.54
    figsize_in_cm = tuple(dim * cm_to_inch for dim in FIGSIZE_IN_INCH)
    fig = plt.figure(figsize=figsize_in_cm)
    gs = fig.add_gridspec(2, 3, height_ratios=(1, 0.10))
    ax_00 = fig.add_subplot(gs[0, 0])
    ax_01 = fig.add_subplot(gs[0, 1])
    ax_02 = fig.add_subplot(gs[0, 2])
    ax_leg = fig.add_subplot(gs[1, :])

    data_00, data_01, data_02 = get_data("performance.csv", "runtime_mean", "double")
    data_stencils_00, data_stencils_01, data_stencils_02 = get_data(
        "performance_stencils.csv", "stencils", "double"
    )
    handles = fill_ax_x0(ax_00, data_00, data_stencils_00)
    ax_00.set_title("(a) CLOUDSC", loc="center", fontsize=17, fontweight="bold")
    fill_ax_x1(ax_01, data_01, data_stencils_01)
    ax_01.set_title("(b) CLOUDSC2: Non-linear", loc="center", fontsize=17, fontweight="bold")
    fill_ax_x2(ax_02, data_02, data_stencils_02)
    ax_02.set_title("(c) CLOUDSC2: Symmetry test", loc="center", fontsize=17, fontweight="bold")

    ax_leg.axis("off")
    labels = [
        data_00[0].label,
        data_00[1].label,
        "Stencil computations (GT4Py generated code)",
        "Python overhead (Tasmania infrastructure and framework)",
    ]
    ax_leg.legend(
        handles,
        labels,
        loc="center",
        framealpha=1,
        ncol=2,
        fontsize=16,
    )

    fig.tight_layout()
    plt.subplots_adjust(hspace=0.38)
    if save:
        os.makedirs(IMG_DIR, exist_ok=True)
        fig.savefig(os.path.join(IMG_DIR, "runtime_fraction_1.pdf"))
    if show:
        plt.show()


if __name__ == "__main__":
    main()
