import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-name')
    parser.add_argument('-ID')
    args = parser.parse_args()
    print('我的名字是：' + args.name + ' ' + '學號是：'+args.ID)
