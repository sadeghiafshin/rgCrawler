# -*-
#
# @author: a sadeghi
# @email:  sadeghi.afshin@gmail.com
#
# @date:   2017-01-05
# -*-
from argparse import ArgumentParser

from pynion import Manager

from . import ScientificSociety


def get_options(*args, **kwds):
    parser = ArgumentParser()

    parser.add_argument("--authorID", dest="RGid",   action="store",
                        help="Query user ID")
    parser.add_argument("--jekyll",   dest="jekyll", action="store_true",
                        help="Format to Jekyll posts", default=False)

    return parser.parse_args()


if __name__ == "__main__":

    m = Manager()
    m.set_stdout()
    m.set_detail()
    m.set_overwrite()

    options = get_options()

    ss = ScientificSociety()
    ss.load()
    if ss.is_empty():
        ss.load_author(options.RGid)
        ss.load_contributions_of(options.RGid)
        ss.save()
    if options.jekyll:
        ss.authors2YAML('authors.yml')
        ss.contributions2MD(set(['dataset']))
