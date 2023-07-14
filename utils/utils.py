import argparse
import os


def get_args():
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument(
        '-c', '--config',
        dest='config',
        metavar='C',
        default='None',
        help='The Configuration file')
    args = argparser.parse_args()
    return args




def create_dirs(dirs):
    """
    dirs - a list of directories to create if these directories are not found
    :param dirs:
    :return exit_code: 0:success -1:failed
    """
    try:
        for dir in dirs:
            if not os.path.exists(dir):
                os.makedirs(dir)
        return 0
    except Exception as err:
        print("Creating directories error: {0}".format(err))
        exit(-1)