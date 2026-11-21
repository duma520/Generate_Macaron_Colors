import colorsys
import math

def generate_macaron_colors(num_colors=360):
    """生成马卡龙色系的颜色"""
    colors = []
    for i in range(num_colors):
        # 使用HSV色彩空间生成柔和色调
        hue = i / num_colors  # 0-1范围
        saturation = 0.3 + 0.2 * math.sin(i * 0.1)  # 低饱和度波动
        value = 0.85 + 0.1 * math.cos(i * 0.05)  # 高亮度波动
        
        # 转换为RGB
        r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
        
        # 转换为0-255范围
        r = int(r * 255)
        g = int(g * 255)
        b = int(b * 255)
        
        # 转换为十六进制
        hex_color = "#{:02X}{:02X}{:02X}".format(r, g, b)
        
        colors.append((r, g, b, hex_color))
    
    return colors

def print_colors(colors):
    """按指定格式打印颜色，每行一个颜色"""
    for r, g, b, hex_color in colors:
        # 格式化为 QColor(r, g, g),  #HEX 形式，每个颜色单独一行
        print(f"QColor({r}, {g}, {b}),  {hex_color}")

if __name__ == "__main__":
    print("生成马卡龙色系颜色表：")
    macaron_colors = generate_macaron_colors(360)  # 生成360种颜色覆盖全色域
    print_colors(macaron_colors)
