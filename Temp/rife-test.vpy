### 性能警告：在mpv初始设置下，rtx-2070s-lp 补帧 H.264_720p(2000kbps)_24fps→48fps 勉强可行

import vapoursynth as vs
core = vs.core

input = video_in

cut1 = input.resize.Point(format=vs.RGBS, matrix_in_s="709")
cut2 = core.rife.RIFE(clip=cut1, model=9, multiplier=2, gpu_id=0, gpu_thread=2, tta=False, uhd=False, sc=False)
## model: 0 = rife ; 1 = rife-HD ; 2 = rife-UHD ; 3 = rife-anime ; 4 = rife-v2 ; 5 = rife-v2.3 ; 6 = rife-v2.4 ; 7 = rife-v3.0 ; 8 = rife-v3.1 ; 9 = rife-v4
## multiplier: 多倍帧数，只支持 rife-v4

output = cut2.resize.Point(format=vs.YUV444P16, matrix_s="709")

output.set_output()
