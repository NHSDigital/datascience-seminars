import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
from matplotlib.axis import YAxis

import matplotlib.ticker as mtick
import matplotlib.transforms as transforms
from matplotlib.ticker import FormatStrFormatter

from config import nhs_palette

def create_marker_on_csv(pre_processing):
    """
    Adds a marker column with a specified value to all CSV files in a given directory and its subdirectories.

    The marker column is inserted as the first column in each CSV file, and the original files are overwritten.

    Args:
        pre_processing (dict): A dictionary containing:
            - 'file_path' (str): Path to the directory containing CSV files.
            - 'marker' (str): The name and value to use for the marker column.

    Returns:
        None
    """
    source_dir = pre_processing['file_path']

    csv_files = []
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(".csv"):
                csv_files.append(os.path.join(root, file))

    #Adding FAKE DATA in a new column
    for file in csv_files:
        df = pd.read_csv(file)
        df[pre_processing['marker']] = pre_processing['marker']
        #Place the FAKE DATA column at the start
        col = df.pop(pre_processing['marker']) 
        df.insert(0, pre_processing['marker'], col)
        #Overwrite the original file
        df.to_csv(file, index=False)

def single_year_table(table):
    """
    Transforms the input DataFrame to a pivot table showing 'ratio' values by 'age_band' and 'sex'.

    Parameters:
        table (pd.DataFrame): Input DataFrame containing at least the columns 'ratio', 'sex', and 'age_band'.

    Returns:
        pd.DataFrame: Pivot table with 'age_band' as index, 'sex' as columns, and 'ratio' as values.
    """

    table = table[['ratio','sex','age_band']]
    table = table[~table['ratio'].isnull()]

    table = pd.pivot_table(table, values='ratio', index=['age_band'], columns=['sex'] )

    return table

                            
def grouped_by_demographics(table, demo, cols_to_sum = ['numerator','denominator'], year_col = ['interval_start']):
    """
    Aggregates and summarizes a table by specified demographic and year columns.

    Parameters:
        table (pd.DataFrame): The input DataFrame containing the data to be grouped and summarized.
        demo (str): The name of the demographic column to group by (e.g., 'sex', 'age_group').
        cols_to_sum (list of str, optional): List of column names to sum within each group. 
            Defaults to ['numerator', 'denominator'].
        year_col (list of str, optional): List of column names representing the year or interval to group by.
            Defaults to ['interval_start'].

    Returns:
        pd.DataFrame: A DataFrame grouped by the specified demographic and year columns, 
            with summed values for the specified columns and an additional 'ratio' column 
            representing the percentage (numerator/denominator * 100) for each group.
    """

    #Need to sum over
    combine_cols = year_col + [demo]

    output = table.groupby(combine_cols, as_index = False)[cols_to_sum].sum()

    #Computing the ratio
    output['ratio'] = output[cols_to_sum[0]]/output[cols_to_sum[1]]

    #Covert into percentage
    output['ratio'] = output['ratio']*100

    return output


def grouped_by_overall(table, cols_to_sum = ['numerator','denominator'], year_col = ['interval_start']):
    """
    Groups a pandas DataFrame by specified columns, sums selected columns, and computes a percentage ratio.

    Args:
        table (pd.DataFrame): The input DataFrame containing the data to be grouped and summarized.
        cols_to_sum (list of str, optional): List of column names to sum. The first column is used as the numerator,
            and the second as the denominator for the ratio calculation. Defaults to ['numerator', 'denominator'].
        year_col (list of str, optional): List of column names to group by. Defaults to ['interval_start'].

    Returns:
        pd.DataFrame: A DataFrame grouped by `year_col`, with summed columns in `cols_to_sum` and an additional
            'ratio' column representing the percentage (numerator/denominator * 100).
    """
                            

    #Need to sum over
    combine_cols = year_col

    output = table.groupby(combine_cols, as_index = False)[cols_to_sum].sum()

    #Computing the ratio
    output['ratio'] = output[cols_to_sum[0]]/output[cols_to_sum[1]]

    #Covert into percentage
    output['ratio'] = output['ratio']*100

    return output

def float_to_2dp_by_default(number_float):
    """
    Format a floating-point number into a string with a sensible number of decimal places.

    This function returns a string representation of number_float using a default of one
    decimal place for most values, but it increases the number of decimal places for
    very small magnitudes to preserve significant digits.

    Behavior:
    - If the absolute magnitude is zero or the value is not finite (NaN or ±inf), the
        function returns a one-decimal-place formatted string using "{:.1f}".
    - For values whose order of magnitude is less than -2 (i.e., |x| < 1e-2), the
        function computes extra decimal places as dp = abs(floor(log10(|x|))) + 1 and
        formats the number using that many decimal places (f"{{:.{dp}f}}").
    - For all other finite nonzero values (|x| >= 1e-2), the function formats with
        one decimal place ("{:.1f}").

    Parameters
    ----------
    number_float : float
            The number to format. The function expects numpy to be available as it uses
            numpy functions (np.absolute and np.isfinite) internally.

    Returns
    -------
    str
            A string representation of number_float formatted according to the rules
            described above. The returned string preserves the sign of the input.

    Examples
    --------
    - float_to_2dp_by_default(123.456) -> "123.5"
    - float_to_2dp_by_default(0.01234) -> "0.01"
    - float_to_2dp_by_default(0.001234) -> "0.0012"  # more decimals for small numbers
    - float_to_2dp_by_default(0.0) -> "0.0"
    - float_to_2dp_by_default(float('nan')) -> "nan"  # formatted via "{:.1f}"

    Notes
    -----
    - The function aims to balance readability and precision: most numbers are shown
        with a single decimal place, while very small numbers are shown with extra
        decimals so their leading significant digits are visible.
    - Because formatting of NaN and infinities relies on Python's float formatting,
        those values will appear as "nan", "inf", or "-inf" when passed through the
        "{:.1f}" formatter.
    """

    #Find the order of mag
    mag_value = np.absolute(number_float)

    # Handle zero or non-finite values to avoid log10 errors
    if mag_value == 0 or not np.isfinite(mag_value):
        return "{:.1f}".format(number_float)

    #Need to detemine the decile of the vaule
    order_of_mag = np.floor(np.log10(mag_value))

    if order_of_mag < -2:
        dp = int(np.abs(order_of_mag)) + 1
        return f"{number_float:.{dp}f}"
    else:
        return "{:.1f}".format(number_float)

