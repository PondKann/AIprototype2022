import argparse     #สำหรับ รับ imput จากภายนอก
import subprocess   #สำหรับ รัน terminal command

#import flask    #สำหรับ ทำ web app และ web service api


def print_other():
    print('Something else')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="test program")
    parser.add_argument(
        'm',
        type=int,
        help='value of M positional argument')
    
    parser.add_argument(
        '--x',
        type=int,
        help='value of x')
    
    parser.add_argument(
        '--yval',
        type=int,
        default=3,
        help='value of y')
    
    args = parser.parse_args()

    x = args.x
    y = args.yval
    print(f'M = {args.m}')
    print(f'calculate {x} * {y} = {x*y}')
    
    