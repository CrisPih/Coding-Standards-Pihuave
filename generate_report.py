
# Reviewed under SE2 coding standards guidelines

import json
from collections import Counter
from html import escape
from pathlib import Path

# input_file = Path("pylint_initial.json")
# output_file = Path("pylint_initial.html")

input_file = Path("pylint_final.json")
output_file = Path("pylint_final.html")

with input_file.open(encoding="utf-16") as file:
    issues = json.load(file)

counts = Counter(issue["type"] for issue in issues)

rows = ""
for issue in issues:
    rows += (
        "<tr>"
        f"<td>{escape(issue['type'])}</td>"
        f"<td>{escape(issue['symbol'])}</td>"
        f"<td>{issue['line']}</td>"
        f"<td>{escape(issue['message'])}</td>"
        "</tr>"
    )

summary = " | ".join(
    f"{escape(category)}: {count}"
    for category, count in sorted(counts.items())
)

html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Pylint Initial Report</title>
<style>
body {{
    font-family: Arial, sans-serif;
    margin: 40px;
    background: #f4f6f8;
}}
h1 {{ color: #243b53; }}
table {{
    width: 100%;
    border-collapse: collapse;
    background: white;
}}
th, td {{
    padding: 12px;
    border: 1px solid #ddd;
    text-align: left;
}}
th {{
    background: #243b53;
    color: white;
}}
tr:nth-child(even) {{ background: #eef2f6; }}
.summary {{ margin: 20px 0; }}
</style>
</head>
<body>
<h1>Pylint - Initial Code Analysis</h1>
<p><strong>File:</strong> test.py</p>
<p><strong>Tool:</strong> Pylint 4.1.2</p>
<p><strong>Initial score:</strong> 0.91 / 10</p>
<div class="summary">
<strong>Total findings:</strong> {len(issues)}
<p>{summary}</p>
</div>
<table>
<thead>
<tr>
<th>Type</th>
<th>Rule</th>
<th>Line</th>
<th>Description</th>
</tr>
</thead>
<tbody>{rows}</tbody>
</table>
</body>
</html>
"""

output_file.write_text(html, encoding="utf-8")
print(f"HTML report generated: {output_file}")