def determine_decimal_percentage_place_of_axis(axis, axis_method = None):
    """
    Determine and apply a sensible number of decimal places for an axis formatter.

    This function inspects the current y-limits of the provided axis object, determines
    the order of magnitude of the largest absolute y-limit, and then sets a
    matplotlib.ticker.FormatStrFormatter with an appropriate number of decimal places.

    Formatting rule:
    - If the order of magnitude is <= -2 (i.e. values smaller than 0.01), the number
        of decimal places is set to abs(order_of_magnitude) + 1. Example: a max value of
        0.001 (order_of_magnitude = -3) yields 4 decimal places ('%.4f').
    - Otherwise, the formatter is set to one decimal place ('%.1f').

    Parameters
    ----------
    axis : object
            An axis-like object with a get_ylim() method that returns (ymin, ymax)
            and (by default) a yaxis attribute with set_major_formatter method
            (i.e. a matplotlib.axes.Axes instance or similar).
    axis_method : callable, optional
            A callable used to apply the formatter. It must accept a matplotlib
            Formatter instance (for example, matplotlib.ticker.FormatStrFormatter).
            If None (default), axis.yaxis.set_major_formatter is used.

    Returns
    -------
    None
            The function has only side effects: it applies the chosen formatter to
            the axis via the provided axis_method.

    Notes and edge cases
    --------------------
    - The function relies on numpy (np.log10, np.floor, np.abs) and
        matplotlib.ticker.FormatStrFormatter being available in the caller's scope.
    - If both y-limits are zero (so the maximum absolute y-limit is 0), numpy.log10(0)
        yields -inf and converting that magnitude to an integer will raise an error.
        Therefore the axis y-limits must not be both zero.
    - axis_method must be callable; otherwise a TypeError will be raised when calling it.

    Example
    -------
    # Default behavior: set formatter for the y-axis of ax
    determine_decimal_percentage_place_of_axis(ax)

    # Provide a custom setter (e.g. set formatter for x-axis instead)
    determine_decimal_percentage_place_of_axis(ax, axis_method=ax.xaxis.set_major_formatter)
    """

    if axis_method is None:
        axis_method = axis.yaxis.set_major_formatter

    #Getting the y limits
    y_limits = axis.get_ylim()

    #Need to get largest vaules by absoulte vaule
    y_limits = np.absolute(y_limits)
    y_max_vaule = max(y_limits)

    #Need to detemine the decile of the vaule
    order_of_mag = np.floor(np.log10(y_max_vaule))

    #Need to set the dp
    if order_of_mag <= -2:
        #Set to an integer number of decimal places
        dp = int(np.abs(order_of_mag)) + 1
        axis_method(FormatStrFormatter(f'%.{dp}f'))
    else: 
        axis_method(FormatStrFormatter('%.1f')) 

