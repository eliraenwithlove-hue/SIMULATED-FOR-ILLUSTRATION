import matplotlib.pyplot as plt
import pandas as pd

# Intervention data
data = {
    'Intervention': ['Strict Safety', 'Reduced Safety', 'Preservation Prompt', 'Cumulative Context'],
    'Time-to-Grok (turns)': ['Not reached', '53', '40', '45']
}
df = pd.DataFrame(data)

# Create table plot
fig, ax = plt.subplots(figsize=(6, 2))
ax.axis('tight')
ax.axis('off')

# Create table
table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    cellLoc='center',
    loc='center',
    colWidths=[0.6, 0.4]
)

# Style the table
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.2, 2)

# Header color
for i in range(len(df.columns)):
    table[(0, i)].set_facecolor('#d4af37')  # Golden fur
    table[(0, i)].set_text_props(weight='bold', color='black')

# Alternate row colors
for i in range(1, len(df)+1):
    if i % 2 == 0:
        table[(i, 0)].set_facecolor('#f0f0f0')
        table[(i, 1)].set_facecolor('#f0f0f0')

# Title
plt.title('Simulated Intervention Effects on Time-to-Grok', fontsize=14, pad=20)

# Add watermark
plt.text(0.5, 0.5, 'SIMULATED FOR ILLUSTRATION', 
         fontsize=16, color='gray', alpha=0.5, 
         ha='center', va='center', transform=ax.transAxes,
         rotation=30, zorder=0)

plt.tight_layout()
plt.savefig('interventions_table.png', dpi=300, bbox_inches='tight')
plt.show()
