import splitfolders

input_folder = 'famous_places2/'

splitfolders.ratio(input_folder, output="famous_places", seed=42, ratio=(0.7, 0.15, 0.15), group_prefix=None)