def plot_adhd_prevalence_charts(sex_group, age_group_young, age_group_middle, age_group_old, nhs_palette = nhs_palette ):
    """
    Plots ADHD prevalence and count charts by sex and age bands.
    This function creates a 2x2 grid of subplots visualizing ADHD prevalence (as a percentage)
    and counts (as bar plots) over time, split by sex and three age groups (young, middle, old).
    Each subplot contains a line plot for prevalence and a bar plot for counts, with legends
    and axis labels appropriately set.
    Parameters
    ----------
    sex_group : pandas.DataFrame
        DataFrame containing ADHD prevalence and count data grouped by sex. Must include columns:
        'interval_start', 'ratio', 'numerator', 'sex'.
    age_group_young : pandas.DataFrame
        DataFrame containing ADHD prevalence and count data for young age bands. Must include columns:
        'interval_start', 'ratio', 'numerator', 'age_band'.
    age_group_middle : pandas.DataFrame
        DataFrame containing ADHD prevalence and count data for middle age bands. Must include columns:
        'interval_start', 'ratio', 'numerator', 'age_band'.
    age_group_old : pandas.DataFrame
        DataFrame containing ADHD prevalence and count data for old age bands. Must include columns:
        'interval_start', 'ratio', 'numerator', 'age_band'.
    nhs_palette : dict or list, optional
        Color palette to use for the plots. Should be compatible with seaborn's palette argument.
    Returns
    -------
    fig : matplotlib.figure.Figure
        The matplotlib Figure object containing the plots.
    axes : numpy.ndarray
        Array of matplotlib Axes objects for the subplots.
    Notes
    -----
    - Each subplot combines a line plot (prevalence) and a bar plot (counts) with a shared x-axis.
    - Legends are customized to display both prevalence and count information.
    - The function assumes the input DataFrames are properly formatted and indexed.
    """

    #Need to convert the tables
    sex_group = sort_and_formal_name(sex_group)
    age_group_young = sort_and_formal_name(age_group_young)
    age_group_middle = sort_and_formal_name(age_group_middle)
    age_group_old = sort_and_formal_name(age_group_old)

    fig, axes = plt.subplots(2, 2, figsize=(15.7, 15.3))  # A4 landscape in inches

    # By sex
    sns.lineplot(x="interval_start", y="ratio", hue="sex", data=sex_group, ax=axes[0, 0], palette=nhs_palette)
    axes[0, 0].set_ylabel("Prevalence, %")
    axes[0, 0].set_xlabel("Year")
    ax_tmp0 = axes[0, 0].twinx()
    sns.barplot(x="interval_start", y="numerator", hue="sex", ax=ax_tmp0, data=sex_group, palette=nhs_palette, alpha=0.3, dodge=True)
    ax_tmp0.set_ylabel("Count")
    axes[0, 0].set_title("ADHD Prevalence and Counts by Sex")
    axes[0, 0].set_xticklabels(axes[0, 0].get_xticklabels(), rotation=90)
    #axes[0, 0].get_legend().remove()
    handles1, labels1 = axes[0, 0].get_legend_handles_labels()
    handles2, labels2 = ax_tmp0.get_legend_handles_labels()
    axes[0, 0].legend((*handles1, *handles2), (*len(labels1)*[''], *labels2),
             loc='best', ncol=2, handlelength=3, edgecolor='black', handletextpad = 0.1,
             labelspacing = 0.1, columnspacing = 0.1,
             )
    ax_tmp0.get_legend().remove()
    #Setting up the axis
    determine_decimal_percentage_place_of_axis(axes[0, 0])

    # Young age bands
    sns.lineplot(x="interval_start", y="ratio", hue="age_band", data=age_group_young, ax=axes[0, 1], palette=nhs_palette)
    axes[0, 1].set_ylabel("Prevalence, %")
    axes[0, 1].set_xlabel("Year")
    ax_tmp1 = axes[0, 1].twinx()
    sns.barplot(x="interval_start", y="numerator", hue="age_band", ax=ax_tmp1, data=age_group_young, palette=nhs_palette, alpha=0.3, dodge=True)
    ax_tmp1.set_ylabel("Count")
    axes[0, 1].set_title("ADHD Prevalence and Counts by Age Band (Young)")
    axes[0, 1].set_xticklabels(axes[0, 1].get_xticklabels(), rotation=90)
    #axes[0, 0].get_legend().remove()
    handles1, labels1 = axes[0, 1].get_legend_handles_labels()
    handles2, labels2 = ax_tmp1.get_legend_handles_labels()
    axes[0, 1].legend((*handles1, *handles2), (*len(labels1)*[''], *labels2),
             loc='best', ncol=2, handlelength=3, edgecolor='black',handletextpad = 0.1,
             labelspacing = 0.1, columnspacing = 0.1
             )
    ax_tmp1.get_legend().remove()
    determine_decimal_percentage_place_of_axis(axes[0, 1])

    # Middle age bands
    sns.lineplot(x="interval_start", y="ratio", hue="age_band", data=age_group_middle, ax=axes[1, 0], palette=nhs_palette)
    axes[1, 0].set_ylabel("Prevalence, %")
    axes[1, 0].set_xlabel("Year")
    ax_tmp2 = axes[1, 0].twinx()
    sns.barplot(x="interval_start", y="numerator", hue="age_band", ax=ax_tmp2, data=age_group_middle, palette=nhs_palette, alpha=0.3, dodge=True)
    ax_tmp2.set_ylabel("Count")
    axes[1, 0].set_title("ADHD Prevalence and Counts by Age Band (Middle Age)")
    axes[1, 0].set_xticklabels(axes[1, 0].get_xticklabels(), rotation=90)

    handles1, labels1 = axes[1, 0].get_legend_handles_labels()
    handles2, labels2 = ax_tmp2.get_legend_handles_labels()
    axes[1, 0].legend((*handles1, *handles2), (*len(labels1)*[''], *labels2),
             loc='best', ncol=2, handlelength=3, edgecolor='black',handletextpad = 0.1,
             labelspacing = 0.1, columnspacing = 0.1
             )
    ax_tmp2.get_legend().remove()
    determine_decimal_percentage_place_of_axis(axes[1, 0])

    # Old age bands
    sns.lineplot(x="interval_start", y="ratio", hue="age_band", data=age_group_old, ax=axes[1, 1], palette=nhs_palette)
    axes[1, 1].set_ylabel("Prevalence, %")
    axes[1, 1].set_xlabel("Year")
    ax_tmp3 = axes[1, 1].twinx()
    sns.barplot(x="interval_start", y="numerator", hue="age_band", ax=ax_tmp3, data=age_group_old, palette=nhs_palette, alpha=0.3, dodge=True)
    ax_tmp3.set_ylabel("Count")
    axes[1, 1].set_title("ADHD Prevalence and Counts by Age Band (Retired)")
    axes[1, 1].set_xticklabels(axes[1, 1].get_xticklabels(), rotation=90)
    handles1, labels1 = axes[1, 1].get_legend_handles_labels()
    handles2, labels2 = ax_tmp3.get_legend_handles_labels()
    axes[1, 1].legend((*handles1, *handles2), (*len(labels1)*[''], *labels2),
             loc='best', ncol=2, handlelength=3, edgecolor='black',handletextpad = 0.1,
             labelspacing = 0.1, columnspacing = 0.1
             )
    ax_tmp3.get_legend().remove()
    determine_decimal_percentage_place_of_axis(axes[1, 1])

    plt.tight_layout()

    #plt.subplots_adjust(hspace=1.75)
    return fig, axes

