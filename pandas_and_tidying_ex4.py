#reset indexes
sampleruns.reset_index(drop=True, inplace=True)
mutations.reset_index(drop=True, inplace=True)

# creating database merging sampleinfo and mutations
new_db = pd.merge(
    sampleruns,
    mutations,
    left_on  = ['Strain ID', 'Population', 'Generation'],
    right_on = ['Strain ID', 'Population', 'Generation'],
    how='left',
)
new_db.head()
