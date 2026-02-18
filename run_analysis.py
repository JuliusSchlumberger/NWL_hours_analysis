import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

from clustering_preset_clusters import preprocess, assign_to_predefined_cluster


# Detect language for each description
df = pd.read_excel('overzicht_sinds_2011.xlsx', converters={'date': str,'hours':float, 'description':str})

year_of_analysis = 2025

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Define initial labels

initial_clusters = {
'Lenen & Klusboete': ['klusboet', 'terug', 'lenen', 'leenuren','geleend', 'back to','lent from',
                      'lent','van', 'aan','naar','to ', 'from', 'correcti', 'uren', 'back',
                      'foutje', 'borrowed', 'return', 'geen', 'overdraag', 'corona'],
    'Klus': ['reparatie','radiator', 'klus', 'hout', 'hornbach', 'gamma', 'impregneren',
             'schilder','kast', 'verfen','balkon','vlonder',
             'muur', 'wc', 'kalk', 'werk', 'dak','solar', 'opknappen', 'toilet','bad', 'boden', 'keuk', 'vloer','laklaag','riol','Vernieuw',
             'plafond', 'plamur','plint','fix', 'verwijder', 'pank', 'plann','riool', 'repareren', 'scharnieren', 'douche', 'tool', 'boiler','trap',
             'vervange', 'trapp', 'verleggen','work', 'beamer', 'elektra', 'vegen', 'verf','verven', 'regenpijp', 'vervang','afmaken','kusco','Behang',
             'deur', 'schuren', 'opgeknapt', 'witten', 'tegels', 'aanrecht', 'kitten', 'terras',
             'bouwen', 'tegelen', 'geluidsisolatie', 'ontstoppen', 'shower','monteren',
             'metsel', 'gaten', 'kus'],
    'Tuin & Onderhoud': ['tuin', 'compost', 'gras', 'boom', 'boem', 'snoei','plant', 'bamboe',
                         'garden', 'kompost', 'bloem', 'hek', 'schaduwgazon', 'fence', 'vijver', 'schoonmaken', 'onkruid',
                                'onderhoud', 'zonne', 'renovatie', 'aaneemer', 'overdracht','hitte','hite', 'hitting', 'ventilatie',
                  'oplever', 'ohc','aanemer', 'mjop', 'aannemer', 'scheur', 'ketel', 'rapport', 'voeg','gevel', 'brug',
                  'kozijnen','omvormer', 'vocht', 'ramen', 'schilders', 'sleutel', 'brandblus',
                  'wasmachine', 'rook', 'blus', 'koof', 'slakken', 'knippen'
                                ],

    'Bestuur (incl uitkering)': ['bestuur', 'b.v.', 'best', 'roadmap', 'jaarrekening', 'penning', 'bv', 'cvt', 'Best',
                'inspectie','begrotin', 'factu', 'triodos','casco', 'reken','secretaris','notulen','stucen', 'statuten', 'kasco', 'kasko',
                'kasco','statuut', 'afrekening','leden', 'pennie', 'financiën', 'verzekering', 'jaaroverzicht', 'jaarverslag', 'eindafrekening', 'pm',
                'notaris', 'administratie', 'alv', 'voorzitter', 'ALV', 'ALB', 'b:', 'klasc',
                                 'HR','nieuwbrief', 'stukken',
                 'ukc', 'uot', 'uitkering', 'uitbeta', 'uitkeer', 'herfinanciering', 'betaalbarheid', 'betaalbaarheid', 'inflatie' ],
    'Feest & HKC & Eetcafe': ['eetcaf', 'hcc', 'koken', 'lunch', 'eten', 'café', 'cafe',
                              'ontbijt', 'flyer', 'fesst',
                              'feest', 'party', 'burendag', 'deco', 'inkoop', 'opbouw', 'boodschappen', 'opruimen', 'fest', 'afbouw','hkc', 'huiskamer', 'concert','Fringe' ],
    'NBC': ['nbc', 'gesprek','housemate', 'instemming', 'maand', 'instem','huisgenoot', 'borrel',
        'zoektocht', 'mediatie'],
    # 'vergadering': ['vergadering', 'overleg', 'alv', 'organiseren', 'zoektocht', 'regelen','meeting', 'visie', 'voorbereiden', 'bijeenkomst'],
    'Website': ['url', 'homepage', 'website', 'backup', 'bug', 'archief'],
}