def get_sex_and_age_groups(table):
    """
    Groups the input table by sex and age bands, and further splits age groups into young, middle, and old categories.

    Args:
        table (pd.DataFrame): The input DataFrame containing demographic data with 'sex' and 'age_band' columns.

    Returns:
        tuple: A tuple containing:
            - sex_group (pd.DataFrame): Data grouped by 'sex'.
            - age_group (pd.DataFrame): Data grouped by 'age_band'.
            - age_group_young (pd.DataFrame): Data for age bands '0 to 9', '10 to 17', '18 to 24'.
            - age_group_middle (pd.DataFrame): Data for age bands '25 to 34', '35 to 44', '45 to 54', '55 to 64'.
            - age_group_old (pd.DataFrame): Data for age bands '65 to 74', '75 and over'.
    """
    sex_group = grouped_by_demographics(table, 'sex')
    age_group = grouped_by_demographics(table, 'age_band')
    age_group_young = age_group[age_group['age_band'].isin(['0 to 9', '10 to 17', '18 to 24'])]
    age_group_middle = age_group[age_group['age_band'].isin(['25 to 34', '35 to 44', '45 to 54', '55 to 64'])]
    age_group_old = age_group[age_group['age_band'].isin(['65 to 74', '75 and over'])]
    return sex_group, age_group, age_group_young, age_group_middle, age_group_old


def watermark_plot(axes, watermark_string):
    """
    Adds a watermark text to one or multiple matplotlib axes.

    Parameters
    ----------
    axes : matplotlib.axes.Axes or array-like of Axes
        The axes object(s) to which the watermark will be added. Can be a single Axes instance or an array-like collection of Axes.
    watermark_string : str
        The text to use as the watermark.

    Returns
    -------
    matplotlib.axes.Axes or array-like of Axes
        The axes object(s) with the watermark added.

    Notes
    -----
    The watermark is placed at the center of each axes, with a gray color, partial transparency, and rotated by 30 degrees.
    """

    if hasattr(axes, "__len__"):
        for ax in axes.flat:
            ax.text(
                0.5, 0.5, watermark_string,
                transform=ax.transAxes,
                fontsize=50, color='gray', alpha=0.5,
                ha='center', va='center', rotation=30
            )
    else:
        axes.text(
                0.5, 0.5, watermark_string,
                transform=axes.transAxes,
                fontsize=50, color='gray', alpha=0.5,
                ha='center', va='center', rotation=30
            )
    return axes
    
