import sys
import unittest

sys.path.append('..')

from films.models import Studio, Country, Movie, Hall 


class testStudio(unittest.TestCase):
    def setUp(self):
       
        self.hall = Hall.objects.create(name="cinetest", city="villetest")
        self.country = Country.objects.create(name="france", code="FR")
        self.studio = Studio.objects.create(  
            name='Test',           
            country=self.country,
        )
            
        self.synopsis = "Dans l'ancien Kahndaq, Teth Adam a reçu les pouvoirs tout-puissants des dieux. Après avoir utilisé ces pouvoirs pour se venger, il a été emprisonné, devenant Black Adam. Près de 5 000 ans se sont écoulés et Black Adam est passé de l'homme au mythe puis à la"
        self.movie = Movie.objects.create(
            title = 'Film 1',     
            slug='test',
            director="realtest",
            synopsis=self.synopsis,
            actif=True,
            note=1,
            hall=self.hall,
            country=self.country,
            studio=self.studio            
        )
        
    def test_studio_create(self):
        self.assertEqual(self.studio.country.code, 'FR')
        
    def test_introduction(self):
        self.assertEqual(self.movie.get_introduction(100), self.synopsis[:100])
    
    def test_hall(self):
        self.assertEqual(self.hall.name, "cinetest")  
        
    def test_movie_count(self):
        self.assertEqual(self.studio.movie_count(), 1)
        
        Movie.objects.create(
            title = 'Film 2',     
            slug='test',
            director="realtest",
            synopsis=self.synopsis,
            actif=True,
            note=1,
            hall=self.hall,
            country=self.country,
            studio=self.studio            
        )
        Movie.objects.create(
            title = 'Film 3',     
            slug='test',
            director="realtest",
            synopsis=self.synopsis,
            actif=True,
            note=1,
            hall=self.hall,
            country=self.country,
            studio=self.studio            
        )
        self.assertEqual(self.studio.movie_count(), 3)
        
        studio2 = Studio.objects.create(  
            name='Test 2',           
            country=self.country,
        )
        Movie.objects.create(
            title = 'Film 4',     
            slug='test',
            director="realtest",
            synopsis=self.synopsis,
            actif=True,
            note=1,
            hall=self.hall,
            country=self.country,
            studio=studio2            
        )
        self.assertEqual(self.studio.movie_count(), 3)
        self.assertEqual(studio2.movie_count(), 1)

        last_movie = Movie.objects.last()
        self.assertEqual(last_movie.title, "Film 4")        
    