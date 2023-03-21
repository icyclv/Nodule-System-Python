import os

import vtkmodules.all as vtk
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import *


class QGlyphViewer(QFrame):
    def __init__(self, parent):
        super(QGlyphViewer,self).__init__(parent)

        # Make tha actual QtWidget a child so that it can be re parented
        self.interactor = QVTKRenderWindowInteractor(self)
        self.layout =QHBoxLayout()
        self.layout.addWidget( self.interactor)
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)
        # self.renWin = None
        self.ren = vtk.vtkRenderer()
        self.renWin = self.interactor.GetRenderWindow()
        self.renWin.AddRenderer(self.ren)
        self.iren = self.renWin.GetInteractor()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.renWin is not None:
            self.interactor.resize(self.width()-2, self.height()-2)
            self.renWin.SetSize(self.width()-2,  self.height()-2)

    def load(self, data):

        # The following reader is used to read a series of 2D slices (images)
        # that compose the volume. The slice dimensions are set, and the
        # pixel spacing. The data Endianness must also be specified. The reader
        # usese the FilePrefix in combination with the slice number to construct
        # filenames using the format FilePrefix.%d. (In this case the FilePrefix
        # is the root name of the file: quarter.)

        # v16 = vtk.vtkVolume16Reader()
        # v16.SetDataDimensions(64, 64)
        # v16.SetImageRange(1, 93)
        # v16.SetDataByteOrderToLittleEndian()
        # v16.SetFilePrefix("D:/dicom_image/headsq/quarter")
        # v16.SetDataSpacing(3.2, 3.2, 1.5)


        z, y, x = data.shape

        # segmentation = segmentation*255
        self.dataImporter = vtk.vtkImageImport()
        data = data.tostring()

        self.dataImporter.CopyImportVoidPointer(data, len(data))
        self.dataImporter.SetDataScalarTypeToUnsignedChar()
        self.dataImporter.SetNumberOfScalarComponents(1)
        self.dataImporter.SetDataExtent(0, x - 1, 0, y - 1, 0, z - 1)
        self.dataImporter.SetWholeExtent(0, x - 1, 0, y - 1, 0, z - 1)
        # v16 = vtk.vtkDICOMImageReader()
        # # v16.SetDirectoryName('D:/dicom_image/vtkDicomRender-master/sample')
        # v16.SetDirectoryName('D:/dicom_image/V')

        # The volume will be displayed by ray-cast alpha compositing.
        # A ray-cast mapper is needed to do the ray-casting, and a
        # compositing function is needed to do the compositing along the ray.
        volumeMapper = vtk.vtkGPUVolumeRayCastMapper()
        volumeMapper.SetInputConnection(self.dataImporter.GetOutputPort())
        volumeMapper.SetBlendModeToComposite()

        # The color transfer function maps voxel intensities to colors.
        # It is modality-specific, and often anatomy-specific as well.
        # The goal is to one color for flesh (between 500 and 1000)
        # and another color for bone (1150 and over).
        volumeColor = vtk.vtkColorTransferFunction()
        volumeColor.AddRGBPoint(0, 0.0, 0.0, 0.0)
        volumeColor.AddRGBPoint(120, 0.5, 0.3, 0.3)
        volumeColor.AddRGBPoint(170, 1.0, 0.3, 0.3)
        volumeColor.AddRGBPoint(254, 1.0, 0.3, 0.3)
        volumeColor.AddRGBPoint(255, 0, 1.0, 0)
        # volumeColor.AddRGBPoint(1500, 0.0, 0.0, 0.0)
        # The opacity transfer function is used to control the opacity
        # of different tissue types.
        volumeScalarOpacity = vtk.vtkPiecewiseFunction()
        volumeScalarOpacity.AddPoint(0, 0.00)
        volumeScalarOpacity.AddPoint(200, 0.1)
        volumeScalarOpacity.AddPoint(255, 0.05)
        # volumeScalarOpacity.AddPoint(100, 0.2)
        # volumeScalarOpacity.AddPoint(2000, 1.0)
        # The gradient opacity function is used to decrease the opacity
        # in the "flat" regions of the volume while maintaining the opacity
        # at the boundaries between tissue types.  The gradient is measured
        # as the amount by which the intensity changes over unit distance.
        # For most medical data, the unit distance is 1mm.
        # volumeGradientOpacity = vtk.vtkPiecewiseFunction()
        # volumeGradientOpacity.AddPoint(0,   0.0)
        # volumeGradientOpacity.AddPoint(90,  0.5)
        # volumeGradientOpacity.AddPoint(100, 1.0)

        # The VolumeProperty attaches the color and opacity functions to the
        # volume, and sets other volume properties.  The interpolation should
        # be set to linear to do a high-quality rendering.  The ShadeOn option
        # turns on directional lighting, which will usually enhance the
        # appearance of the volume and make it look more "3D".  However,
        # the quality of the shading depends on how accurately the gradient
        # of the volume can be calculated, and for noisy data the gradient
        # estimation will be very poor.  The impact of the shading can be
        # decreased by increasing the Ambient coefficient while decreasing
        # the Diffuse and Specular coefficient.  To increase the impact
        # of shading, decrease the Ambient and increase the Diffuse and Specular.
        volumeProperty = vtk.vtkVolumeProperty()
        volumeProperty.SetColor(volumeColor)
        volumeProperty.SetScalarOpacity(volumeScalarOpacity)
        # volumeProperty.SetGradientOpacity(volumeGradientOpacity)
        volumeProperty.SetInterpolationTypeToLinear()  # 用来设置体数据的插值方式
        volumeProperty.ShadeOn()
        volumeProperty.SetAmbient(0.9)  # 设置环境光的强度
        volumeProperty.SetDiffuse(0.9)  # 设置漫反射光的强度
        volumeProperty.SetSpecular(0.9)  # 设置镜面反射光的强度

        # The vtkVolume is a vtkProp3D (like a vtkActor) and controls the position
        # and orientation of the volume in world coordinates.
        volume = vtk.vtkVolume()
        volume.SetMapper(volumeMapper)
        volume.SetProperty(volumeProperty)

        # Finally, add the volume to the renderer
        self.ren.AddViewProp(volume)

        # Set up an initial view of the volume.  The focal point will be the
        # center of the volume, and the camera position will be 400mm to the
        # patient's left (which is our right).
        camera = self.ren.GetActiveCamera()
        c = volume.GetCenter()  # 获取体数据的中心点
        camera.SetFocalPoint(c[0], c[1], c[2])  # 设置相机焦点
        camera.SetPosition(c[0], c[1] + 600, c[2])  # 设置相机位置
        camera.SetViewUp(0, 0, 1)  #
        # q:如何设置相机在正前方
        # camera.SetFocalPoint(0, 0, 0)
        # camera.SetPosition(0, 0, 100)
        # camera.SetViewUp(0, 1, 0)

        # Increase the size of the render window



    def start(self):
        self.iren.Initialize()
        self.renWin.Render()
        self.iren.Start()
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:

        super().closeEvent(a0)
        self.interactor.Finalize()
        self.iren.TerminateApp()

        self.iren = None
        self.renWin = None
        self.interactor = None
        self.dataImporter = None


    def re_render(self,data):
        z, y, x = data.shape


        data = data.tostring()
        self.dataImporter.CopyImportVoidPointer(data, len(data))
        self.dataImporter.SetDataScalarTypeToUnsignedChar()
        self.dataImporter.SetNumberOfScalarComponents(1)
        self.dataImporter.SetDataExtent(0, x - 1, 0, y - 1, 0, z - 1)
        self.dataImporter.SetWholeExtent(0, x - 1, 0, y - 1, 0, z - 1)
        self.renWin.Render()



    # def start(self):
    #     self.interactor.Initialize()
    #     self.interactor.Start()