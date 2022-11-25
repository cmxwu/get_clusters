import numpy as np

def getallclusters(clustersid,frames):
    totclusters=[]
    positions=np.array(frames)
    for clusters in clustersid:
        eachcluster=[]
        for i in range(len(parser)):
            clusters_indices = parser.cluster_detail[clusters][i]
            tcp=[]
            for clusters_indices in clusters_indices:
    # find the positions of the cluster
                cluster = np.array(positions[i])[clusters_indices]
                tcp.append(cluster)
     
                 
            eachcluster.append(tcp)

        totclusters.append(eachcluster)
        
    return(totclusters)
    
