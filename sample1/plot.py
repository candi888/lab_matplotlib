from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
import matplotlib.ticker as ticker
import numpy as np
from matplotlib.axes import Axes
from matplotlib.collections import PathCollection
from matplotlib.figure import Figure
from matplotlib.legend import Legend
from matplotlib.lines import Line2D


def set_mplparams_init(
    is_use_TimesNewRoman_in_mathtext: bool,
    axis_lw: float,
    is_plot_mticks_x: bool,
    is_plot_mticks_y: bool,
) -> None:
    # 描画高速化
    mplstyle.use("fast")

    # svg用の設定
    mpl.use("Agg")
    plt.rcParams["svg.fonttype"] = "none"

    # MatplotlibのデフォルトフォントをTimes New Romanに設定
    plt.rcParams["font.family"] = "Times New Roman"

    # mathtext関連
    if is_use_TimesNewRoman_in_mathtext:
        plt.rcParams["mathtext.fontset"] = "custom"
        plt.rcParams["mathtext.it"] = "Times New Roman:italic"
        plt.rcParams["mathtext.bf"] = "Times New Roman:bold"
        plt.rcParams["mathtext.bfit"] = "Times New Roman:italic:bold"
        plt.rcParams["mathtext.rm"] = "Times New Roman"
        plt.rcParams["mathtext.fallback"] = "cm"
    else:
        plt.rcParams["mathtext.fontset"] = "cm"

    # x軸,y軸の目盛りの向き
    plt.rcParams["xtick.direction"] = "out"
    plt.rcParams["ytick.direction"] = "out"

    # 軸関係
    plt.rcParams["axes.linewidth"] = axis_lw
    plt.rcParams["xtick.minor.visible"] = is_plot_mticks_x
    plt.rcParams["ytick.minor.visible"] = is_plot_mticks_y

    # 凡例の見た目設定
    plt.rcParams["legend.fancybox"] = False  # 丸角OFF
    plt.rcParams["legend.framealpha"] = 1  # 透明度の指定、0で塗りつぶしなし
    plt.rcParams["legend.edgecolor"] = "black"  # edgeの色を変更

    return


def standardize_legend_sizes(
    legend: Legend,
    legend_lines_lw: float | None,
    legend_scatters_size: float | None,
) -> None:
    for idx, handle in enumerate(legend.legend_handles):
        if isinstance(handle, Line2D) and legend_lines_lw is not None:
            # Line2Dの場合は線の太さを設定
            legend.legend_handles[idx].set_linewidth(legend_lines_lw)
        elif isinstance(handle, PathCollection) and legend_scatters_size is not None:
            # PathCollection（scatter）の場合はマーカーサイズを設定
            legend.legend_handles[idx]._sizes = [legend_scatters_size]

    return


def set_fig_ax(
    fig_horizontal_cm: float, fig_vertical_cm: float, dpi: int, is_aspect_equal: bool
) -> tuple[Figure, Axes]:
    scaler_cm_to_inch = 1 / 2.54

    fig = plt.figure(
        figsize=(
            fig_horizontal_cm * scaler_cm_to_inch,
            fig_vertical_cm * scaler_cm_to_inch,
        ),
        dpi=dpi,
        layout="constrained",
    )
    ax = fig.add_subplot(1, 1, 1)
    if is_aspect_equal:
        ax.set_aspect("equal")

    return fig, ax


def set_ax_lim(ax: Axes, xmin: float, xmax: float, ymin: float, ymax: float) -> None:
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    return


def set_ax_xticks(
    ax: Axes,
    space_x_ticks: float,
    anchor_x_ticks: float,
    strformatter_x: str | None,
    is_plot_mticks_x: bool,
    num_x_mtick: int,
    xticks_font_size: float,
) -> None:
    ax.xaxis.set_major_locator(
        ticker.MultipleLocator(base=space_x_ticks, offset=anchor_x_ticks)
    )

    if strformatter_x is not None:
        ax.xaxis.set_major_formatter(ticker.FormatStrFormatter(strformatter_x))

    if is_plot_mticks_x:
        ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(n=num_x_mtick + 1))

    ax.tick_params(axis="x", labelsize=xticks_font_size)

    return


