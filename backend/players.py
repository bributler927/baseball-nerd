import pandas as pd

data = pd.read_csv('stats.csv')
df = pd.DataFrame(data)


four_fast_cols = [col for col in df.columns if 'ff_' in col]
change_cols = [col for col in df.columns if 'ch_' in col]
slider_cols = [col for col in df.columns if 'sl_' in col]
curve_cols = [col for col in df.columns if 'cu_' in col]
sinker_cols = [col for col in df.columns if 'si_' in col]
knuckle_cols = [col for col in df.columns if 'kn_' in col]
screw_cols = [col for col in df.columns if 'sc_' in col]
cutter_cols = [col for col in df.columns if 'fc_' in col]
split_cols = [col for col in df.columns if 'fs_' in col]
sweep_cols = [col for col in df.columns if 'st_' in col]
fork_cols = [col for col in df.columns if 'fo_' in col]
slurve_cols = [col for col in df.columns if 'sv_' in col]

pitch_cols = [change_cols, slider_cols, curve_cols, sinker_cols, knuckle_cols, 
              screw_cols, cutter_cols, split_cols, sweep_cols, fork_cols, slurve_cols]

fastball_cols = [col for col in df.columns if 'fastball_' in col]
offspeed_cols = [col for col in df.columns if 'offspeed_' in col]
breaking_cols = [col for col in df.columns if 'breaking_' in col]

pitch_cat_cols = [fastball_cols, offspeed_cols, breaking_cols]

pitcher_def_cols = [col for col in df.columns if 'p_' in col]
speed_cols = [col for col in df.columns if 'speed_' in col]

lefties = df[df['pitch_hand'] == "L"]
righties = df[df['pitch_hand'] == "R"]

wildness_cols = ["bb_percent", "out_zone_percent"]
hard_hit_cols = ["hard_hit_percent", "solidcontact_percent"]

for index, lefty in lefties.iterrows():
    print(lefty["last_name, first_name"] + ": " + lefty["pitch_hand"])
    