ScreenStreamerManager
=====================
A python project, aim for using ScreenStreamer easily, it's a wxpython GUI application.

ScreenShots
-----------
1. Working like this
   
   ![Alt text](/doc/main_window.png?raw=true "main_window")
   
   ![Alt text](/doc/run_rtmp.png?raw=true "run_rtmp")

Run ScreenStreamerManager
-------------------------
1. Config configuration file
   
   ```yaml
   # LOG_LEVEL
   # a value of (NOSET, DEBUG, INFO, WARNING, ERROR, CRITICAL)
   # default NOSET
   log_level: DEBUG

   get_active_window: ./get_active_window # or ./get_active_window.exe

   rtmp: ./rtmp # or ./rtmp.exe
   rtmp_config_path: ./configuration.rtmp.yml

   mjpeg: ./mjpeg # or ./mjpeg.exe
   mjpeg_config_path: ./configuration.mjpeg.yml
   ```
2. Run it
   
   ```bash
   # first you need to copy ScreenStreamer's binary and configuration files to ./ScreenStreamerManager/app
   # copy rtmp or rtmp.exe to ./ScreenStreamerManager/app
   # copy mjpeg or mjpeg.exe to ./ScreenStreamerManager/app
   # copy configuration.rtmp.yml and configuration.mjpeg.yml to ./ScreenStreamerManager/app
   
   # enter the project root directory
   cd ./ScreenStreamerManager/app
   
   # run ScreenStreamerManager.py
   python ./ScreenStreamerManager.py
   
   # use ScreenStreamerManager, you can select a window to stream, but you must not change the window's size during streaming
   # click "Select" button, then click the window you want to stream, you can see the "Window ID" changed
   
   # the "Full Screen" Option is for setting stream full screen or just one window
   
   # run mjpeg service
   # choose "Execute" to mjpeg, then click "Run" button
   # use a web browser or other video player, open http://host:port/mjpeg

   # run rtmp service
   # choose "Execute" to rtmp, then click "Run" button
   # use a video player, open rtmp://host:port/live/screen
   
   # stop service
   # click "Stop" button
   ```


