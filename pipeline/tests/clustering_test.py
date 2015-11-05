#! /usr/bin/env python
""" 
Unit-test the package clustering
"""
from operator import itemgetter
import unittest
from stpipeline.common.clustering import countMolecularBarcodesClustersNaive, countMolecularBarcodesClustersHierarchical, countMolecularBarcodesPrefixtrie

class TestClustering(unittest.TestCase):
         
    @classmethod
    def setUpClass(self):
        self.molecular_barcodes1 = [('AAAAAAAAAA', []),
                                    ('AAAAAAAAAA', []),
                                    ('AAAAAAAAAA', []),
                                    ('AAAAAAAAAA', []),
                                    ('AAAAAAAAAA', []),
                                    ('AAAAAAAAAA', []),
                                    ('AAAAAAAABB', []),
                                    ('AAAAAAAABB', []),
                                    ('AAAAAAAABB', [])]
        
        self.molecular_barcodes2 = [('AAAAAAAAAA', []),
                                    ('AAAAAAAABB', []),
                                    ('AAAAAAAACC', []),
                                    ('AAAAAADDDD', []),
                                    ('AAAAAAAAAA', []),
                                    ('AAAAAAAAAA', []),
                                    ('ZZZZAABBBB', []),
                                    ('AAAAAABBBB', []),
                                    ('AAAAAABBBB', [])]
        
        self.molecular_barcodes3 = [('AAAA', []),
                                    ('DAAA', []),
                                    ('ABAA', []),
                                    ('ABBA', []),
                                    ('ABBB', []),
                                    ('BBBB', []),
                                    ('CCCC', []),
                                    ('ACCC', [])]
        
    def test_naive_clustering(self):
        clusters = countMolecularBarcodesClustersNaive(self.molecular_barcodes1, 3, 0, 10, 2)
        # should be one cluster of 10 reads so only a random one is returned
        self.assertTrue(len(clusters) == 1)
        
        clusters = countMolecularBarcodesClustersNaive(self.molecular_barcodes1, 3, 0, 10, 10)
        # should not return any cluster so it will return the 9 reads
        self.assertTrue(len(clusters) == 9)

        clusters = countMolecularBarcodesClustersNaive(self.molecular_barcodes2, 3, 0, 10, 2)
        # should make four clusters
        self.assertTrue(len(clusters) == 4)
        
        clusters = countMolecularBarcodesClustersNaive(self.molecular_barcodes2, 1, 0, 10, 2)
        # should make siz clusters
        self.assertTrue(len(clusters) == 6)
        
        clusters = countMolecularBarcodesClustersNaive(self.molecular_barcodes2, 5, 0, 10, 2)
        # should make two clusters
        self.assertTrue(len(clusters) == 2)
        
        clusters = countMolecularBarcodesClustersNaive(self.molecular_barcodes3, 1, 0, 4, 2)
        # should make 5 clusters
        self.assertTrue(len(clusters) == 5)

    def test_prefix_tree_clustering(self):
        clusters = countMolecularBarcodesPrefixtrie(self.molecular_barcodes1, 3, 0, 10, 2)
        # should be one cluster of 10 reads so only a random one is returned
        self.assertTrue(len(clusters) == 1)
          
        clusters = countMolecularBarcodesPrefixtrie(self.molecular_barcodes1, 3, 0, 10, 10)
        # should not return any cluster so it will return the 9 reads
        self.assertTrue(len(clusters) == 9)
     
        clusters = countMolecularBarcodesPrefixtrie(self.molecular_barcodes2, 3, 0, 10, 2)
        # should make two cluster, one of 5 reads and one of 2 so the output should have 4 reads
        self.assertTrue(len(clusters) == 4)
          
        clusters = countMolecularBarcodesPrefixtrie(self.molecular_barcodes2, 1, 0, 10, 2)
        # should make two clusters one of 3 reads and another one of 2 so the output should have 6 reads
        self.assertTrue(len(clusters) == 5)
          
        clusters = countMolecularBarcodesPrefixtrie(self.molecular_barcodes2, 5, 0, 10, 2)
        # should make one cluster of 8 reads so the output should have 2 reads
        self.assertTrue(len(clusters) == 2)
          
        clusters = countMolecularBarcodesPrefixtrie(self.molecular_barcodes3, 1, 0, 4, 2)
        # should make one cluster of 4 reads so the output should have 2 reads
        self.assertTrue(len(clusters) == 5)
        
    def test_hierarchical_clustering(self):
        clusters = countMolecularBarcodesClustersHierarchical(self.molecular_barcodes1, 3, 0, 10, 2)
        # should be one cluster 
        self.assertTrue(len(clusters) == 1)
        
        clusters = countMolecularBarcodesClustersHierarchical(self.molecular_barcodes1, 3, 0, 10, 10)
        # should not return any cluster so it will return 9
        self.assertTrue(len(clusters) == 9)

        clusters = countMolecularBarcodesClustersHierarchical(self.molecular_barcodes2, 3, 0, 10, 2)
        # should make four clusters in complete mode or 3 in single mode
        self.assertTrue(len(clusters) == 3)
        
        clusters = countMolecularBarcodesClustersHierarchical(self.molecular_barcodes2, 1, 0, 10, 2)
        # should make six clusters
        self.assertTrue(len(clusters) == 6)
        
        clusters = countMolecularBarcodesClustersHierarchical(self.molecular_barcodes2, 5, 0, 10, 2)
        # should make two clusters
        self.assertTrue(len(clusters) == 1)
        
        clusters = countMolecularBarcodesClustersHierarchical(self.molecular_barcodes3, 1, 0, 4, 2)
        # should make four clusters in complete mode or 2 in single mode
        self.assertTrue(len(clusters) == 2)
          
if __name__ == '__main__':
    unittest.main()        
