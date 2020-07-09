tar xvf golly-3.3-src.tar.gz 
cd ~/Downloads
tar xvf golly-3.3-src.tar.gz 
tar xvf wxWidgets-3.0.5.tar.bz2 
sudo apt-get install --yes libgtk2.0-dev
sudo apt-get install --yes mesa-common-dev
sudo apt-get install --yes freeglut3-dev
sudo apt-get install --yes python2.7-dev 
sudo apt-get install --yes mesa-common-dev
sudo apt-get install --yes freeglut3-dev
sudo apt-get install --yes python2.7-dev 
sudo apt-get install --yes mesa-common-dev
sudo apt-get install --yes freeglut3-dev
sudo apt-get install --yes python2.7-dev 


mkdir ~/Downloads/wxWidgets-3.0.5/build-gtk
cd ~/Downloads/wxWidgets-3.0.5/build-gtk
../configure --with-gtk --disable-shared --enable-unicode --with-opengl
make
sudo make install
 
 The installation of wxWidgets is finished.  On certain
 platforms (e.g. Linux) you'll now have to run ldconfig
 if you installed a shared library and also modify the
 LD_LIBRARY_PATH (or equivalent) environment variable.
 
 
sudo ldconfig
'
sudo ldconfig
cd ~/Downloads/golly-3.3-src/gui-wx
make -f makefile-gtk
make -f makefile-gtk bgolly
