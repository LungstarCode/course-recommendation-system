# app/visualization_utils.py

import os
import matplotlib
matplotlib.use("Agg")  # Non-interactive backend for servers / Flask
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud
import pandas as pd
import seaborn as sns

VISUAL_PATH = os.path.join(os.getcwd(), "app", "static", "visuals")
os.makedirs(VISUAL_PATH, exist_ok=True)

def plot_category_counts(df):
    """Visualize distribution of categories."""
    plt.figure(figsize=(8,4))
    df['category'].value_counts().plot(kind='bar', color='skyblue')
    plt.title("Courses per Category")
    plt.xlabel("Category")
    plt.ylabel("Count")
    path = os.path.join(VISUAL_PATH, "category_counts.png")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return "visuals/category_counts.png"


def plot_tag_wordcloud(df):
    """Create a word cloud for tags."""
    tags = df['tags'].dropna().str.split(',').sum()
    tags = [t.strip() for t in tags if t.strip()]
    tag_counts = Counter(tags)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(tag_counts)
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    path = os.path.join(VISUAL_PATH, "tag_wordcloud.png")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return "visuals/tag_wordcloud.png"


def plot_description_wordcloud(df):
    """Create a word cloud for description text."""
    text = " ".join(df['description'].dropna().tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=set(['the','and','to','in','of','for'])).generate(text)
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    path = os.path.join(VISUAL_PATH, "description_wordcloud.png")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return "visuals/description_wordcloud.png"


def plot_user_category_heatmap(df):
    """Show how many courses each user took in each category."""
    user_category = df.groupby(['user_id', 'category']).size().unstack(fill_value=0)
    plt.figure(figsize=(10,6))
    sns.heatmap(user_category, cmap="YlGnBu")
    plt.title("User Preference by Category")
    path = os.path.join(VISUAL_PATH, "user_category_heatmap.png")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return "visuals/user_category_heatmap.png"

def plot_category_counts(df):
    """Visualize distribution of categories."""
    plt.figure(figsize=(8,4))
    df['category'].value_counts().plot(kind='bar', color='skyblue')
    plt.title("Courses per Category")
    plt.xlabel("Category")
    plt.ylabel("Count")
    path = os.path.join(VISUAL_PATH, "category_counts.png")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return "visuals/category_counts.png"


def plot_tag_frequencies(df, top_n=15):
    """Visualize most common tags."""
    tags = df['tags'].dropna().str.split(',').sum()
    tags = [t.strip() for t in tags if t.strip()]
    tag_counts = pd.Series(tags).value_counts().head(top_n)
    plt.figure(figsize=(8,4))
    sns.barplot(x=tag_counts.values, y=tag_counts.index, palette="Blues_r")
    plt.title(f"Top {top_n} Tags")
    plt.xlabel("Frequency")
    plt.ylabel("Tag")
    path = os.path.join(VISUAL_PATH, "top_tags.png")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return "visuals/top_tags.png"


def plot_user_activity(df, top_n=15):
    """Show most active users."""
    user_counts = df['user_id'].value_counts().head(top_n)
    plt.figure(figsize=(8,4))
    sns.barplot(x=user_counts.values, y=user_counts.index, palette="coolwarm")
    plt.title(f"Top {top_n} Active Users")
    plt.xlabel("Courses Taken")
    plt.ylabel("User ID")
    path = os.path.join(VISUAL_PATH, "user_activity.png")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return "visuals/user_activity.png"


def plot_course_popularity(df, top_n=15):
    """Show most frequent courses."""
    course_counts = df['course_id'].value_counts().head(top_n)
    plt.figure(figsize=(8,4))
    sns.barplot(x=course_counts.values, y=course_counts.index, palette="viridis")
    plt.title(f"Top {top_n} Most Offered Courses")
    plt.xlabel("Occurrences")
    plt.ylabel("Course ID")
    path = os.path.join(VISUAL_PATH, "course_popularity.png")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return "visuals/course_popularity.png"


def plot_description_wordcloud(df):
    """Create a word cloud for description text."""
    text = " ".join(df['description'].dropna().tolist())
    wordcloud = WordCloud(width=800, height=400, background_color='white',
                          stopwords=set(['the','and','to','in','of','for','on','a','is'])).generate(text)
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    path = os.path.join(VISUAL_PATH, "description_wordcloud.png")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return "visuals/description_wordcloud.png"


# --- MULTIVARIATE / CROSS VISUALS ---

def plot_user_category_heatmap(df):
    """Show how many courses each user took in each category."""
    user_category = df.groupby(['user_id', 'category']).size().unstack(fill_value=0)
    plt.figure(figsize=(10,6))
    sns.heatmap(user_category, cmap="YlGnBu")
    plt.title("User Preference by Category")
    path = os.path.join(VISUAL_PATH, "user_category_heatmap.png")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return "visuals/user_category_heatmap.png"


def plot_tag_wordcloud(df):
    """Create a word cloud for tags."""
    tags = df['tags'].dropna().str.split(',').sum()
    tags = [t.strip() for t in tags if t.strip()]
    tag_counts = Counter(tags)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(tag_counts)
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    path = os.path.join(VISUAL_PATH, "tag_wordcloud.png")
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return "visuals/tag_wordcloud.png"

def get_description_word_counts(df, top_n=20):
    """Return top word frequencies in description as an HTML table."""
    from collections import Counter
    text = " ".join(df['description'].dropna().tolist()).lower().split()
    counts = Counter(text)
    df_counts = pd.DataFrame(counts.most_common(top_n), columns=["Word", "Frequency"])
    return df_counts.to_html(classes="table table-striped", index=False)

def get_tag_counts(df, top_n=20):
    """Return tag counts as an HTML table."""
    tags = df['tags'].dropna().str.split(',').sum()
    tags = [t.strip() for t in tags if t.strip()]
    tag_counts = pd.Series(tags).value_counts().head(top_n)
    df_tags = pd.DataFrame({"Tag": tag_counts.index, "Frequency": tag_counts.values})
    return df_tags.to_html(classes="table table-striped", index=False)
