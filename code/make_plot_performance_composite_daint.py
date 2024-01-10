# -*- coding: utf-8 -*-
from __future__ import annotations
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
from typing import Any, Literal

from common import Bar, project_root_dir


# config: start
FIGSIZE_IN_INCH: tuple[int, int] = (40, 20)
NUM_COLS: int = 65536
ROOT_DIR: str = os.path.join(project_root_dir, "data")
# config: end


def get_data(precision: Literal["double", "single"]) -> tuple[list[Bar], list[Bar], list[Bar]]:
    # import ipdb
    # ipdb.set_trace()
    data_0 = [
        Bar(
            ds_name=os.path.join(ROOT_DIR, "cloudsc/daint/intel/6.0.10/release/performance.csv"),
            constraints={"variant": "fortran", "num_cols": NUM_COLS, "precision": precision},
            x=1,
            color="grey",
            label="Fortran: OpenMP (CPU)",
        ),
        Bar(
            ds_name=os.path.join(ROOT_DIR, "cloudsc/daint/nvidia/6.0.10/release/performance.csv"),
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
            ds_name=os.path.join(ROOT_DIR, "cloudsc/daint/nvidia/6.0.10/release/performance.csv"),
            constraints={
                "variant": "loki-scc-cuf-hoist",
                "num_cols": NUM_COLS,
                "precision": precision,
            },
            x=4,
            color="khaki",
            label="Fortran: Loki (GPU)",
        ),
        Bar(
            ds_name=os.path.join(ROOT_DIR, "cloudsc/daint/nvidia/6.0.10/release/performance.csv"),
            constraints={"variant": "cuda-k-caching", "num_cols": NUM_COLS, "precision": precision},
            x=5,
            color="green",
            label="C: CUDA",
        ),
        Bar(
            ds_name=os.path.join(ROOT_DIR, "cloudsc/daint/gnu/6.0.10/performance.csv"),
            constraints={"variant": "gt:cpu_kfirst", "num_cols": NUM_COLS, "precision": precision},
            x=2,
            color="cornflowerblue",
            label="GT4Py: CPU k-first",
        ),
        Bar(
            ds_name=os.path.join(ROOT_DIR, "cloudsc/daint/gnu/6.0.10/performance.csv"),
            constraints={"variant": "dace:gpu", "num_cols": NUM_COLS, "precision": precision},
            x=6,
            color="coral",
            label="GT4Py: DaCe (GPU)",
        ),
    ]
    data_1 = [
        Bar(
            ds_name=os.path.join(ROOT_DIR, "cloudsc2/daint/intel/6.0.10/release/performance.csv"),
            constraints={"variant": "nl", "num_cols": NUM_COLS, "precision": precision},
            x=1,
            color="grey",
        ),
        Bar(
            ds_name=os.path.join(ROOT_DIR, "cloudsc2/daint/nvidia/6.0.10/release/performance.csv"),
            constraints={
                "variant": "nl-loki-scc-hoist",
                "num_cols": NUM_COLS,
                "precision": precision,
            },
            x=4,
            color="khaki",
        ),
        Bar(
            ds_name=os.path.join(ROOT_DIR, "cloudsc2/daint/gnu/6.0.10/performance.csv"),
            constraints={
                "variant": "nl-gt:cpu_kfirst",
                "num_cols": NUM_COLS,
                "precision": precision,
            },
            x=2,
            color="cornflowerblue",
        ),
        Bar(
            ds_name=os.path.join(ROOT_DIR, "cloudsc2/daint/gnu/6.0.10/performance.csv"),
            constraints={"variant": "nl-dace:gpu", "num_cols": NUM_COLS, "precision": precision},
            x=6,
            color="coral",
        ),
    ]
    data_2 = [
        Bar(
            ds_name=os.path.join(ROOT_DIR, "cloudsc2/daint/intel/6.0.10/release/performance.csv"),
            constraints={"variant": "ad", "num_cols": NUM_COLS, "precision": precision},
            x=1,
            color="grey",
        ),
        Bar(
            ds_name=os.path.join(ROOT_DIR, "cloudsc2/daint/gnu/6.0.10/performance.csv"),
            constraints={
                "variant": "ad-gt:cpu_kfirst",
                "num_cols": NUM_COLS,
                "precision": precision,
            },
            x=2,
            color="cornflowerblue",
        ),
        Bar(
            ds_name=os.path.join(ROOT_DIR, "cloudsc2/daint/gnu/6.0.10/performance.csv"),
            constraints={"variant": "ad-dace:gpu", "num_cols": NUM_COLS, "precision": precision},
            x=6,
            color="coral",
        ),
    ]
    return data_0, data_1, data_2


