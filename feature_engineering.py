import pandas as pd
#CLASSIFICATION AND SCORES
feature_engineering_file='cleaned_ROLE OF DOPAMINE IN THE BEHAVIOURAL PATTERNS OF ADULTS.xlsx'
df = pd.read_excel(feature_engineering_file)
# Calculate composite scores 
# Attention Fragmentation Score (AF)
Attention_Fragmentation_Score_col=['Daily_screen_time','Notif_check_freq','Video_preference','Perceived_prod_reduction','Screentime_regret']
df['Attention_Fragmentation_Score'] = df[Attention_Fragmentation_Score_col].mean(axis=1)

# Digital Overuse Index (DOI) 
Digital_Overuse_Index_col=['Daily_screen_time','Prod_screen_time','Notif_check_freq','Video_preference']
df['Digital_Overuse_Index'] = (5-df[Digital_Overuse_Index_col]).mean(axis=1)

# Intervention Readiness Score (IR)
Intervention_Readiness_Score_col=['Screen_limit','Screentime_regret','Schools_impact','AI_coach_belief']
df['Intervention_Readiness_Score'] = df[Intervention_Readiness_Score_col].mean(axis=1)

# Calculate overall descriptive statistics
desc_stats = df.describe()  # mean, std, min, max, etc.
print("Descriptive Statistics:\n", desc_stats)

#Classes
median_val_af = df['Attention_Fragmentation_Score'].median()
df['Attention_fragmentation_class'] = df['Attention_Fragmentation_Score'].apply(lambda x: 1 if x > median_val_af else 0)
print(df['Attention_fragmentation_class'].value_counts())
print(df['Attention_fragmentation_class'].value_counts(normalize=True))

median_val_doi = df['Digital_Overuse_Index'].median()
df['Digital_Overuse_Index_class'] = df['Digital_Overuse_Index'].apply(lambda x: 1 if x > median_val_doi else 0)
print(df['Digital_Overuse_Index_class'].value_counts())
print(df['Digital_Overuse_Index_class'].value_counts(normalize=True))

median_val_ir = df['Intervention_Readiness_Score'].median()
df['Intervention_Readiness_class'] = df['Intervention_Readiness_Score'].apply(lambda x: 1 if x > median_val_ir else 0)
print(df['Intervention_Readiness_class'].value_counts())
print(df['Intervention_Readiness_class'].value_counts(normalize=True))

#save the final dataset
df.to_excel('ml_ready_ROLE OF DOPAMINE IN THE BEHAVIOURAL PATTERNS OF ADULTS.xlsx', index=False)
print("ML-ready dataset saved as 'ml_ready_attention_fragmentation_data.xlsx'")

df.to_csv('ml_ready_ROLE OF DOPAMINE IN THE BEHAVIOURAL PATTERNS OF ADULTS.csv', index=False)
print("ML-ready csv dataset saved as 'ml_ready_attention_fragmentation_data.csv'")