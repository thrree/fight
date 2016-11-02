#coding=utf-8

class CFightMgr(object):
	team_a = None
	team_b = None
	rounds = None
	def __init__(self):
		pass


class CRound(object):
	index = 0
	def __init__(self, index):
		self.index = index
	def OnBegin(self):
		pass
	def OnEnd(self):
		pass