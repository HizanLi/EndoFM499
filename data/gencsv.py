from tqdm import tqdm
import csv
import glob

print("start")

datadir = 'pretrain'

# folders = ['CholecT45', 'Colonoscopic', 'Hyper-Kvasir', 'Kvasir-Capsule', 'LDPolypVideo', 'private']

# all_list =  []

mp4_files = glob.glob(f"{datadir}/**/*.mp4", recursive=True)

    

videos = []
for video in tqdm(mp4_files):
    videos.append([f'{video}', -1])

print(len(videos))

with open(f"{datadir}/train.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(videos)

print("end")
