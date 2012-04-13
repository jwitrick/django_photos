
import logging
import os
import glob
import sys
import shutil
from django.conf import settings

class GalleryHelper(object):
    """
    This class is designed to interact with the file system
    so that the front end does not need to worry about it.
    """

    def __init__(self, media_root):
        self.media_root = media_root

    def _create_gallery(self, cust_name, new_gallery):
        """
        This creates the new gallery. The variable needs to be relative path
        from the level below the cust level
        """
        if os.path.exists(os.path.join(self.media_root, cust_name, new_gallery)):
            return True
        cust_dir = os.path.join(self.media_root, cust_name)
        if not os.path.exists(cust_dir):
            os.makedirs(cust_dir)

        n_gallery_path = os.path.join(cust_dir, new_gallery)
        os.makedirs(n_gallery_path)
        return os.path.exists(n_gallery_path)

    def _delete_gallery(self, cust_name, gallery_name):
        """
        This deletes the directory and all its contents
        """
        gallery_path = os.path.join(self.media_root, cust_name, gallery_name)
        if os.path.exists(gallery_path):
            shutil.rmtree(gallery_path)

        return os.path.exists(gallery_path)

    def _get_all_files_in_gallery(self, cust_name, gallery_name):
        """
        This will return the names of each file in gallery
        """
        path = self.media_root
        files = glob.glob(os.path.join(path, cust_name, gallery_name, '*.*'))
        file_list = []
        for file in files:
            n_path = file.rsplit('media')[1]
            file_list.append(n_path)
        return file_list
    
    def _get_all_thumbnail_files_in_gallery(self, cust_name, gallery_name):
        """
        This will return the names of each thumbnail file in gallery
        """
        path = self.media_root
        files = glob.glob(os.path.join(path, cust_name, gallery_name, 'thumb.*.*'))
        file_list = []
        for file in files:
            n_path = file.rsplit('media')[1]
            file_list.append(n_path)
        return file_list
