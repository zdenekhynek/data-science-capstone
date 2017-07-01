import argparse

import pandas as pd


parser = argparse.ArgumentParser(description='')
parser.add_argument('--file', type=str, help='Path to a file')
args = parser.parse_args()

df = pd.read_csv(args.file)
df.to_json(args.file + '.json', orient='index')
