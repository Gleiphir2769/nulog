#!/usr/bin/env python

import sys

sys.path.append('../')
from logparser.NuLog import NuLogParser
from logparser.utils import evaluator

import os
import pandas as pd

input_dir = '../logs/'  # The input directory of log file
output_dir = './AttentionParserResult/'  # The output directory of parsing results

benchmark_settings = {
    'BGL': {
        'log_file': 'BGL/BGL_2k.log',
        'log_format': '<Label> <Timestamp> <Date> <Node> <Time> <NodeRepeat> <Type> <Component> <Level> <Content>',
        'filters': '([ |:|\(|\)|=|,])|(core.)|(\.{2,})',
        'k': 50,
        'nr_epochs': 3,
        'num_samples': 0
    },
    'OpenStack': {
        'log_file': 'OpenStack/OpenStack_2k.log',
        'log_format': '<Logrecord> <Date> <Time> <Pid> <Level> <Component> \[<ADDR>\] <Content>',
        'filters': '([ |:|\(|\)|"|\{|\}|@|$|\[|\]|\||;])',
        'k': 5,
        'nr_epochs': 6,
        'num_samples': 0

    },

    'HDFS': {
        'log_file': 'HDFS/HDFS.log',
        'log_format': '<Date> <Time> <Pid> <Level> <Component>: <Content>',
        'filters': '(\s+blk_)|(:)|(\s)',
        'k': 15,
        'nr_epochs': 5,
        'num_samples': 0
    },
}

def parse_hdfs():
    dataset = "HDFS"
    setting = benchmark_settings.get(dataset)
    indir = os.path.join(input_dir, os.path.dirname(setting['log_file']))
    log_file = os.path.basename(setting['log_file'])
    parser = NuLogParser.LogParser(indir=indir, outdir=output_dir, filters=setting['filters'], k=setting['k'],
                                   log_format=setting['log_format'])
    parser.parse_for_USE_HDFS(log_file, nr_epochs=setting['nr_epochs'], num_samples=setting['num_samples'])
    print("parsing has been finished!!")

if __name__ == '__main__':
    parse_hdfs()