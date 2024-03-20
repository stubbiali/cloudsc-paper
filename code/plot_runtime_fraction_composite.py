# -*- coding: utf-8 -*-
from __future__ import annotations
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
from typing import Any, Literal

from common import Bar, NUM_COLS, ROOT_DIR
from plot_runtime_lumi import NUM_THREADS as NUM_THREADS_LUMI
from plot_runtime_mlux import NUM_THREADS as NUM_THREADS_MLUX


# config: start
FIGSIZE_IN_INCH: tuple[int, int] = (40, 20)
# config: end


def get_data(
    ds_name: str, col_name: str, precision: Literal["double", "single"]
) -> tuple[list[Bar], list[Bar], list[Bar]]:
    data_0 = [
        Bar(
            ds_name=os.path.join(ROOT_DIR, f"cloudsc/daint/gnu/6.0.10/{ds_name}"),
            col_name=col_name,
            constraints={"variant": "gt:cpu_kfirst", "num_cols": NUM_COLS, "precision": precision},
            x=1,
            color="cornflowerblue",
            label="CPU k-first",
        ),
        Bar(
            ds_name=os.path.join(ROOT_DIR, f"cloudsc/daint/gnu/6.0.10/{ds_name}"),
            col_name=col_name,
            constraints={"variant": "dace:gpu", "num_cols": NUM_COLS, "precision": precision},
            x=1.5,
            color="coral",
            label="DaCe (GPU)",
        ),
        Bar(
            ds_name=os.path.join(ROOT_DIR, f"cloudsc/mlux/release/2022.1/gnu/11.3.0/{ds_name}"),
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
            ds_name=os.path.join(ROOT_DIR, f"cloudsc/mlux/release/2022.1/gnu/11.3.0/{ds_name}"),
            col_name=col_name,
            constraints={"variant": "dace:gpu", "num_cols": NUM_COLS, "precision": precision},
            x=3,
            color="coral",
        ),
        Bar(
            ds_name=os.path.join(
                ROOT_DIR, f"cloudsc/lumi/lumi/23.03/cray/8.3.3/cce/15.0.1/{ds_name}"
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
                ROOT_DIR, f"cloudsc/lumi/lumi/23.03/cray/8.3.3/cce/15.0.1/{ds_name}"
            ),
            col_name=col_name,
            constraints={"variant": "dace:gpu", "num_cols": NUM_COLS, "precision": precision},
            x=4.5,
            color="coral",
        ),
    ]
    data_1 = [
        Bar(
            ds_name=os.path.join(ROOT_DIR, f"cloudsc2/daint/gnu/6.0.10/{ds_name}"),
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
            ds_name=os.path.join(ROOT_DIR, f"cloudsc2/daint/gnu/6.0.10/{ds_name}"),
            col_name=col_name,
            constraints={"variant": "nl-dace:gpu", "num_cols": NUM_COLS, "precision": precision},
            x=1.5,
            color="coral",
        ),
        Bar(
            ds_name=os.path.join(ROOT_DIR, f"cloudsc2/mlux/release/2022.1/gnu/11.3.0/{ds_name}"),
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
            ds_name=os.path.join(ROOT_DIR, f"cloudsc2/mlux/release/2022.1/gnu/11.3.0/{ds_name}"),
            col_name=col_name,
            constraints={"variant": "nl-dace:gpu", "num_cols": NUM_COLS, "precision": precision},
            x=3,
            color="coral",
        ),
        Bar(
            ds_name=os.path.join(
                ROOT_DIR, f"cloudsc2/lumi/lumi/23.03/cray/8.3.3/cce/15.0.1/{ds_name}"
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
                ROOT_DIR, f"cloudsc2/lumi/lumi/23.03/cray/8.3.3/cce/15.0.1/{ds_name}"
            ),
            col_name=col_name,
            constraints={"variant": "nl-dace:gpu", "num_cols": NUM_COLS, "precision": precision},
            x=4.5,
            color="coral",
        ),
    ]
    data_2 = [
        Bar(
            ds_name=os.path.join(ROOT_DIR, f"cloudsc2/daint/gnu/6.0.10/{ds_name}"),
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
            ds_name=os.path.join(ROOT_DIR, f"cloudsc2/daint/gnu/6.0.10/{ds_name}"),
            col_name=col_name,
            constraints={"variant": "ad-dace:gpu", "num_cols": NUM_COLS, "precision": precision},
            x=1.5,
            color="coral",
        ),
        Bar(
            ds_name=os.path.join(ROOT_DIR, f"cloudsc2/mlux/release/2022.1/gnu/11.3.0/{ds_name}"),
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
            ds_name=os.path.join(ROOT_DIR, f"cloudsc2/mlux/release/2022.1/gnu/11.3.0/{ds_name}"),
            col_name=col_name,
            constraints={"variant": "ad-dace:gpu", "num_cols": NUM_COLS, "precision": precision},
            x=3,
            color="coral",
        ),
        Bar(
            ds_name=os.path.join(
                ROOT_DIR, f"cloudsc2/lumi/lumi/23.03/cray/8.3.3/cce/15.0.1/{ds_name}"
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
                ROOT_DIR, f"cloudsc2/lumi/lumi/23.03/cray/8.3.3/cce/15.0.1/{ds_name}"
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
        h1 = ax.bar(bar.x, y1, width=bar.width, color=bar.color, edgecolor="black")
        ax.bar(bar.x, y2, bottom=y1, width=bar.width, color=bar.color, hatch="//")
        ax.bar(bar.x, y2, bottom=y1, width=bar.width, color="none", edgecolor="black")
        if len(handles) < 2:
            handles.append(h1)
    handles.append(ax.bar(0, 0, color="none", edgecolor="black"))
    handles.append(ax.bar(0, 0, color="none", edgecolor="black", hatch="//"))

    ax.set_xlim([0.25, 5.25])
    ax.xaxis.set_ticks([1.25, 2.75, 4.25])
    ax.xaxis.set_ticklabels(["Daint", "MLux", "LUMI"])
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
        ax.bar(bar.x, y1, width=bar.width, color=bar.color, edgecolor="black")
        ax.bar(bar.x, y2, bottom=y1, width=bar.width, color=bar.color, hatch="//")
        ax.bar(bar.x, y2, bottom=y1, width=bar.width, color="none", edgecolor="black")

    ax.set_xlim([0.25, 5.25])
    ax.xaxis.set_ticks([1.25, 2.75, 4.25])
    ax.xaxis.set_ticklabels(["Daint", "MLux", "LUMI"])
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
        ax.bar(bar.x, y1, width=bar.width, color=bar.color, edgecolor="black")
        ax.bar(bar.x, y2, bottom=y1, width=bar.width, color=bar.color, hatch="//")
        ax.bar(bar.x, y2, bottom=y1, width=bar.width, color="none", edgecolor="black")

    ax.set_xlim([0.25, 5.25])
    ax.xaxis.set_ticks([1.25, 2.75, 4.25])
    ax.xaxis.set_ticklabels(["Daint", "MLux", "LUMI"])
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


def main() -> None:
    plt.rcParams["font.size"] = 16
    plt.rcParams["hatch.color"] = "white"
    plt.rcParams["hatch.linewidth"] = 3

    cm_to_inch = 1 / 2.54
    figsize_in_cm = tuple(dim * cm_to_inch for dim in FIGSIZE_IN_INCH)
    fig = plt.figure(figsize=figsize_in_cm)
    gs = fig.add_gridspec(3, 3, height_ratios=(1, 1, 0.05))
    ax_00 = fig.add_subplot(gs[0, 0])
    ax_01 = fig.add_subplot(gs[0, 1])
    ax_02 = fig.add_subplot(gs[0, 2])
    ax_10 = fig.add_subplot(gs[1, 0])
    ax_11 = fig.add_subplot(gs[1, 1])
    ax_12 = fig.add_subplot(gs[1, 2])
    ax_leg = fig.add_subplot(gs[2, :])

    data_00, data_01, data_02 = get_data("performance.csv", "runtime_mean", "double")
    data_stencils_00, data_stencils_01, data_stencils_02 = get_data(
        "performance_stencils.csv", "stencils", "double"
    )
    data_10, data_11, data_12 = get_data("performance.csv", "runtime_mean", "single")
    data_stencils_10, data_stencils_11, data_stencils_12 = get_data(
        "performance_stencils.csv", "stencils", "single"
    )
    handles = fill_ax_x0(ax_00, data_00, data_stencils_00)
    fill_ax_x0(ax_10, data_10, data_stencils_10)
    fill_ax_x1(ax_01, data_01, data_stencils_01)
    fill_ax_x1(ax_11, data_11, data_stencils_11)
    fill_ax_x2(ax_02, data_02, data_stencils_02)
    fill_ax_x2(ax_12, data_12, data_stencils_12)

    ax_leg.axis("off")
    labels = [
        data_00[0].label,
        data_00[1].label,
        "Stencil computations (generated code)",
        "Framework (Python)",
    ]
    ax_leg.legend(
        handles,
        labels,
        loc="center",
        framealpha=1,
        ncol=2,
        fontsize=14,
    )

    fig.tight_layout()
    plt.subplots_adjust(hspace=0.38)
    plt.show()
    # fig.savefig(
    #     "/Users/subbiali/Desktop/kilos/events/202306-PASC23/poster/img/performance_cloudsc_3.pdf"
    # )


if __name__ == "__main__":
    main()
