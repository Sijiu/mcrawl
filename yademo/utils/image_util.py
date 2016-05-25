# coding=utf8

from cStringIO import StringIO
from lib.nosql.mongo_util import ServerFS
from yademo.utils.logger_util import logger
from PIL import Image


class ImageCover(object):
    def __init__(self, image):
        if image:
            self.__im = image

    def thumbnail(self, format_size):
        """
        不变形缩放，以图像中心为原点，按比例最大化截取图片，然后缩放
        """
        raw_size = self.__im.size
        if raw_size[0] < format_size[0] or raw_size[1] < format_size[1]:
            return None
        x_scale = raw_size[0]/format_size[0]
        y_scale = raw_size[1]/format_size[1]
        min_scale = min(x_scale, y_scale)
        s_x = (raw_size[0] - min_scale * format_size[0])/2
        s_y = (raw_size[1] - min_scale * format_size[1])/2
        box = (s_x, s_y, format_size[0]*min_scale+s_x, format_size[1]*min_scale+s_y)
        region_im = self.__im.crop(box)
        region_im.thumbnail(format_size, Image.ANTIALIAS)
        return region_im

    def resize(self, format_size):
        """
        变形缩放
        """
        img = self.__im.resize(format_size)
        return img

    def crop(self, box):
        """
        box是4个像素坐不值(left, upper, right, lower)
        """
        region = self.__im.crop(box)
        return region

'''
头像规格大小：50px*50px, 140px*140px, 200px*150px, 600px*450px
50px*50px 是采用拖动生成的小头像，用于在评论等地方显示
每次上传，生成四张图，分别名字为：
random_name = random(32)
sx_uid_random_name, sm_uid_random_name, md_uid_random_name, lg_uid_random_name
文件存储meta信息:
{'filename':'', 'contentType': 'valid mime-type', 'owner': '', 'group': '', 'title':'', 'description': '', 'comments':{}}
PIL save(fd, format)
format: BMP DCX EPS GIF IM JPEG PCD PCX PDF PNG PPM PSD TIFF XBM XPM
'''


class Avatar(object):
    """
    输入头像文件对象 --> fd
    """
    def __init__(self, fd=None, user=None, ext="jpeg"):
        self.raw_content = fd.read() if fd else None
        fd.seek(0)
        im = Image.open(fd) if fd else None
        self.raw_size = im.size
        self.ic = ImageCover(im) if im else None
        self.sfs = ServerFS()
        self.current_user = user
        self.fs_meta = {
            "contentType": "image/"+ext,
            "filename": "",
            "owner": self.current_user.mobile,
            "group": "avatar",
            "title": u"头像",
            "size": "",
            "kind": ""
        }

    def load(self, fd):
        self.ic = ImageCover(Image.open(fd))

    def save_gif(self):
        self.fs_meta["filename"] = self.current_user.get_avatar()
        self.fs_meta["size"] = "%spx*%spx" % self.raw_size
        self.fs_meta["kind"] = "sm"
        self.sfs.save(self.raw_content, **self.fs_meta)

    def save_avatar(self):
        """
        140px * 140px avatar image
        """
        if not self.ic:
            logger.error("the image ic is NoneObject, so confirm the image object.")
        format_size = (140, 140)
        self.fs_meta["filename"] = self.current_user.get_avatar()
        self.fs_meta["size"] = "140px*140px"
        self.fs_meta["kind"] = "sm"
        im = self.ic.resize(format_size)
        self.save(im)

    def save(self, im):
        fileObj = StringIO()
        im.convert("RGB").save(fileObj, 'JPEG')
        fileObj.seek(0)
        self.sfs.save(fileObj.read(), **self.fs_meta)
        fileObj.close()