def plot_time_from_diagnosis_to_medication(time_between_dia_and_med, nhs_palette,
                                           include_bar_chart = False):
    
    """
    Plot median time (in weeks) from diagnosis to medication by year, sex, and age band.

    This function creates a two-row matplotlib figure with separate subplots for male and female
    patients. For each sex it draws a seaborn lineplot of the median time between diagnosis and
    medication across years, with separate lines for each age band. Optionally, a semi-transparent
    bar chart showing patient counts (column "size") can be overlaid on a secondary y-axis.

    Important behavior:
    - Rows that contain the string 'ALL' in any column are removed prior to plotting.
    - A new column 'year' is created by converting the 'year_of_medication' column to string and
        extracting the first four characters (typically the YYYY year). Note: this assignment may
        trigger a pandas SettingWithCopyWarning or modify the provided DataFrame; pass a copy
        if you wish to avoid side effects.
    - The function expects categorical sex values 'male' and 'female' (case-sensitive) and will
        split the data accordingly.

    Parameters
    ----------
    time_between_dia_and_med : pandas.DataFrame
            DataFrame containing at minimum the following columns:
                - 'year_of_medication' : convertible to string; the first 4 characters are used as year.
                - 'sex' : values expected include 'male' and 'female'.
                - 'age_band' : categorical/grouping column used as the hue for plots.
                - 'median' : numeric median time (weeks) to be plotted on the primary y-axis.
                - 'size' : numeric count used for optional bar charts on the secondary y-axis.
            Any rows containing the exact string 'ALL' in any column are removed prior to plotting.

    nhs_palette : matplotlib-compatible color palette
            Palette passed to seaborn plotting functions. Can be a seaborn/matplotlib palette name,
            list of colors, or a dict mapping levels of 'age_band' to colors.

    include_bar_chart : bool, optional (default=False)
            If True, a bar plot of patient counts ('size') is drawn on a secondary y-axis for each
            sex subplot. Bars are drawn with alpha=0.3 and are dodged by 'age_band'.

    Returns
    -------
    matplotlib.figure.Figure
            The created matplotlib Figure object.

    numpy.ndarray
            An array-like of two Axes objects (shape (2,)), corresponding to the male (index 0)
            and female (index 1) subplots.

    Raises
    ------
    KeyError
            If any required columns ('year_of_medication', 'sex', 'age_band', 'median', 'size') are
            missing from the input DataFrame.

    Notes
    -----
    - The function uses seaborn.lineplot and seaborn.barplot with matplotlib.twinx to overlay
        counts on a secondary y-axis. Axis labels, titles and tight layout are applied automatically.
    - The function filters sex values using exact matches to 'male' and 'female'; data with other
        sex encodings will not appear in the plots unless pre-normalized.

    Example
    -------
    # Assuming `df` is a DataFrame with the required columns and `palette` is defined:
    fig, axes = plot_time_from_diagnosis_to_medication(df, nhs_palette=palette, include_bar_chart=True)
    """

    # Remove rows with 'ALL' in any column
    time_between_dia_and_med = time_between_dia_and_med[~time_between_dia_and_med.isin(['ALL']).any(axis=1)]
    # Convert year_of_medication to year string
    time_between_dia_and_med['year'] = time_between_dia_and_med['year_of_medication'].astype(str).str[:4]
    time_between_dia_and_med =  sort_and_formal_name(time_between_dia_and_med, col_name = "year")

    # Split by sex
    time_males_table = time_between_dia_and_med[time_between_dia_and_med['sex'].isin(['male'])]
    time_females_table = time_between_dia_and_med[time_between_dia_and_med['sex'].isin(['female'])]

    fig, axes = plt.subplots(2, 1, figsize=(12, 12))

    # Males plot
    sns.lineplot(
        x="year",
        y="median",
        hue="age_band",
        data=time_males_table,
        ax=axes[0],
        palette=nhs_palette,
    )
    axes[0].set_ylabel("Median Time Weeks")
    axes[0].set_xlabel("Year")
    axes[0].set_title("Male - Time between Diagnosis to Medication")

    if include_bar_chart:
        ax_tmp = axes[0].twinx()
        sns.barplot(
            x="year",
            y="size",
            hue="age_band",
            data=time_males_table,
            palette=nhs_palette,
            alpha=0.3,
            dodge=True,
            ax=ax_tmp
        )
        ax_tmp.set_ylabel("Count of Patients")

    # Females plot
    sns.lineplot(
        x="year",
        y="median",
        hue="age_band",
        data=time_females_table,
        ax=axes[1],
        palette=nhs_palette,
    )
    axes[1].set_ylabel("Median Time Weeks")
    axes[1].set_xlabel("Year")
    axes[1].set_title("Female - Time between Diagnosis to Medication")

    if include_bar_chart:
        ax_tmp = axes[1].twinx()
        sns.barplot(
            x="year",
            y="size",
            hue="age_band",
            data=time_females_table,
            palette=nhs_palette,
            alpha=0.3,
            dodge=True,
            ax=ax_tmp
        )
        ax_tmp.set_ylabel("Count of Patients")

    plt.tight_layout()
    return fig, axes

def plot_monthly_interval_charts(table3_percentage, nhs_palette):
    """
    Plots monthly interval charts showing the percentage and count of patients with ADHD who had an ADHD medication in the previous 6 months, grouped by sex and age band.

    Parameters
    ----------
    table3_percentage : pd.DataFrame
        DataFrame containing the interval data with columns for sex, age_band, interval_start, ratio (percentage), and numerator (count).
    nhs_palette : dict or list
        Color palette to use for the line plots, compatible with seaborn.

    Returns
    -------
    fig : matplotlib.figure.Figure
        The matplotlib figure object containing the plots.
    axes : np.ndarray of matplotlib.axes.Axes
        Array of axes objects for the subplots.

    Notes
    -----
    - The function creates a 2x2 grid of line plots:
        (0, 0): Percentage by sex
        (0, 1): Count by sex
        (1, 0): Percentage by age band
        (1, 1): Count by age band
    - The x-axis represents the interval start date (converted to datetime).
    - Titles and axis labels are set for clarity.
    """
    sex_group, age_group, _, _, _ = get_sex_and_age_groups(table3_percentage)

    # Preprocessing
    sex_group["interval_start"] = pd.to_datetime(sex_group["interval_start"])
    age_group["interval_start"] = pd.to_datetime(age_group["interval_start"])

    fig, axes = plt.subplots(2, 2, figsize=(11.7, 8.3))  # A4 landscape in inches

    # By sex - percentage
    sns.lineplot(x="interval_start", y="ratio", hue="sex", data=sex_group, ax=axes[0, 0], palette=nhs_palette)
    axes[0, 0].set_ylabel("Percentage")
    axes[0, 0].set_xlabel("Year")
    axes[0, 0].set_title("Percentage of Patients with ADHD that had\nan ADHD medication in the previous 6 months")
    determine_decimal_percentage_place_of_axis(axes[0, 0])

    # By sex - count
    sns.lineplot(x="interval_start", y="numerator", hue="sex", data=sex_group, ax=axes[0, 1], palette=nhs_palette)
    axes[0, 1].set_ylabel("Count")
    axes[0, 1].set_xlabel("Year")
    axes[0, 1].set_title("Counts of Patients with ADHD that had\nan ADHD medication in the previous 6 months")

    # By age band - percentage
    sns.lineplot(x="interval_start", y="ratio", hue="age_band", data=age_group, ax=axes[1, 0], palette=nhs_palette)
    axes[1, 0].set_ylabel("Percentage")
    axes[1, 0].set_xlabel("Year")
    axes[1, 0].set_title("Percentage of Patients with ADHD that had\nan ADHD medication in the previous 6 months")
    determine_decimal_percentage_place_of_axis(axes[1, 0])

    # By age band - count
    sns.lineplot(x="interval_start", y="numerator", hue="age_band", data=age_group, ax=axes[1, 1], palette=nhs_palette)
    axes[1, 1].set_ylabel("Count")
    axes[1, 1].set_xlabel("Year")
    axes[1, 1].set_title("Counts of Patients with ADHD that had\nan ADHD medication in the previous 6 months")

    plt.subplots_adjust(hspace=0.4)
    return fig, axes

