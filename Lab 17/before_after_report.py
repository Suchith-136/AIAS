import pandas as pd
from pathlib import Path


def summarize_dataframe(df: pd.DataFrame) -> dict:
    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    object_cols = df.select_dtypes(include=["object"]).columns.tolist()

    summary = {
        "rows": int(df.shape[0]),
        "cols": int(df.shape[1]),
        "nulls_total": int(df.isna().sum().sum()),
        "numeric_cols_count": len(numeric_cols),
        "object_cols_count": len(object_cols),
    }

    # Basic stats for numeric columns (keep concise)
    if numeric_cols:
        desc = df[numeric_cols].describe().transpose()[["mean", "std", "min", "max"]]
        desc = desc.round(3)
        summary["numeric_stats"] = desc
    else:
        summary["numeric_stats"] = pd.DataFrame()

    return summary


def compare_dataframes(df_before: pd.DataFrame, df_after: pd.DataFrame) -> dict:
    summary_before = summarize_dataframe(df_before)
    summary_after = summarize_dataframe(df_after)

    stats_before = summary_before["numeric_stats"]
    stats_after = summary_after["numeric_stats"]

    common_numeric = []
    if not stats_before.empty and not stats_after.empty:
        common_numeric = list(set(stats_before.index).intersection(set(stats_after.index)))

    stats_change = pd.DataFrame()
    if common_numeric:
        stats_change = pd.DataFrame(index=sorted(common_numeric))
        for col in ["mean", "std", "min", "max"]:
            stats_change[f"{col}_before"] = stats_before.loc[stats_change.index, col]
            stats_change[f"{col}_after"] = stats_after.loc[stats_change.index, col]
            stats_change[f"{col}_delta"] = (
                stats_after.loc[stats_change.index, col] - stats_before.loc[stats_change.index, col]
            ).round(3)

    return {
        "before": summary_before,
        "after": summary_after,
        "numeric_stats_change": stats_change,
    }


def _markdown_table_from_df(df: pd.DataFrame, include_index: bool = True, max_rows: int = 10) -> str:
    if df is None or df.empty:
        return ""
    data = df.head(max_rows)
    if include_index:
        data = data.copy()
        data.reset_index(inplace=True)
        data.rename(columns={"index": "column"}, inplace=True)
    # Convert to strings
    data = data.fillna("")
    headers = list(data.columns)
    lines = ["| " + " | ".join(str(h) for h in headers) + " |"]
    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for _, row in data.iterrows():
        cells = [str(row[h]) for h in headers]
        lines.append("| " + " | ".join(cells) + " |")
    return "\n".join(lines)


def render_section_md(title: str, comparison: dict) -> str:
    b = comparison["before"]
    a = comparison["after"]
    lines = [f"### {title}"]
    lines.append("")
    lines.append("- **rows (before → after)**: " + f"{b['rows']} → {a['rows']}")
    lines.append("- **cols (before → after)**: " + f"{b['cols']} → {a['cols']}")
    lines.append("- **nulls_total (before → after)**: " + f"{b['nulls_total']} → {a['nulls_total']}")
    lines.append("- **numeric cols (before → after)**: " + f"{b['numeric_cols_count']} → {a['numeric_cols_count']}")
    lines.append("- **object cols (before → after)**: " + f"{b['object_cols_count']} → {a['object_cols_count']}")

    change = comparison["numeric_stats_change"]
    if change is not None and not change.empty:
        lines.append("")
        lines.append("Numeric column stats (before/after/delta):")
        lines.append("")
        lines.append(_markdown_table_from_df(change, include_index=True, max_rows=10))

    lines.append("")
    return "\n".join(lines)


def main():
    pairs = [
        ("social_media.csv", "social_media_cleaned.csv", "Social Media"),
        ("movie_reviews-1.csv", "movie_reviews-1_cleaned.csv", "Movie Reviews"),
        ("financial_data.csv", "financial_data_cleaned.csv", "Financial Data"),
        ("iot_sensor.csv", "iot_sensor_filled.csv", "IoT Sensor"),
    ]

    root = Path(__file__).parent
    report_lines = ["## Before vs After Summary Report", ""]

    for before_name, after_name, title in pairs:
        before_path = root / before_name
        after_path = root / after_name

        if not before_path.exists() or not after_path.exists():
            report_lines.append(f"### {title}")
            report_lines.append("")
            report_lines.append(
                f"- **Status**: Skipped (missing file: {'before' if not before_path.exists() else 'after'})"
            )
            report_lines.append("")
            continue

        try:
            df_before = pd.read_csv(before_path)
            df_after = pd.read_csv(after_path)
            comparison = compare_dataframes(df_before, df_after)
            report_lines.append(render_section_md(title, comparison))
        except Exception as exc:
            report_lines.append(f"### {title}")
            report_lines.append("")
            report_lines.append(f"- **Status**: Error while processing: {exc}")
            report_lines.append("")

    report_path = root / "before_after_report.md"
    report_path.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"Report written to {report_path}")


if __name__ == "__main__":
    main()
