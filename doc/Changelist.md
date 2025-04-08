Documentation of what I did to integrate the shapefiles from online

TNC:
https://sites.google.com/view/caribbean-marine-maps
https://www.nature.org/en-us/newsroom/caribbean-marine-maps/

-	Brought in shapefiles for PR, DR, BVI, USVI. Extracted the first 5 raster values (Reef Crest, Fore Reef, Back Reef, Coral/Algae, and Spur and Groove Reef). According to Supplementary Material from Schill et al. (2021) in Remote Sensing. Some coral are in the Hardbottom Algae areas, as well as in Seagrass and Boulders and Rocks, however including these layers would have vastly overestimated shallow coral coverage since corals are generally quite sparse in these areas.
-	Methods:
o	Extract only raster values I want, to a new raster (https://gis.stackexchange.com/questions/49800/extracting-raster-values-and-creating-new-raster-in-qgis)
o	Polygonize that raster (now “reefs” are 1s and everything else is 0s)
o	Extract just the 1s to a new polygon (Extract by Attributes) (https://gis.stackexchange.com/questions/93237/eliminate-0-values-from-raster)

UNEP-WCMC, WorldFish Centre, WRI, TNC:
https://data.unep-wcmc.org/pdfs/1/WCMC_008_Global_Distribution_of_Coral_Reefs.pdf?1617121809
https://data.unep-wcmc.org/datasets/1


Insular shelf south of St Thomas and St John:
https://coastalscience.noaa.gov/project/habitat-map-insular-shelf-south-of-st-thomas-st-john/
https://www.fisheries.noaa.gov/inport/item/50381


Habitat drafts from Dan:
These appear to be a merged file from:
https://coastalscience.noaa.gov/project/habitat-mapping-us-virgin-islands/
https://products.coastalscience.noaa.gov/collections/benthic/e95usvi_pr/
https://products.coastalscience.noaa.gov/collections/benthic/e93stcroix/
https://coastalscience.noaa.gov/project/benthic-habitat-mapping-buck-island-reef-national-monument-st-croix/
https://data.doi.gov/dataset/digital-geologic-map-of-st-croix-and-buck-island-reef-national-monument-u-s-virgin-islands
-	and Hind Bank MCD map (unclear where this is housed online)

SDM from Katharine Egan:
Shared through email with me bfarme8@lsu.edu
NOAA BVI:
https://www.fisheries.noaa.gov/inport/item/40578
https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.nodc:0049955

PR:
https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.nodc:0217139
https://coastalscience.noaa.gov/news/2019-puerto-rico-coral-reef-monitoring-data-now-available/


DCRMP:
Want to use this?


STT+STX sampleframe extent:
272699.9688,348350.0313,1950849.75,2037350.0000 [EPSG:26920]


Lo-res net:
270099.9688,376375.1563,2005498.5672,2065950.0000 [EPSG:26920]

Net over BVI:
270100.0000,448700.0000,2005500.0000,2137950.0000 [EPSG:26920]

270100.0000,378100.0000,2005500.0000,2066700.0000 [EPSG:26920]

270100.0000,378100.0000,2065950.0000,2127150.0000 [EPSG:26920]

376700.0000,401900.0000,2005500.0000,2065950.0000 [EPSG:26920]


Update 26 Sep 2024:
Freaked out after MacOS Sequoia update broke some things in my spatial R set-up, so I uninstalled MacPorts and QGIS completely.
This may not have been smart.
Once it is (hopefully) sucessfully reinstalled on the new OS, which has some dependency issues with MacPorts (and MacPorts is required
to have access to the newest GDAL versions, so I can't avoid using it to properly load geodatabases), I may have to set up all my preferences
in QGIS again. This includes the plug-in that loaded stuff like NOAA /ESRI ocean basebamps, and also the benthic terrain modeler plug-in

Update 17 Oct 2024:
- Installing QGIS from the regular launcher for MacOS, after already having QGIS installed using MacPorts with latest updates and upgrades, seemed to somehow do the trick. QGIS 3.38.3-Grenoble is opening properly, with all latest GDAL, PROJ, and GEOS. Woo!
- Now I'm making sure I can load the geodatabase properly again
- Okay now I am realizing this didn't actually work and MacPorts never finished properly installing QGIS. Ugh. GDAL drivers are still out of date so loading the geodatabase is messed up again
- So I am working to install via MacPorts again - which may still be broken with MacOS Sequoia
- In the meantime, can try working with original Dan VI_Shapes bathy?


--->  Fetching archive for libvpx
--->  Attempting to fetch libvpx-1.13.1_0.darwin_24.arm64.tbz2 from https://packages.macports.org/libvpx
--->  Attempting to fetch libvpx-1.13.1_0.darwin_24.arm64.tbz2 from https://ywg.ca.packages.macports.org/mirror/macports/packages/libvpx
--->  Attempting to fetch libvpx-1.13.1_0.darwin_24.arm64.tbz2 from http://bos.us.packages.macports.org/libvpx
--->  Fetching distfiles for libvpx
--->  Verifying checksums for libvpx
--->  Extracting libvpx
--->  Applying patches to libvpx
--->  Configuring libvpx
Error: libvpx cannot be built while gtest is active.
Error: Please forcibly deactivate gtest, e.g. by running:
Error: 
Error:     sudo port -f deactivate gtest
Error: 
Error: Then try again. You can reactivate gtest again later.
Error: Failed to configure libvpx: gtest is active
Error: See /opt/local/var/macports/logs/_opt_local_var_macports_sources_rsync.macports.org_macports_release_tarballs_ports_multimedia_libvpx/libvpx/main.log for details.
Error: Follow https://guide.macports.org/#project.tickets if you believe there
is a bug.
Error: Processing of port qgis3 failed
--->  Some of the ports you installed have notes:
  hdf5 has the following notes:
    Mac users may need to set the environment variable "HDF5_USE_FILE_LOCKING"
    to the five-character string "FALSE" when accessing network mounted files.
    This is an application run-time setting, not a configure or build setting.
    Otherwise errors such as "unable to open file" or "HDF5 error" may be
    encountered.
  leveldb has the following notes:
    Before version 1.23 leveldb has RTTI and a lot of code uses typeid. Version
    1.23 disables RTTI which lead to broken things from plyvel to ceph. We
    re-enable RTTI by default, if you wish to disable it switch off rtti variant
    by:
       port upgrade --enforce-variants leveldb -rtti
    Before version 1.21 leveldb exposed helpers/memenv/memenv.h and some code
    uses it. Version 1.21 prevent that which lead to broken things like
    qtwebkit. We re-enable exposing memenv by default, if you wish to disable it
    switch off memenv variant by:
       port upgrade --enforce-variants leveldb -memenv
  openssl11 has the following notes:
    This is the last release of OpenSSL 1.1. No further public security updates
    will be provided. Please migrate to the openssl3 port.
  py311-pygments has the following notes:
    To make the Python 3.11 version of Pygments the one that is run when you
    execute the commands without a version suffix, e.g. 'pygmentize', run:
    
    port select --set pygments py311-pygments
  py312-fonttools has the following notes:
    To make the Python 3.12 version of fonttools the one that is run when you
    execute the commands without a version suffix, e.g. 'fonttools', run:
    
        sudo port select --set fonttools fonttools-312
  py312-pygments has the following notes:
    To make the Python 3.12 version of Pygments the one that is run when you
    execute the commands without a version suffix, e.g. 'pygmentize', run:
    
    port select --set pygments py312-pygments
  py312-virtualenv has the following notes:
    The executable is installed as '/opt/local/bin/virtualenv-3.12'. To symlink
    it to '/opt/local/bin/virtualenv', run:
    
        sudo port select --set virtualenv virtualenv312
  python27 has the following notes:
    To make this the default Python or Python 2 (i.e., the version run by the
    'python' or 'python2' commands), run one or both of:
    
        sudo port select --set python python27
        sudo port select --set python2 python27
benja@Benjamins-MacBook-Pro-4 ~ % 
