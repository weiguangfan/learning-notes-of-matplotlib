# %matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread('./stinkbug.png')
print(img)
# imgplot = plt.imshow(img)
lum_img = img[:, :, 0]
# plt.imshow(lum_img)
plt.imshow(lum_img, cmap="hot")
imgplot_2 = plt.imshow(lum_img)
imgplot_2.set_cmap('nipy_spectral')
plt.show()