def fill_ax_x0(ax: plt.Axes, data: list[Bar], ylim: tuple[int, int]) -> list[Any]:
    handles = []
    for bar in data:
        if bar.y != 0:
            h = ax.bar(bar.x, bar.y, width=bar.width, color=bar.color, edgecolor="black")
            ax.annotate(
                f"{bar.y:.2f}",
                xy=(bar.x, bar.y + 7),
                ha="center",
                va="bottom",
                fontsize=14,
                bbox={"pad": 0.1, "facecolor": "white", "edgecolor": "white"},
            )
        else:
            h = ax.bar(bar.x, -1, width=bar.width, color=bar.color, edgecolor="black")
        handles.append(h)

    ax.set_xlim([0.25, 6.75])
    ax.xaxis.set_ticks([])
    ax.xaxis.set_ticklabels([])

    ax.set_ylim(ylim)
    ax.yaxis.set_ticks(np.linspace(ylim[0], ylim[1], 6, dtype=int))
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, linestyle=":")
    ax.set_ylabel("Runtime [ms]")

    precision = data[0].constraints.get("precision", "double")
    if precision == "double":
        letter = "a"
        dtype = "FP64"
    else:
        letter = "d"
        dtype = "FP32"
    ax.set_title("$\\mathbf{(" + letter + ")}$ CLOUDSC (" + dtype + ")", loc="center", fontsize=16)

    return handles


def fill_ax_x1(ax: plt.Axes, data: list[Bar], ylim: tuple[int, int]) -> None:
    for bar in data:
        if bar.y != 0:
            ax.bar(bar.x, bar.y, width=bar.width, color=bar.color, edgecolor="black")
            ax.annotate(
                f"{bar.y:.2f}",
                xy=(bar.x, bar.y + 4),
                ha="center",
                va="bottom",
                fontsize=14,
                bbox={"pad": 0.1, "facecolor": "white", "edgecolor": "white"},
            )

    ax.set_xlim([0.25, 6.75])
    ax.xaxis.set_ticks([])
    ax.xaxis.set_ticklabels([])

    ax.set_ylim(ylim)
    ax.yaxis.set_ticks(np.linspace(ylim[0], ylim[1], 6, dtype=int))
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, linestyle=":")
    # ax.set_ylabel("Runtime [ms]")

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


def fill_ax_x2(ax: plt.Axes, data: list[Bar], ylim: tuple[int, int]) -> None:
    for bar in data:
        if bar.y != 0:
            ax.bar(bar.x, bar.y, width=bar.width, color=bar.color, edgecolor="black")
            ax.annotate(
                f"{bar.y:.2f}",
                xy=(bar.x, bar.y + 10),
                ha="center",
                va="bottom",
                fontsize=14,
                bbox={"pad": 0.1, "facecolor": "white", "edgecolor": "white"},
            )

    ax.set_xlim([0.25, 6.75])
    ax.xaxis.set_ticks([])
    ax.xaxis.set_ticklabels([])

    ax.set_ylim(ylim)
    ax.yaxis.set_ticks(np.linspace(ylim[0], ylim[1], 6, dtype=int))
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, linestyle=":")
    # ax.set_ylabel("Runtime [ms]")

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
    mpl.rcParams["font.size"] = 16
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

    data_00, data_01, data_02 = get_data("double")
    data_10, data_11, data_12 = get_data("single")
    handles = fill_ax_x0(ax_00, data_00, ylim=(0, 900))
    fill_ax_x0(ax_10, data_10, ylim=(0, 900))
    fill_ax_x1(ax_01, data_01, ylim=(0, 400))
    fill_ax_x1(ax_11, data_11, ylim=(0, 400))
    fill_ax_x2(ax_02, data_02, ylim=(0, 2000))
    fill_ax_x2(ax_12, data_12, ylim=(0, 2000))

    ax_leg.axis("off")
    labels = [item.label for item in data_00]
    ax_leg.legend(
        handles,
        labels,
        loc="center",
        framealpha=1,
        ncol=3,
        fontsize=14,
    )

    fig.tight_layout()
    plt.subplots_adjust(hspace=0.32)
    plt.show()
    # fig.savefig(
    #     "/Users/subbiali/Desktop/kilos/events/202306-PASC23/poster/img/performance_cloudsc_3.pdf"
    # )


if __name__ == "__main__":
    main()
