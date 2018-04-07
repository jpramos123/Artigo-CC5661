import numpy
import data_generator
import math

def identifyCluster(kmeansClusters, databaseClusters):
	databaseClusterAmount = len(databaseClusters)
	kmeansClusterAmount = len(kmeansClusters)
	features = len(kmeansClusters[0])
	databaseClusterIDs = [1, 2, 3, 4, 5]

	for dbClusterIdx in range(databaseClusterAmount):
		correspondingKmCluster = None
		minor = 0
		squareDistance = 0
		for kmClusterIdx in range(kmeansClusterAmount):
			squareDistance = 0
			for featureIdx in range(features):
				squareDistance += (kmeansClusters[kmClusterIdx][featureIdx] - databaseClusters[dbClusterIdx][featureIdx])**2
			distance = math.sqrt(squareDistance)
			if (kmClusterIdx != 0):
				if(distance < minor):
					minor = distance
					correspondingKmCluster = kmClusterIdx
			else:
				minor = distance
				correspondingKmCluster = kmClusterIdx
		databaseClusterIDs[dbClusterIdx] = correspondingKmCluster + 1

	return databaseClusterIDs