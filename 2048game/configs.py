# 刘氏生
# 时间：2022/9/21 14:45
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Game 2048')


    # Form
    """
    screen_width: Width of the form
    screen_height: Height of the form
    """
    parser.add_argument('--screen_width', default=400)
    parser.add_argument('--screen_height', default=500)

    # Block
    """
    block_gap: Gap between two blocks
    block_size: Size of a block
    block_arc: Arc of a block
    """
    parser.add_argument('--block_gap', default=10)
    parser.add_argument('--block_size', default=86)
    parser.add_argument('--block_arc', default=10)

    return parser.parse_args()