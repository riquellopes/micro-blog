# -*- encoding:utf-8 -*-
import sys
import time
import os

"""
	Code snippets:
	https://github.com/rodrigopinto/forkinrio/blob/master/deploy.py		
"""
	
def deploy(args):

	if not args[1:]:
		print "Error: No revision given. Cannot deploy"
		print "To deploy the current revision, use the following command:"
		print "$ python deploy.py 'git rev-parse HEAD'\n"
		sys.exit(1)

	rev = args[1]

	#Run testes
	if run_tests():
		#Create a stap based on local time
		stamp = time.strftime("%Y%m%d-%Hh%Mn%Ss")

		#Deploy
		os.system("appcfg.py  update blog")

		#Tag the deployed revision
		os.system("git tag -a deploy/%s %s -m ''" % (stamp, rev))
		os.system("git push --tags")
		
	else:
		print "Error: Tests are not passing. Cannot deploy."
		print "Solve problems and run command again.\n"
		
def run_tests():

	#This tip was used to solve problem on os.system
	#that return true when it is broke
	broke = os.system("nosetests -v --with-gae tests")

	if broke:
		return False
	else:
		return True

if __name__ == '__main__':
	deploy(sys.argv)
