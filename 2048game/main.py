# 刘氏生
# 时间：2022/9/21 14:45
import configs
from Game2048 import Game2048


def main(args):
    """
    screen_width: Width of the form
    screen_height: Height of the form
    block_gap: Gap between two blocks
    block_size: Size of a block
    """
    screen_width = args.screen_width
    screen_height = args.screen_height
    block_gap = args.block_gap
    block_size = args.block_size
    block_arc = args.block_arc

    game = Game2048(screen_width, screen_height, block_gap, block_size, block_arc)
    game.Form()


if __name__ == '__main__':
    args = configs.parse_args()
    main(args)
