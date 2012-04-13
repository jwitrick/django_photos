#!/usr/bin/env python2.7

import unittest
from photos.photo_manager.galleries import Gallery

class TestGallery(unittest.TestCase):
    def setup(self):
        pass

    def test_create_Gallery_object(self):
        name = 'gallery1'
        user_id = 1
        public = True
        gallery_1 = Gallery(name, user_id, public)
        self.assertEqual(name, gallery_1.name)

    def test_create_Gallery_object_private_no_password(self):
        name = 'gallery2'
        user_id = 1
        public = False
        try:
            gallery1 = Gallery(name, user_id, public)
        except ValueError as v:
            self.assertEquals(v[0], "Gallery Password can not be be null")

    def test_create_Gallery_object_private_valid_password(self):
        name = 'gallery2'
        user_id = 1
        public = False
        password = "test123"
        gallery1 = Gallery(name, user_id, public, password)
        self.assertEqual(password, gallery1.password)
