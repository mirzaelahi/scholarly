#import unittest
import scholarly

search_query = scholarly.search_author('Mirza Elahi Virginia')
author = next(search_query).fill()
print(author)
author.plotCitation()
#
#class TestScholarly(unittest.TestCase):
#
#    def test_empty_author(self):
#        authors = [a for a in scholarly.search_author('')]
#        self.assertIs(len(authors), 0)
#
#    def test_empty_keyword(self):
#        ''' Returns 5 individuals with the name 'label' '''
#        authors = [a for a in scholarly.search_keyword('')]
#        self.assertEqual(len(authors), 5)
#
#    def test_empty_publication(self):
#        pubs = [p for p in scholarly.search_pubs_query('')]
#        self.assertIs(len(pubs), 0)
#
#    def test_get_cited_by(self):
#        pub = next(scholarly.search_pubs_query('frequency-domain analysis of haptic gratings cholewiak')).fill()
#        cites = [c for c in pub.get_citedby()]
#        self.assertEqual(len(cites), pub.citedby)
#
#    def test_keyword(self):
#        authors = [a.name for a in scholarly.search_keyword('3d_shape')]
#        self.assertIsNot(len(authors), 0)
#        self.assertIn(u'Steven A. Cholewiak', authors)
#
#    def test_multiple_authors(self):
#        ''' As of February 12, 2016, there are 26 'Zucker's, 3 pages worth '''
#        authors = [a.name for a in scholarly.search_author('Zucker')]
#        self.assertEqual(len(authors), 26)
#        self.assertIn(u'Steven W Zucker', authors)
#
#    def test_multiple_publications(self):
#        ''' As of February 12, 2016 there are 8 pubs that fit the search term'''
#        pubs = [p.bib['title'] for p in scholarly.search_pubs_query('cholewiak campbell robson')]
#        self.assertEqual(len(pubs), 8)
#        self.assertIn(u'A frequency-domain analysis of haptic gratings', pubs)
#
#    def test_publication_contents(self):
#        pub = next(scholarly.search_pubs_query('A frequency-domain analysis of haptic gratings')).fill()
#        self.assertTrue(pub.bib['author'] == u'Cholewiak, Steven A and Kim, Kwangtaek and Tan, Hong Z and Adelstein, Bernard D')
#        self.assertTrue(pub.bib['journal'] == u'Haptics, IEEE Transactions on')
#        self.assertTrue(pub.bib['number'] == u'1')
#        self.assertTrue(pub.bib['pages'] == u'3--14')
#        self.assertTrue(pub.bib['publisher'] == u'IEEE')
#        self.assertTrue(pub.bib['title'] == u'A frequency-domain analysis of haptic gratings')
#        self.assertTrue(pub.bib['url'] == u'http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5210096')
#        self.assertTrue(pub.bib['volume'] == u'3')
#        self.assertTrue(pub.bib['year'] == u'2010')
#
#    def test_single_author(self):
#        author = next(scholarly.search_author('Steven A. Cholewiak')).fill()
#        self.assertEqual(author.name, u'Steven A. Cholewiak')
#        self.assertEqual(author.id, u'4bahYMkAAAAJ')
#
#if __name__ == '__main__':
#    unittest.main()
#    