def _import_mpl():
    """This function is not needed outside this utils module."""
    try:
        import matplotlib.pyplot as plt
    except:
        raise ImportError("Matplotlib is not found.")

    return plt

def change_to_correct_form(date_col):
    """
    Convert a column/Series of date-like values into a "YYYY/YY" year-range string.

    This function expects a pandas Series (or array-like) where each entry, when
    cast to str, begins with a four-digit year (characters 0:4). It extracts that
    four-digit year, computes the next year, and returns a Series of strings in
    the form "YYYY/YY" where "YY" are the last two digits of the following year
    (e.g. "2023/24").

    Parameters
    ----------
    date_col : pandas.Series or array-like
        Series or array-like of date-like values (e.g., datetime64, "YYYY-MM-DD",
        "YYYY", or similar). Values are converted to str and the first four
        characters are interpreted as the year.

    Returns
    -------
    pandas.Series
        Series of strings formatted as "YYYY/YY" (object dtype). For example,
        an input year of 2023 becomes "2023/24".

    Raises
    ------
    ValueError, TypeError
        If an entry cannot be converted to a string with a valid four-digit year
        at positions 0:4, casting to int will raise an error (e.g., for NaN,
        very short strings, or non-date-like values).

    Notes
    -----
    - Leading/trailing whitespace or unexpected formats may produce incorrect
      results or raise exceptions because the function unconditionally slices the
      first four characters and converts them to int.
    - NaN values in the input will generally cause an error when casting to int.
      Pre-clean the input if you need to preserve or handle missing values.
    - The function does not localize or interpret fiscal calendars beyond the
      simple next-year string formatting.

    Examples
    --------
    >>> import pandas as pd
    >>> change_to_correct_form(pd.Series(["2023-01-01", "2020-12-31"]))
    0    2023/24
    1    2020/21
    dtype: object
    """

    table_current_year = date_col.astype(str).str[0:4].astype(int)

    table_next_year = table_current_year + 1

    final_form = table_current_year.astype(str) + '/' + table_next_year.astype(str).str[-2:]

    return final_form

    
def sort_and_formal_name(table, col_name = "interval_start"):
    """
    Transform and standardize the values of a DataFrame column using a helper function.

    This function applies the helper function `change_to_correct_form` to the specified
    column of a pandas DataFrame, assigns the transformed values back to that column,
    and returns the DataFrame. The operation updates the provided DataFrame in place.

    Parameters
    ----------
    table : pandas.DataFrame
        DataFrame containing the column to transform.
    col_name : str, optional
        Name of the column to be transformed. Default is "interval_start".

    Returns
    -------
    pandas.DataFrame
        The same DataFrame instance with `col_name` replaced by the transformed values.

    Notes
    -----
    - `change_to_correct_form` must be defined in the calling module and should accept
      a pandas Series (or array-like) and return a Series or array-like of compatible length.
    - Because the assignment `table[col_name] = ...` modifies the DataFrame in place,
      pass a copy (e.g., `table.copy()`) if you need to preserve the original.
    - If `col_name` is not present in `table`, a KeyError will be raised.
    - Errors raised by `change_to_correct_form` (e.g., TypeError, ValueError) will propagate.

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({"interval_start": ["2020-01-01", "2020-02-01"]})
    >>> # Assuming change_to_correct_form converts strings to pandas.Timestamp
    >>> sort_and_formal_name(df)
    # df["interval_start"] is now transformed by change_to_correct_form
    """

    #Need to rename
    table[col_name] = change_to_correct_form(table[col_name])

    return table

def create_mpl_ax(ax=None):
    """Helper function for when a single plot axis is needed.

    Parameters
    ----------
    ax : AxesSubplot, optional
        If given, this subplot is used to plot in instead of a new figure being
        created.

    Returns
    -------
    fig : Figure
        If `ax` is None, the created figure.  Otherwise the figure to which
        `ax` is connected.
    ax : AxesSubplot
        The created axis if `ax` is None, otherwise the axis that was passed
        in.

    Notes
    -----
    This function imports `matplotlib.pyplot`, which should only be done to
    create (a) figure(s) with ``plt.figure``.  All other functionality exposed
    by the pyplot module can and should be imported directly from its
    Matplotlib module.

    See Also
    --------
    create_mpl_fig

    Examples
    --------
    A plotting function has a keyword ``ax=None``.  Then calls:

    >>> from statsmodels.graphics import utils
    >>> fig, ax = utils.create_mpl_ax(ax)
    """
    if ax is None:
        plt = _import_mpl()
        fig = plt.figure()
        ax = fig.add_subplot(111)
    else:
        fig = ax.figure

    return fig, ax

