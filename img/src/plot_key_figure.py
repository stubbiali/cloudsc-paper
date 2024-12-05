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

from common import Bar, CM_TO_INCH, IMG_ROOT_DIR
from plot_runtime_lumi_fp64 import get_data as get_data_lumi
from plot_runtime_mlux import get_data as get_data_mlux


# config: start
FIGSIZE_IN_INCH: tuple[int, int] = (24.6, 20)
# config: end


def fill_ax(ax: plt.Axes, data: list[Bar], text: str) -> list[Any]:
    ylim = (0, 1.2 * data[-2].y)
    yoff = 0.02 * ylim[1]

    handles = []
    for bar in data:
        if bar.y != 0:
            h = ax.bar(bar.x, bar.y, width=bar.width, color=bar.color, edgecolor="black")
            ax.annotate(
                f"{bar.y:.2f}",
                xy=(bar.x, bar.y + yoff),
                ha="center",
                va="bottom",
                fontsize=13,
                bbox={"pad": 0.1, "facecolor": "white", "edgecolor": "white"},
            )
        else:
            h = ax.bar(bar.x, -1, width=bar.width, color=bar.color, edgecolor="black")
        handles.append(h)

    ax.set_xlim([0.25, 6.75])
    ax.xaxis.set_ticks([])
    ax.xaxis.set_ticklabels([])

    ax.set_ylim(ylim)
    ax.yaxis.set_ticks([])
    # ax.yaxis.set_ticks(np.linspace(ylim[0], ylim[1], 6, dtype=int))
    ax.yaxis.set_ticklabels([])
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, linestyle=":")
    # ax.set_ylabel("Runtime [ms]", labelpad=13)

    ax.annotate(
        text, xy=(0.97 * 6.75, 0.97 * ylim[1]), ha="right", va="top", fontsize=13, fontweight="bold"
    )

    return handles


@click.command()
@click.option("--show/--no-show", is_flag=True, default=True)
@click.option("--save", is_flag=True, default=False)
def main(show: bool, save: bool) -> None:
    figsize_in_cm = tuple(dim * CM_TO_INCH for dim in FIGSIZE_IN_INCH)
    fig = plt.figure(figsize=figsize_in_cm)
    gs = fig.add_gridspec(3, 2, height_ratios=(1, 1, 0.2))
    ax_00 = fig.add_subplot(gs[0, 0])
    ax_01 = fig.add_subplot(gs[0, 1])
    ax_10 = fig.add_subplot(gs[1, 0])
    ax_11 = fig.add_subplot(gs[1, 1])
    ax_leg = fig.add_subplot(gs[2, :])

    data_00, _, data_01 = get_data_mlux("double")
    data_10, _, data_11 = get_data_lumi("double")

    handles = fill_ax(ax_00, data_00, text="MeluXina\nFP64")
    ax_00.set_title(
        "Runtime (in ms) for CLOUDSC", loc="center", fontsize=16, fontweight="bold", pad=20
    )

    fill_ax(ax_10, data_10, text="LUMI\nFP64")

    fill_ax(ax_01, data_01, text="MeluXina\nFP64")
    ax_01.set_title(
        "Runtime (in ms) for the\nsymmetry test for CLOUDSC2",
        loc="center",
        fontsize=16,
        fontweight="bold",
        pad=20,
    )

    fill_ax(ax_11, data_11, text="LUMI\nFP64")

    ax_leg.axis("off")
    labels = [item.label for item in data_00]
    ax_leg.legend(
        handles,
        labels,
        loc="center",
        framealpha=1,
        ncol=3,
        fontsize=13.5,
    )

    fig.tight_layout()
    if save:
        os.makedirs(IMG_ROOT_DIR, exist_ok=True)
        fig.savefig(os.path.join(IMG_ROOT_DIR, "final/key_figure.pdf"))
    if show:
        plt.show()


if __name__ == "__main__":
    main()
