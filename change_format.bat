f:
cd RWF-200_train_avi



for %%a in ('./*.avi') do ffmpeg -i "%%a" "../RWF-200_train_mp4/%%~na.mp4"
pause
