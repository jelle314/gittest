#!/usr/bin/python2.7 -tt

import sys

def hello(name):
  if name == 'jelle' or name == 'Jelle van dijk':
   print name, 'resolve the issue fast'
  else:
   print 'unknown'

def main():
  hello(sys.argv[1])

if __name__ == '__main__':
  main()



