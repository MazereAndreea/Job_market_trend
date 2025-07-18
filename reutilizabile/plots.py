from reutilizabile.common_imports import sns, plt, ListedColormap, color_list
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# categorical bars, optionally with hue
def plot_feature_frequency(data_df, feature, title=None, hue=None, horizontal=True, top_n=None):
    """
    Plot frequency counts of a categorical feature.

    Parameters:
    - data_df: pandas DataFrame
    - feature: str, column name to plot counts for
    - title: str, plot title (optional)
    - hue: str or None, column name for grouping (optional)
    - horizontal: bool, if True plot horizontal bars (good for many categories)
    - top_n: int or None, if set, plot only top_n most frequent categories
    """
    plt.figure(figsize=(12, 6))

    if top_n is not None:
        # Limit data to top_n categories
        top_categories = data_df[feature].value_counts().nlargest(top_n).index
        plot_data = data_df[data_df[feature].isin(top_categories)]
    else:
        plot_data = data_df

    order = plot_data[feature].value_counts().index

    if horizontal:
        sns.countplot(y=feature, data=plot_data, order=order, hue=hue)
        plt.xlabel('Count')
        plt.ylabel(feature.capitalize())
    else:
        sns.countplot(x=feature, data=plot_data, order=order, hue=hue)
        plt.ylabel('Count')
        plt.xlabel(feature.capitalize())

    if title:
        plt.title(title)
    else:
        plt.title(f'Frequency of {feature.capitalize()}')

    plt.tight_layout()
    fig.show()

# histogram with/ without hue
def plot_distribution_pairs(data_df, feature, title, hue="None"):
    color_list = ["#a6b5f2","#f9051b","#009e97","#111644"]
    f, ax = plt.subplots(1,1, figsize=(8,4))
    if hue is not None:
        unique_vals = data_df[hue].dropna().unique()
        for i, h in enumerate(unique_vals):
            sns.histplot(
                data_df.loc[data_df[hue] == h, feature],
                color=color_list[i],
                ax=ax,
                label=h,
                alpha=0.5  # for transparency to see overlap
            )
        ax.legend()
    else:
        sns.histplot(data_df[feature], ax=ax, color=color_list[0])
    ax.set_title(f"{title}")
    plt.show()

# top-N horizontal bar
def plot_bar_top_n(df, col, title, top_n=15):
    top = df[col].value_counts().nlargest(top_n)
    fig = px.bar(top, x=top.values, y=top.index, orientation='h', title=title)
    plt.show()

# scatter, box, line, bar plots
def plot_scatter(df, x, y, title, multiple_y, lim_inf, lim_sup):
    fig = px.scatter(df, x=x, y=y, title=title)
    fig.show()
    ax.yaxis.set_major_locator(MultipleLocator(5000))
    ax.set_ylim(290000, 420000)

def plot_box(df, x, y, title):
    fig = px.box(df, x=x, y=y, title=title)
    plt.show()

def plot_line_by_year(df, time_col, val_col, title):
    df_year = df.groupby(time_col)[val_col].mean().reset_index()
    fig = px.line(df_year, x=time_col, y=val_col, title=title)
    plt.show()

# average salary by category
def plot_avg_bar(df, category, target, title):
    avg_df = df.groupby(category)[target].mean().sort_values(ascending=False).head(15)
    fig = px.bar(avg_df, x=avg_df.values, y=avg_df.index, orientation='h', title=title)
    plt.show()

# heatmap of numeric columns
def plot_corr_heatmap(df):
    numeric_df = df.select_dtypes(include="number")
    corr = numeric_df.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    plt.show()

# set and preview color palette
def set_color_map(color_list):
    cmap_custom = ListedColormap(color_list)
    sns.palplot(sns.color_palette(color_list))
    plt.show()
    return cmap_custom
