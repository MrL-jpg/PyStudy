import cv2
import numpy
import time

class CaptureManager(object):
    def __init__(self,capture,previewWindowMannager = None,shouldMirrorPreview = False):
        self.previewWindowManager = previewWindowMannager
        self.shouldMirrorPreview = shouldMirrorPreview
        self._capture = capture
        self._channel = 0
        self._enteredFrame = False
        self._frame = None
        self._imgFilename = None
        self._videoFilename = None
        self._videoEncodoing = None
        self._videoWriter = None
        self._startTime = None
        self._frameElapaed = 0
        self._fpsEstimate = None
    @property
    def channel(self):
        return self._channel
    @channel.setter
    def channel(self,value):
        if value != self._channel:
            self._channel = value
            self._frame = None
    @property
    def frame(self):
        if self._enteredFrame and self.frame is None:
            _, self.frame = self._capture.retrieve(self._frame,self.channel)
            return self.frame
    