from django.test import TestCase
from .models import Images, Categories, Locations

# Create your tests here.
class TestImages(TestCase):
    '''
    test class for Images model
    '''
    def setUp(self):
        '''
        test method to create Image instances before every test
        '''
        self.new_category = Categories(name='art')
        self.new_category.save_category()
        
        self.new_location = Locations(town='Cali', country='Colombia')
        self.new_location.save_location()
        
        self.new_photo = Images(image_link='images/martin.jpeg', title='Martin Luther', description='cicil rights leader', category=self.new_category, location=self.new_location)
        self.new_photo.save_image()
        self.another_photo = Images(image_link='images/vik.jpg', title='siderra', description='chess player', category=self.new_category, location=self.new_location)
        self.another_photo.save_image()

    def tearDown(self):
        '''
        test method to delete Image instances after each test is run
        '''
        Categories.objects.all().delete()
        Locations.objects.all().delete()
        Images.objects.all().delete()

    def test_instances(self):
        '''
        test method to assert instances created during setUp
        '''
        self.assertTrue(isinstance(self.new_photo,Images))
        self.assertTrue(isinstance(self.new_category, Categories))
        self.assertTrue(isinstance(self.new_location, Locations))

    def test_save_image(self):
        '''
        test method to ensure an Image instance has been correctly saved
        '''
        self.assertTrue(len(Images.objects.all()) == 2)

    def test_delete_image(self):
        '''
        test method to ensure an Image instance has been correctly deleted
        '''
        self.new_photo.delete_image()
        self.assertTrue(len(Images.objects.all()) == 1)    

    def test_get_all(self):
        '''
        test method to ensure all instances of Image class have been retrieved
        '''
        photos = Images.get_all()    


class TestCategory(TestCase):
    '''
    test class for Categories model
    '''
    def setUp(self):
        '''
        test method to create Category instances called before all tests
        '''
        self.new_category = Categories(name='Nature')
        self.new_category.save_category()

    def tearDown(self):
        '''
        test method to delete Category instances after each test is run
        '''
        Categories.objects.all().delete()

    def test_save_category(self):
        '''
        test method to ensure a Category instance is saved
        '''
        self.assertTrue(len(Categories.objects.all()) == 1)     

    def test_delete_category(self):
        '''
        test method to ensure a Category instance is deleted
        '''
        self.new_category.save_category()
        self.new_category.delete_category()
        self.assertTrue(len(Categories.objects.all()) == 0)    

class TestLocation(TestCase):
    '''
    test class for Locations model
    '''
    def setUp(self):
        '''
        test method to create Location instances called before all tests
        '''
        self.new_location = Locations(city='tehran', country='Iran')
        self.new_location.save_location()

    def test_save_location(self):
        '''
        test method to ensure a Location instance has been correctly saved
        '''
        self.assertTrue(len(Locations.objects.all()) == 1)     

    def test_delete_location(self):
        '''
        test method to ensure a Location instance is deleted
        '''
        self.new_location.save_location()
        self.new_location.delete_location()
        self.assertTrue(len(Locations.objects.all()) == 0)