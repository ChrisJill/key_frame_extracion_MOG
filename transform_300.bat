f:
cd DATASET
cd hockyfights_120
for %%a in ("./*.mp4") do ffmpeg -i "%%a" -vf scale=300:300,setsar=1:1 "f:/DATASET/hockyfights_120_300/%%~na.mp4"
pause
