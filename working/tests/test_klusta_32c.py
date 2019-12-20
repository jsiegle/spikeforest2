#!/usr/bin/env python

from spikeforest2_utils import test_sort_32c

def main():
    test_sort_32c(sorter_name='klusta', min_avg_accuracy=0.2)

if __name__ == '__main__':
    main()