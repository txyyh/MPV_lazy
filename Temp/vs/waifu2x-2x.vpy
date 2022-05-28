### waifu2x算法放大两倍（几乎不可能实时）

import vapoursynth as vs
from vapoursynth import core

input = video_in

denoise_lv = -1
scale_model = 2
GPU = 0
GPU_t = 2
# 降噪强度 -1=不降噪 // 0 // 1 // 2 // 3
# 放大模型 0=upconv_7_anime_style_art_rgb // 1=upconv_7_photo // 2=cunet
# 指定加速的显卡
# 显卡使用的线程

if input.width > 2560 and input.height > 2560 :
	raise Warning("源分辨率超过限制的范围，已临时禁用该脚本。")

cut1 = input.resize.Bilinear(format=vs.RGBS, matrix_in_s="709")
cut2 = core.w2xncnnvk.Waifu2x(clip=cut1, noise=denoise_lv, scale=2, model=scale_model, gpu_id=GPU, gpu_thread=GPU_t)
output = cut2.resize.Bilinear(format=vs.YUV444P16, matrix_s="709")
if input.get_frame(0).props._ColorRange == 0 :
	output = output.resize.Bilinear(range=1)

output.set_output()