def set_ax_yticks(
    ax: Axes,
    space_y_ticks: float,
    anchor_y_ticks: float,
    strformatter_y: str | None,
    is_plot_mticks_y: bool,
    num_y_mtick: int,
    yticks_font_size: float,
) -> None:
    ax.yaxis.set_major_locator(
        ticker.MultipleLocator(base=space_y_ticks, offset=anchor_y_ticks)
    )

    if strformatter_y is not None:
        ax.yaxis.set_major_formatter(ticker.FormatStrFormatter(strformatter_y))

    if is_plot_mticks_y:
        ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(n=num_y_mtick + 1))

    ax.tick_params(axis="y", labelsize=yticks_font_size)

    return


def set_ax_xticks_log(
    ax: Axes,
    log_base_x: int,
    log_num_xticks: int | None,
    is_log_plot_mticks_x: bool,
    xticks_font_size: float,
) -> None:
    ax.set_xscale("log")
    ax.xaxis.set_major_locator(
        ticker.LogLocator(base=log_base_x, numticks=log_num_xticks)
    )
    ax.xaxis.set_major_formatter(ticker.LogFormatterMathtext(base=log_base_x))

    # フォントサイズ
    ax.tick_params(axis="x", labelsize=xticks_font_size)

    # 副目盛り
    if is_log_plot_mticks_x:
        ax.xaxis.set_minor_locator(ticker.LogLocator(base=log_base_x, subs="auto"))
    else:
        ax.xaxis.minorticks_off()

    return


def set_ax_yticks_log(
    ax: Axes,
    log_base_y: int,
    log_num_yticks: int | None,
    is_log_plot_mticks_y: bool,
    yticks_font_size: float,
) -> None:
    ax.set_yscale("log")
    ax.yaxis.set_major_locator(
        ticker.LogLocator(base=log_base_y, numticks=log_num_yticks)
    )
    ax.yaxis.set_major_formatter(ticker.LogFormatterMathtext(base=log_base_y))

    # フォントサイズ
    ax.tick_params(axis="y", labelsize=yticks_font_size)

    # 副目盛り
    if is_log_plot_mticks_y:
        ax.yaxis.set_minor_locator(ticker.LogLocator(base=log_base_y, subs="auto"))
    else:
        ax.yaxis.minorticks_off()

    return


def set_xlabel(
    ax: Axes,
    xlabel_text: str,
    xlabel_pos: float,
    ymin: float,
    xlabel_offset: float,
    xlabel_font_size: float,
) -> None:
    ax.text(
        s=xlabel_text,
        x=xlabel_pos,
        y=ymin + xlabel_offset,
        horizontalalignment="center",
        verticalalignment="top",
        fontsize=xlabel_font_size,
        gid="x_title_text",
    )
    return


def set_ylabel(
    ax: Axes,
    ylabel_text: str,
    ylabel_pos: float,
    xmin: float,
    ylabel_offset: float,
    ylabel_font_size: float,
    is_horizontal_ylabel: bool,
) -> None:
    tmp = ax.text(
        s=ylabel_text,
        y=ylabel_pos,
        x=xmin + ylabel_offset,
        verticalalignment="center",
        horizontalalignment="right",
        fontsize=ylabel_font_size,
        gid="y_title_text",
    )

    if not is_horizontal_ylabel:
        tmp.set_rotation("vertical")

    return


def set_gridline(ax: Axes, gridline_style: str) -> None:
    ax.grid(linestyle=gridline_style)
    ax.set_axisbelow(True)

    return