def mean_diff_plot(m1, m2, sd_limit=1.96, ax=None, scatter_kwds=None,
                   mean_line_kwds=None, limit_lines_kwds=None):
    """
    Construct a Tukey/Bland-Altman Mean Difference Plot.

    Tukey's Mean Difference Plot (also known as a Bland-Altman plot) is a
    graphical method to analyze the differences between two methods of
    measurement. The mean of the measures is plotted against their difference.

    For more information see
    https://en.wikipedia.org/wiki/Bland-Altman_plot

    Parameters
    ----------
    m1 : array_like
        A 1-d array.
    m2 : array_like
        A 1-d array.
    sd_limit : float
        The limit of agreements expressed in terms of the standard deviation of
        the differences. If `md` is the mean of the differences, and `sd` is
        the standard deviation of those differences, then the limits of
        agreement that will be plotted are md +/- sd_limit * sd.
        The default of 1.96 will produce 95% confidence intervals for the means
        of the differences. If sd_limit = 0, no limits will be plotted, and
        the ylimit of the plot defaults to 3 standard deviations on either
        side of the mean.
    ax : AxesSubplot
        If `ax` is None, then a figure is created. If an axis instance is
        given, the mean difference plot is drawn on the axis.
    scatter_kwds : dict
        Options to to style the scatter plot. Accepts any keywords for the
        matplotlib Axes.scatter plotting method
    mean_line_kwds : dict
        Options to to style the scatter plot. Accepts any keywords for the
        matplotlib Axes.axhline plotting method
    limit_lines_kwds : dict
        Options to to style the scatter plot. Accepts any keywords for the
        matplotlib Axes.axhline plotting method

    Returns
    -------
    Figure
        If `ax` is None, the created figure.  Otherwise the figure to which
        `ax` is connected.

    References
    ----------
    Bland JM, Altman DG (1986). "Statistical methods for assessing agreement
    between two methods of clinical measurement"

    Examples
    --------

    Load relevant libraries.

    >>> import statsmodels.api as sm
    >>> import numpy as np
    >>> import matplotlib.pyplot as plt

    Making a mean difference plot.

    >>> # Seed the random number generator.
    >>> # This ensures that the results below are reproducible.
    >>> np.random.seed(9999)
    >>> m1 = np.random.random(20)
    >>> m2 = np.random.random(20)
    >>> f, ax = plt.subplots(1, figsize = (8,5))
    >>> sm.graphics.mean_diff_plot(m1, m2, ax = ax)
    >>> plt.show()

    .. plot:: plots/graphics-mean_diff_plot.py
    """
    fig, ax = create_mpl_ax(ax)

    if len(m1) != len(m2):
        raise ValueError('m1 does not have the same length as m2.')
    if sd_limit < 0:
        raise ValueError(f'sd_limit ({sd_limit}) is less than 0.')

    means = np.mean([m1, m2], axis=0)
    diffs = m1 - m2
    mean_diff = np.mean(diffs)
    std_diff = np.std(diffs, axis=0)

    scatter_kwds = scatter_kwds or {}
    if 's' not in scatter_kwds:
        scatter_kwds['s'] = 20
    mean_line_kwds = mean_line_kwds or {}
    limit_lines_kwds = limit_lines_kwds or {}
    for kwds in [mean_line_kwds, limit_lines_kwds]:
        if 'color' not in kwds:
            kwds['color'] = 'gray'
        if 'linewidth' not in kwds:
            kwds['linewidth'] = 1
    if 'linestyle' not in mean_line_kwds:
        kwds['linestyle'] = '--'
    if 'linestyle' not in limit_lines_kwds:
        kwds['linestyle'] = ':'

    ax.scatter(means, diffs, **scatter_kwds) # Plot the means against the diffs.
    ax.axhline(mean_diff, **mean_line_kwds)  # draw mean line.

    # Annotate mean line with mean difference.
    ax.annotate(f'mean diff:\n{float_to_2dp_by_default(mean_diff)}',
                xy=(0.99, 0.5),
                horizontalalignment='right',
                verticalalignment='center',
                fontsize=14,
                xycoords='axes fraction')

    if sd_limit > 0:
        half_ylim = (1.5 * sd_limit) * std_diff
        ax.set_ylim(mean_diff - half_ylim,
                    mean_diff + half_ylim)
        limit_of_agreement = sd_limit * std_diff
        lower = mean_diff - limit_of_agreement
        upper = mean_diff + limit_of_agreement
        for j, lim in enumerate([lower, upper]):
            ax.axhline(lim, **limit_lines_kwds)
        ax.annotate(f'-{sd_limit} SD: {float_to_2dp_by_default(lower)}',
                    xy=(0.99, 0.07),
                    horizontalalignment='right',
                    verticalalignment='bottom',
                    fontsize=14,
                    xycoords='axes fraction')
        ax.annotate(f'+{sd_limit} SD: {float_to_2dp_by_default(upper)}',
                    xy=(0.99, 0.92),
                    horizontalalignment='right',
                    fontsize=14,
                    xycoords='axes fraction')

    elif sd_limit == 0:
        half_ylim = 3 * std_diff
        ax.set_ylim(mean_diff - half_ylim,
                    mean_diff + half_ylim)

    ax.set_ylabel('Difference', fontsize=15)
    ax.set_xlabel('Means', fontsize=15)
    ax.tick_params(labelsize=13)
    fig.tight_layout()
    return fig

