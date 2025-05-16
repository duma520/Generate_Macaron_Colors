import colorsys
import math

# 统一参数配置
DEFAULT_NUM_COLORS = 360  # 默认生成180色
DEFAULT_SATURATION_BASE = 0.3  # 基础饱和度
DEFAULT_SATURATION_VARIATION = 0.2  # 饱和度波动范围
DEFAULT_VALUE_BASE = 0.85  # 基础亮度
DEFAULT_VALUE_VARIATION = 0.1  # 亮度波动范围
DEFAULT_HUE_OFFSET = 0.0  # 色相偏移（可选）

def generate_macaron_colors(
    num_colors=DEFAULT_NUM_COLORS,
    saturation_base=DEFAULT_SATURATION_BASE,
    saturation_variation=DEFAULT_SATURATION_VARIATION,
    value_base=DEFAULT_VALUE_BASE,
    value_variation=DEFAULT_VALUE_VARIATION,
    hue_offset=DEFAULT_HUE_OFFSET,
):
    """生成马卡龙色系的颜色
    
    Args:
        num_colors (int): 生成的颜色数量
        saturation_base (float): 基础饱和度 (0-1)
        saturation_variation (float): 饱和度波动范围 (0-1)
        value_base (float): 基础亮度 (0-1)
        value_variation (float): 亮度波动范围 (0-1)
        hue_offset (float): 色相偏移 (0-1)
    """
    colors = []
    for i in range(num_colors):
        # 计算色相（0-1范围）
        hue = (i / num_colors + hue_offset) % 1.0
        
        # 计算饱和度（基础值 + 波动）
        saturation = saturation_base + saturation_variation * math.sin(i * 0.1)
        saturation = max(0.0, min(1.0, saturation))  # 确保在0-1范围内
        
        # 计算亮度（基础值 + 波动）
        value = value_base + value_variation * math.cos(i * 0.05)
        value = max(0.0, min(1.0, value))  # 确保在0-1范围内
        
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
        print(f"QColor({r}, {g}, {b}),  {hex_color}")

if __name__ == "__main__":
    print("生成马卡龙色系颜色表：")
    macaron_colors = generate_macaron_colors(
        num_colors=360,  # 可调整颜色数量
        saturation_base=0.3,  # 可调整饱和度
        value_base=0.85,  # 可调整亮度
    )
    print_colors(macaron_colors)