# 長さ等は特記がない限りはポイント単位
def main() -> None:
    # ! ---↓基本設定１------------------------------------------------
    # *---出力画像の大きさ [cm]---
    # （参考）A4用紙の縦向きサイズ（縦 × 横）は 29.7 × 21.0[cm]
    fig_vertical_cm = 8.0  # 縦方向
    fig_horizontal_cm = 18.0  # 横方向
    # *---出力画像の大きさ [cm]---

    # *---全体の見た目の設定----
    axis_lw = 0.8  # 軸線の太さ
    is_aspect_equal = False  # グラフのx軸,y軸のアスペクト比を1:1で固定するか
    plt.rcParams["xtick.top"] = False  # 上側の軸の目盛りを表示するか
    plt.rcParams["axes.spines.top"] = True  # 上側の軸を表示するか
    plt.rcParams["ytick.right"] = False  # 右側の軸の目盛りを表示するか
    plt.rcParams["axes.spines.right"] = True  # 右側の軸を表示するか
    # *---全体の見た目の設定----

    # *---フォント関連---
    base_font_size = 11  # 基準フォントサイズ
    xlabel_font_size = base_font_size + 2  # x軸タイトルのフォントサイズ
    ylabel_font_size = base_font_size + 2  # y軸タイトルのフォントサイズ
    xticks_font_size = base_font_size  # x軸目盛りの値のフォントサイズ
    yticks_font_size = base_font_size  # y軸目盛りの値のフォントサイズ
    legend_font_size = 15  # 凡例のフォントサイズ
    is_use_TimesNewRoman_in_mathtext = True  # 数式で可能な限りTimes New Romanを使うか（FalseでTeXっぽいフォントを使う）
    # *---フォント関連---

    # *---グラフの表示範囲の設定---
    xmin = 0  # x座標の最小値
    xmax = 20  # x座標の最大値
    ymin = -0.12  # y座標の最小値
    ymax = 0.16  # y座標の最大値
    # *---グラフの表示範囲の設定---

    # *---目盛りの設定（x軸）---
    # -主目盛り-
    anchor_x_ticks = 0.0  # 主目盛りで必ず表示する座標
    space_x_ticks = 10.0  # 主目盛りの間隔
    strformatter_x = "%.1f"  # 主目盛りの値の書式等を変更したいときにいじる（変更しない場合はNoneにする）．
    plt.rcParams["xtick.major.pad"] = 4.0  # x軸主目盛りから目盛りラベルをどれだけ離すか
    plt.rcParams["xtick.major.width"] = axis_lw  # x軸主目盛り線の線幅
    plt.rcParams["xtick.major.size"] = 4  # x軸主目盛り線の長さ
    # -副目盛り-
    is_plot_mticks_x = True  # 副目盛りをプロットするか
    num_x_mtick = 3  # 副目盛りの数
    plt.rcParams["xtick.minor.width"] = axis_lw  # x軸補助目盛り線の線幅
    plt.rcParams["xtick.minor.size"] = 2  # x軸補助目盛り線の長さ
    # *---目盛りの設定（x軸）---

    # *---（対数軸）目盛りの設定（x軸）---
    # -対数軸プロットを行うか-
    is_log_ticks_x = False
    # -主目盛り-
    log_base_x = 10  # 基底
    log_num_xticks = None  # 「主目盛りのプロット数-1」を指定（自動の場合はNone）
    # -副目盛り-
    is_log_plot_mticks_x = (
        True  # 副目盛りをプロットするか（log_num_xticksによってはプロットされない）
    )
    # *---（対数軸）目盛りの設定（x軸）---

    # *---目盛りの設定（y軸）---
    # -主目盛り-
    anchor_y_ticks = 0.0  # 主目盛りで必ず表示する座標
    space_y_ticks = 0.1  # 主目盛りの間隔
    strformatter_y = None  # 主目盛りの値の書式等を変更したいときにいじる（変更しない場合はNoneにする）．
    plt.rcParams["ytick.major.pad"] = 4.0  # y軸主目盛りから目盛りラベルをどれだけ離すか
    plt.rcParams["ytick.major.width"] = axis_lw  # y軸主目盛り線の線幅
    plt.rcParams["ytick.major.size"] = 4  # y軸主目盛り線の長さ
    # -副目盛り-
    is_plot_mticks_y = True  # 副目盛りをプロットするか
    num_y_mtick = 3  # 副目盛りの数
    plt.rcParams["ytick.minor.width"] = axis_lw  # y軸補助目盛り線の線幅
    plt.rcParams["ytick.minor.size"] = 2  # y軸補助目盛り線の長さ
    # *---目盛りの設定（y軸）---

    # *---（対数軸）目盛りの設定（x軸）---
    # -対数軸プロットを行うか-
    is_log_ticks_y = False
    # -主目盛り-
    log_base_y = 10  # 基底
    log_num_yticks = 2  # 「主目盛りのプロット数-1」を指定（自動の場合はNone）
    # -副目盛り-
    is_log_plot_mticks_y = (
        True  # 副目盛りをプロットするか（log_num_xticksによってはプロットされない）
    )
    # *---（対数軸）目盛りの設定（x軸）---

    # *---軸ラベルの設定（x軸）---
    xlabel_text = r"$t \, \mathrm{(s)}$"  # ラベルのテキスト
    xlabel_pos = 17.5  # テキストの中心のx座標
    xlabel_offset = -0.013  # yminからの，テキストの上端のy座標の変位
    # *---軸ラベルの設定（x軸）---

    # *---軸ラベルの設定（y軸）---
    ylabel_text = r"$y \, \mathrm{(m)}$"  # ラベルのテキスト
    ylabel_pos = 0.14  # テキストの中心のy座標
    ylabel_offset = -0.3  # xminからの，テキストの右端のx座標の変位
    is_horizontal_ylabel = True  # ラベルを横向きにするか
    # *---軸ラベルの設定（y軸）---

    # *---グリッド線---
    is_plot_girdline = False  # グリッド線をプロットするか
    gridline_style = "--"  # グリッド線のスタイル（破線など）
    # *---グリッド線---

    # *---画像保存時の設定---
    # 画質設定（dpi）;（よく使う設定）png -> 300，jpeg -> 600
    dpi = 600
    # 拡張子の選択
    extension_list = [
        "jpeg",
        # "png",
        "svg",
        "pdf",
        # "eps",
    ]
    # 保存名（拡張子なし）
    output_filename_withoutextention = "sample1_res"
    # *---画像保存時の設定---
    # ! ---↑基本設定１------------------------------------------------

    # print_debug
    print("プロット開始")
    print("デバッグ用出力（設定を忘れやすいもの一覧）")
    print(f"- Times New Romanをmathtextで使用: {is_use_TimesNewRoman_in_mathtext}")
    print(f"- グラフのアスペクト比を1:1に固定するか: {is_aspect_equal}")
    print(f"- 用紙サイズ（縦 × 横）: ({fig_vertical_cm}cm × {fig_horizontal_cm}cm)")
    print(f"- 対数プロットモード（x軸）: {is_log_ticks_x}")
    print(f"- 対数プロットモード（y軸）: {is_log_ticks_y}")
    print(f"- dpi: {dpi} ")
    print(f"- 保存する形式一覧: {extension_list}")

    set_mplparams_init(
        is_use_TimesNewRoman_in_mathtext=is_use_TimesNewRoman_in_mathtext,
        axis_lw=axis_lw,
        is_plot_mticks_x=is_plot_mticks_x,
        is_plot_mticks_y=is_plot_mticks_y,
    )

    fig, ax = set_fig_ax(
        fig_horizontal_cm=fig_horizontal_cm,
        fig_vertical_cm=fig_vertical_cm,
        dpi=dpi,
        is_aspect_equal=is_aspect_equal,
    )

    set_ax_lim(ax=ax, xmin=xmin, xmax=xmax, ymin=ymin, ymax=ymax)

    if is_log_ticks_x:
        set_ax_xticks_log(
            ax=ax,
            log_base_x=log_base_x,
            log_num_xticks=log_num_xticks,
            is_log_plot_mticks_x=is_log_plot_mticks_x,
            xticks_font_size=xticks_font_size,
        )
    else:
        set_ax_xticks(
            ax=ax,
            space_x_ticks=space_x_ticks,
            anchor_x_ticks=anchor_x_ticks,
            strformatter_x=strformatter_x,
            is_plot_mticks_x=is_plot_mticks_x,
            num_x_mtick=num_x_mtick,
            xticks_font_size=xticks_font_size,
        )

    if is_log_ticks_y:
        set_ax_yticks_log(
            ax=ax,
            log_base_y=log_base_y,
            log_num_yticks=log_num_yticks,
            is_log_plot_mticks_y=is_log_plot_mticks_y,
            yticks_font_size=yticks_font_size,
        )
    else:
        set_ax_yticks(
            ax=ax,
            space_y_ticks=space_y_ticks,
            anchor_y_ticks=anchor_y_ticks,
            strformatter_y=strformatter_y,
            is_plot_mticks_y=is_plot_mticks_y,
            num_y_mtick=num_y_mtick,
            yticks_font_size=yticks_font_size,
        )

    set_xlabel(
        ax=ax,
        xlabel_text=xlabel_text,
        xlabel_pos=xlabel_pos,
        ymin=ymin,
        xlabel_offset=xlabel_offset,
        xlabel_font_size=xlabel_font_size,
    )
    set_ylabel(
        ax=ax,
        ylabel_text=ylabel_text,
        ylabel_pos=ylabel_pos,
        xmin=xmin,
        ylabel_offset=ylabel_offset,
        ylabel_font_size=ylabel_font_size,
        is_horizontal_ylabel=is_horizontal_ylabel,
    )

    if is_plot_girdline:
        set_gridline(ax=ax, gridline_style=gridline_style)

    plotdata_dir_path = Path(__file__).parent / "plot_original_data"
    # ! ---↓基本設定２------------------------------------------------
    # *---データのプロット---

    # -↓データのプロット（これで1ブロック）-
    # プロットに使うファイル
    cur_plotdata_filename = "d-SPHC-VCS.dat"
    # データ読み込み
    data = np.loadtxt(
        plotdata_dir_path / cur_plotdata_filename,
        usecols=(
            0,
            1,
        ),  # プロットするデータがそれぞれ何列目か指定（0始まりで）
        # delimiter=",",  # 列方向のデータの区切り文字を指定
        # comments="//",  # 行頭などにあるコメント文の開始文字を指定
        # skiprows=4,  # 無視する先頭行の数
        # max_rows=9,  # データの先頭からいくつ列を読み込むか
    )
    # プロット（線）
    ax.plot(
        data[:, 0],
        data[:, 1],
        color="cyan",  # 線の色
        linewidth=2.5,  # 線の太さ
        linestyle="-",  # 線のスタイル（破線などはここで）
        label="Scheme-A",  # 凡例に使用するラベル
        zorder=2.3,  # 重ね順の調整．この値が大きいほど手前にプロットされる（開区間(2,3)内で設定）
        # 以下は基本いじらなくてOK
        gid=cur_plotdata_filename,
    )

    print(f"データプロット完了: {cur_plotdata_filename}")
    # -↑データのプロット（これで1ブロック）-

    # -↓データのプロット（これで1ブロック）-
    # プロットに使うファイル
    cur_plotdata_filename = "d-SPHC.dat"
    # データ読み込み
    data = np.loadtxt(
        plotdata_dir_path / cur_plotdata_filename,
        usecols=(
            0,
            1,
        ),  # プロットするデータがそれぞれ何列目か指定（0始まりで）
        # delimiter=",",  # 列方向のデータの区切り文字を指定
        # comments="//",  # 行頭などにあるコメント文の開始文字を指定
        # skiprows=4,  # 無視する先頭行の数
        # max_rows=9,  # データの先頭からいくつ列を読み込むか
    )
    # プロット（線）
    ax.plot(
        data[:, 0],
        data[:, 1],
        color="red",  # 線の色
        linewidth=1.4,  # 線の太さ
        linestyle="-",  # 線のスタイル（破線などはここで）
        label="Scheme-B",  # 凡例に使用するラベル
        zorder=2.3,  # 重ね順の調整．この値が大きいほど手前にプロットされる（開区間(2,3)内で設定）
        # 以下は基本いじらなくてOK
        gid=cur_plotdata_filename,
    )

    print(f"データプロット完了: {cur_plotdata_filename}")
    # -↑データのプロット（これで1ブロック）-

    # -↓データのプロット（これで1ブロック）-
    # プロットに使うファイル
    cur_plotdata_filename = "Theory.dat"
    # データ読み込み
    data = np.loadtxt(
        plotdata_dir_path / cur_plotdata_filename,
        usecols=(
            0,
            1,
        ),  # プロットするデータがそれぞれ何列目か指定（0始まりで）
        # delimiter=",",  # 列方向のデータの区切り文字を指定
        # comments="//",  # 行頭などにあるコメント文の開始文字を指定
        # skiprows=4,  # 無視する先頭行の数
        # max_rows=9,  # データの先頭からいくつ列を読み込むか
    )
    # プロット（線）
    ax.plot(
        data[:, 0],
        data[:, 1],
        color="gray",  # 線の色
        linewidth=1.0,  # 線の太さ
        linestyle="--",  # 線のスタイル（破線などはここで）
        label="Theoretical solution",  # 凡例に使用するラベル
        zorder=2.3,  # 重ね順の調整．この値が大きいほど手前にプロットされる（開区間(2,3)内で設定）
        # 以下は基本いじらなくてOK
        gid=cur_plotdata_filename,
    )

    print(f"データプロット完了: {cur_plotdata_filename}")
    # -↑データのプロット（これで1ブロック）-

    # *---データのプロット---

    # *---凡例の設定---
    is_plot_legend = True  # 凡例をプロットするか

    if is_plot_legend:
        legend = ax.legend(
            loc="lower left",  # legendboxのどの位置をbbox_to_anchorで固定するか（公式リファレンス参照）
            bbox_to_anchor=(
                0.0,
                1.03,
                0.7,
                1,
            ),  # それぞれ((locで固定するx), (~~するy), (legendboxの横幅), (これはあまり意味ない？))
            mode="expand",  # bbox_to_anchorの3,4個目の引数を指定するとき以外はコメントアウト
            ncol=2,  # 凡例をいくつ横並びで置くか
            # 以下は基本いじらなくてOK
            borderaxespad=0,
            prop={"size": legend_font_size},
        )

        standardize_legend_sizes(
            legend=legend,
            legend_lines_lw=2.5,  # 凡例のlineの太さを統一（しないときはNone）
            legend_scatters_size=None,  # 凡例のscatterの大きさを統一（しないときはNone）
        )

        # いじらなくてOK
        legend.set_zorder(1000000)
    # *---凡例の設定---
    # ! ---↑基本設定２------------------------------------------------

    output_dir_path = Path(__file__).parent / "plot_result"
    output_dir_path.mkdir(exist_ok=True)

    for extension in extension_list:
        fig.savefig(output_dir_path / f"{output_filename_withoutextention}.{extension}")
        print(f"画像保存完了: {extension}")

    plt.close()
    print("プロット終了")

    return


if __name__ == "__main__":
    main()
