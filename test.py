#!/usr/bin/python2.7 -tt

import sys

def hello(name):
  if name == 'jelle' or name == 'Close your issue properly':
   print name, 'edadan'
  else:
   print 'unknown'

def main():
  hello(sys.argv[1])

if __name__ == '__main__':
  main()



