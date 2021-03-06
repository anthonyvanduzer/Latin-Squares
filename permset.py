from .permutation import *

class PermSet(set):
  ''' Provides functions for dealing with sets of Permutation objects '''

  def __repr__(self):
    return 'Set of %d permutations' % len(self)

  @staticmethod
  def all(n):
    ''' builds the set of all permutations of length n'''
    return PermSet(Permutation.listall(n))

  def show_all(self):
    return set.__repr__(self)

  def minimal_elements(self):
    B = list(self)
    B = sorted(B, key=len)
    C = B[:]
    n = len(B)
    for (i,b) in enumerate(B):
      if b not in C:
        continue
      for j in range(i+1,n):
        if B[j] not in C:
          continue
        if b.involved_in(B[j]):
          C.remove(B[j])
    return PermSet(C)

  def layer_down(self):
    S = PermSet()
    i = 1
    n = len(self)
    for P in self:
      if i % 10000 == 0:
        print('\t',i,'of',n,'. Now with',len(S),'.')
      S.update(P.shrink_by_one())
      i += 1
    return S

  def downset(self):
    bottom_edge = PermSet()
    bottom_edge.update(self)

    done = PermSet(bottom_edge)
    while len(bottom_edge) > 0:
      oldsize = len(done)
      next_layer = bottom_edge.layer_down()
      done.update(next_layer)
      del bottom_edge
      bottom_edge = next_layer
      del next_layer
      newsize = len(done)
      print('\t\tDownset currently has',newsize,'permutations, added',(newsize-oldsize),'in the last run.')
    return done

  def total_statistic(self, statistic):
    return sum([statistic(p) for p in self])

  def threepats(self):
    patnums = {'123' : 0, '132' : 0, '213' : 0, 
               '231' : 0, '312' : 0, '321' : 0}
    L = list(self)
    for p in L:
      n = len(p) 
      for i in range(n-2):
        for j in range(i+1,n-1):
          for k in range(j+1,n):
            std = Permutation.standardize([p[i], p[j], p[k]])
            patnums[''.join([str(x + 1) for x in std])] += 1
    return patnums

  def fourpats(self):
    patnums = {'1234' : 0, '1243' : 0, '1324' : 0, 
               '1342' : 0, '1423' : 0, '1432' : 0,
               '2134' : 0, '2143' : 0, '2314' : 0,
               '2341' : 0, '2413' : 0, '2431' : 0,
               '3124' : 0, '3142' : 0, '3214' : 0,
               '3241' : 0, '3412' : 0, '3421' : 0,
               '4123' : 0, '4132' : 0, '4213' : 0,
               '4231' : 0, '4312' : 0, '4321' : 0 }
    L = list(self)
    for p in L:
      n = len(p)
      for i in range(n-3):
        for j in range(i+1,n-2):
          for k in range(j+1,n-1):
            for m in range(k+1,n):
              std = Permutation.standardize([p[i], p[j], p[k], p[m]])
              patnums[''.join([str(x + 1) for x in std])] += 1
    return patnums
