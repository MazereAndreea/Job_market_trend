from reutilizabile.common_imports import sns, plt, ListedColormap, color_list

def plot_count_pairs(data_df, feature, title, hue="set"):
    f, ax = plt.subplots(1, 1, figsize=(8,4))
    sns.countplot(x = feature, data = data_df, hue=hue, palette = color_list)
    plt.grid(color="black",linestyle="-.", linewidth=0.5, axis="y", which="major")
    ax.set_title(f"{title}")
    plt.show()


import matplotlib.pyplot as plt
import seaborn as sns


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
    plt.show()


def plot_distribution_pairs(data_df, feature, title, hue="set"):
    f, ax = plt.subplots(1,1, figsize=(8,4))
    for i, h in enumerate(data_df[hue].unique()):
        g = sns.histplot(data_df.loc[data_df[hue]==h, feature], color = color_list[i], ax=ax, label=h)
    ax.set_title(f"{title}")
    g.legend()
    plt.show()

def set_color_map(color_list):
    cmap_custom = ListedColormap(color_list)
    sns.palplot(sns.color_palette(color_list))
    plt.show()
    return cmap_custom