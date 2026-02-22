import pandas as pd
#DATA CLEANING ON EXCEL
# Load raw survey file
raw_file = 'SURVEY ON ROLE OF DOPAMINE IN THE BEHAVIOURAL PATTERNS OF ADULTS.xlsx' 
df = pd.read_excel(raw_file)

# Create a mapping dictionary for each question
q1_map = {
    '1-2 hours': 1,
    '3-5 hours': 2,
    '6-8 hours': 3,
    '9+ hours': 4
}
q2_map = {
    'Almost all of it (80%+ productive)': 4,
    'More than half (50–80% productive)': 3,
    'Less than half (20–50% productive)': 2,
    'Very little (less than 20% productive)': 1
}
q3_map = {
    'Very often (several times an hour)': 3, 
    'Often (several times a day)': 2,
    'Occasionally (a few times a day)':2,
    'Rarely or never': 1
}
q4_map = {
    'Shorter videos (reels)': 2,
    'Longer videos (7 to 15 minutes)': 1
}
q5_map = {
    'Yes, a lot—it affects my work and daily tasks.': 3,
    'Yes—it distracts me at times.': 2,
    'No, I don’t think it affects me.': 1
}
q6_map = {
    'Yes, I regret wasting too much time.': 3,
    'Sometimes, but I don’t think it’s a big problem.': 2,
    'No, I don’t regret it.': 1
}
q7_map = {
    'Yes,regularly': 3,
    'Yes,sometimes': 2,
    'No,never': 1
}
q8_map = {
    "It's too addictive" :4,
    'I feel like I’d miss out (FOMO)': 3,
    'I use it to relax after work': 2,
    'Lack of hobbies to make better use of time':2,
    'The constant need to keep checking for something ':2,
    "I don't realize how much time I spend.":2,
    "I don't feel the need to reduce it, as it's already low.": 1,
    'I dont see my screen time as a big issue yet, If I need to do something, I dont really think my screen time gets in the way.':1
}
q9_map = {
    'Yes, this should be a required subject': 3,
    'Maybe, but not as a main subject': 2,
    "No,I don't think that's a required subject ": 1
}
q10_map = {
    'Yes, it would help me a lot': 3,
    'Maybe, I’m not sure': 2,
    "No, I don’t think it would make a difference": 1
}

# Apply mappings to dataframe
df['Daily_screen_time'] = df['Daily_screen_time'].map(q1_map)
df['Prod_screen_time'] = df['Prod_screen_time'].map(q2_map)
df['Notif_check_freq'] = df['Notif_check_freq'].map(q3_map)
df['Video_preference'] = df['Video_preference'].map(q4_map)
df['Perceived_prod_reduction'] = df['Perceived_prod_reduction'].map(q5_map)
df['Screentime_regret'] = df['Screentime_regret'].map(q6_map)
df['Screen_limit'] = df['Screen_limit'].map(q7_map)
df['Screen_barrier'] = df['Screen_barrier'].map(q8_map)
df['Schools_impact'] = df['Schools_impact'].map(q9_map)
df['AI_coach_belief'] = df['AI_coach_belief'].map(q10_map)

#Checking for missing values
missing = df.isna().sum()
print("Missing values after coding:\n", missing)

#save the dataset if required
df.to_excel('cleaned_ROLE OF DOPAMINE IN THE BEHAVIOURAL PATTERNS OF ADULTS.xlsx', index=False)
print("Cleaned dataset saved as 'ROLE OF DOPAMINE IN THE BEHAVIOURAL PATTERNS OF ADULTS.xlsx'")