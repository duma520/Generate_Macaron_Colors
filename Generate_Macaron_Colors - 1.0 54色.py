import colorsys

def generate_macaron_colors(num_colors=60, saturation_range=(0.15, 0.4), lightness_range=(0.85, 0.93)):
    """
    生成全色域马卡龙色
    :param num_colors: 生成颜色数量
    :param saturation_range: 饱和度范围 (0.15-0.4)
    :param lightness_range: 明度范围 (0.85-0.93)
    :return: 包含QColor和HEX的列表
    """
    colors = []
    for i in range(num_colors):
        # 均匀分布色相（0-360°）
        hue = i * (360 / num_colors)  
        
        # 在范围内随机微调饱和度和明度（避免机械感）
        sat = saturation_range[0] + (i % 5) * 0.05
        light = lightness_range[0] + (i % 3) * 0.03
        
        # HSL转RGB
        rgb = colorsys.hls_to_rgb(hue/360, light, sat)
        r, g, b = [int(x * 255) for x in rgb]
        
        # 转换为HEX
        hex_color = "#{:02X}{:02X}{:02X}".format(r, g, b)
        
        colors.append({
            "qcolor": f"QColor({r}, {g}, {b})",
            "hex": hex_color,
            "hsl": f"HSL({int(hue)}, {int(sat*100)}%, {int(light*100)}%)"
        })
    return colors

# 生成54色（6色相×9变体）
macaron_colors = generate_macaron_colors(54)

# 打印前10个颜色示例
for i, color in enumerate(macaron_colors):
    # print(f"{i+1}. {color['qcolor']}  {color['hex']}  {color['hsl']}")
    print(f"{color['qcolor']}  {color['hex']}  {color['hsl']}")

# 输出全部颜色到文件
with open("macaron_colors.txt", "w") as f:
    for color in macaron_colors:
        f.write(f"{color['qcolor']},  {color['hex']}\n")