df['processed_description'] = df['description'].astype(str).apply(preprocess)
df['predefined_cluster'] = df['processed_description'].apply(lambda x: assign_to_predefined_cluster(x, initial_clusters))

# Summarize data by category
category_summary = df.groupby('predefined_cluster')['hours'].sum()
print(category_summary)

# Summarize data by category and year
# Extract year from datum
df['year'] = df['Datum'].dt.year
# Summarize data by category and year
summary_by_year = df.groupby(['year', 'predefined_cluster'])['hours'].sum().unstack(fill_value=0)

# Determine the order of categories based on the total hours across all years
category_order = summary_by_year.sum().sort_values(ascending=False).index

# Reindex the DataFrame to ensure consistent category order
summary_by_year = summary_by_year[category_order]

# Store the results per year (example with dictionary)
summary_dict = summary_by_year.to_dict(orient='index')

# Plotting
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

print(summary_by_year)
# plot = summary_by_year.plot.pie(y=2024, figsize=(5, 5))
pie_data = summary_by_year[summary_by_year.index == year_of_analysis]
colors = [cm.get_cmap('tab20')(i) for i in range(len(pie_data.keys()))]

print(colors)
plt.figure(figsize=(8, 8))
print(pie_data.values[0])
plt.pie(pie_data.values[0], labels=pie_data.keys(), autopct='%1.1f%%', startangle=10,
        colors=colors
        )
plt.title(f"Nieuwelaanuren in {year_of_analysis} (totaal={int(np.sum(pie_data.values[0]))})")
plt.savefig(f'figures/Overview_{year_of_analysis}.png', dpi=300)

# Stacked bar plot
summary_by_year.plot(kind='bar', stacked=True, ax=ax1)
ax1.set_title('Stacked Bar Plot of Hours by Cluster and Year')
ax1.set_ylabel('Total Hours')
ax1.set_xlabel('Year')

# Line plot
summary_by_year.plot(kind='line', ax=ax2)
ax2.set_title('Line Plot of Hours by Cluster and Year')
ax2.set_ylabel('Total Hours')
ax2.set_xlabel('Year')

plt.tight_layout()


# Plotting
fig1, axs = plt.subplots(len(category_order), 1, figsize=(10, 1.5 * len(category_order)), sharex=True)
fig1.subplots_adjust(wspace=.6,hspace=.6, )
# Define a colormap
colors = cm.get_cmap('tab20', len(category_order))

# Plotting
num_categories = len(category_order)
num_cols = 2
num_rows = (num_categories + 1) // num_cols

fig1, axs = plt.subplots(num_rows, num_cols, figsize=(15, 2.5 * num_rows), sharex=True, sharey=True)

for i, category in enumerate(category_order):
    row = i // num_cols
    col = i % num_cols
    color = colors(i)
    axs[row, col].bar(summary_by_year.index, summary_by_year[category], color=color)
    axs[row, col].set_title(category)
    axs[row, col].set_ylim(-50, 1500)
    axs[row, col].grid()
    # axs[row, col].tick_params(axis='y', which='both', labelleft=False)

# Add a single y-axis label in the middle
fig1.text(0.04, 0.5, 'Spend hours per year [h]', va='center', rotation='vertical')

# Set x-axis label on the bottom row
for col in range(num_cols):
    axs[num_rows - 1, col].set_xlabel('Year')

# Adjust layout to make room for the y-axis label and titles
plt.tight_layout(rect=[0.05, 0, 1, 0.96])
# fig1.suptitle('Bar Plots of Hours by Year for Each Category', y=0.98)

fig1.suptitle(f'Development of vereningsuren between 2011 and {year_of_analysis}')
fig1.savefig(f'figures/Development_Per_Category_{year_of_analysis}.png', dpi=300)
# plt.grid()
# plt.tight_layout()
# plt.show()

# print(error)

# # Clustering
# # optimize_clusters(df, max_clusters=300)
# df_subset = df[df.predefined_cluster == 'Other']
# custom_stopwords = ['en', 'van', 'aan', 'the', 'kamer', 'met', 'de', 'zoeken']
# count_most_common(df_subset, custom_stopwords)
# # print(df_subset.sort_values('hours', ascending=False))
# print(df_subset.size)