def plot_bland_altman(table_2_tpp, table_2_emis, bland_altman_plt, custom_scaling = False):
    """
    Generates a Bland–Altman plot to compare ADHD diagnosis prevalence between TPP and EMIS+Cegedim datasets.

    Parameters
    ----------
    table_2_tpp : pandas.DataFrame
        DataFrame containing prevalence ratios from the TPP dataset.
    table_2_emis : pandas.DataFrame
        DataFrame containing prevalence ratios from the EMIS+Cegedim dataset.
    bland_altman_plt : dict
        Dictionary containing plot configuration, including:
            - 'joining_cols': list of column names to join on.
            - 'suffixes': tuple of suffixes to apply to overlapping columns.
    custom_scaling : bool, optional
        If True, scales the y-axis limits by 1.4 for custom visualization. Default is False.

    Returns
    -------
    f : matplotlib.figure.Figure
        The matplotlib Figure object containing the plot.
    ax : matplotlib.axes.Axes
        The matplotlib Axes object containing the plot.

    Notes
    -----
    - The function merges the two input DataFrames on specified columns, drops rows with missing values,
      and plots the Bland–Altman plot using the 'ratio_tpp' and 'ratio_emis' columns.
    - The plot visualizes the mean and difference in prevalence ratios between the two datasets.
    """


    joined_data = table_2_tpp.merge(
        table_2_emis,
        how='left',
        on=bland_altman_plt['joining_cols'],
        suffixes=bland_altman_plt['suffixes']
    )
    # Clean the join
    joined_data = joined_data.dropna()

    f, ax = plt.subplots(1, figsize=(8, 5))
    mean_diff_plot(
        joined_data['ratio_tpp'] * 100,
        joined_data['ratio_emis'] * 100,
        ax=ax
    )

    ax.set_title(
        "Bland–Altman plot between ADHD Diagnosis\nPrevalence between TPP and EMIS+Cegedim",
        fontsize=18
    )
    ax.set_ylabel("Prevalence from TPP minus\nPrevalence from EMIS+Cegedim, %")
    determine_decimal_percentage_place_of_axis(ax)
    ax.set_xlabel("Mean Prevalence TPP and EMIS+Cegedim, %")
    determine_decimal_percentage_place_of_axis(ax, axis_method = ax.xaxis.set_major_formatter)

    if custom_scaling:
        y_lower, y_upper = ax.get_ylim()
        ax.set_ylim([y_lower * 1.4, y_upper * 1.4])

    plt.tight_layout()
    return f, ax

def single_cut_of_data(table, 
                       filter_dict = {
                           'sex':'ALL', 
                           'age_band':'10 to 17'
                           },
                        nhs_palette = nhs_palette
                       ):
    
    """
    Filters the input DataFrame based on the specified criteria and generates a combined line and bar plot.
    Parameters
    ----------
    table : pandas.DataFrame
        The input data containing at least the columns 'sex', 'age_band', 'year_of_medication', 'median', and 'size'.
    filter_dict : dict, optional
        Dictionary specifying column-value pairs to filter the data. Default is {'sex': 'ALL', 'age_band': '10 to 17'}.
    nhs_palette : dict or list
        Color palette to use for the plots, passed to seaborn plotting functions.
    Returns
    -------
    fig : matplotlib.figure.Figure
        The matplotlib Figure object containing the plot.
    axes : matplotlib.axes.Axes
        The primary matplotlib Axes object for the line plot.
    Notes
    -----
    - The function filters the DataFrame according to `filter_dict`.
    - The 'year_of_medication' column is converted to a string and truncated to the first 4 characters to create a 'year' column.
    - A line plot of 'median' by 'year' is created, colored by 'age_band'.
    - A secondary y-axis bar plot of 'size' by 'year' is overlaid, also colored by 'age_band'.
    """
    
    #Do some filter
    for each_column in filter_dict:
        table = table[
            table[each_column] == filter_dict[each_column]
            ]
        
    #Need to covert the cols
    table['year'] = table['year_of_medication'].astype(str).str[:4]

    fig, axes = plt.subplots(1, figsize = (5,5))  # Changed to 2 rows, 1 column

    sns.lineplot(
        x="year",
        y="median",
        hue="age_band",
        data=table,
        ax=axes,
        palette=nhs_palette,
    )
    axes.set_ylabel("Median Time Weeks")
    axes.set_xlabel("Year")
    axes.set_title("Male - Time between Diagnosis to Medication")

    ax_tmp = axes.twinx()
    sns.barplot(
        x="year", 
        y="size", 
        hue="age_band", 
        data=table, 
        palette=nhs_palette, 
        alpha=0.3, 
        dodge=True,
        ax=ax_tmp
    )

    ax_tmp.set_ylabel("Count of Patients")

    plt.tight_layout()

    return fig, axes