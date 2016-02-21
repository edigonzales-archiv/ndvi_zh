import java.util.logging.Logger

import geoscript.layer.GeoTIFF
import geoscript.render.*
import geoscript.layer.*
import geoscript.style.*

Logger logger = Logger.getLogger("createNDVI.groovy")
logger.setUseParentHandlers(true)

def startTime = Calendar.instance.time
def endTime
logger.info "Start: ${startTime}."

CIR = "/Users/stefan/Downloads/1091-231_cir_tiled.tif"

def tif = new GeoTIFF(new File(CIR))
def raster = tif.read()

MapAlgebra mapAlgebra = new MapAlgebra()

Raster output = mapAlgebra.calculate("dest = (src[0] - src[1]) / (src[0] + src[1]);", [src: raster])

File file = new File("/Users/stefan/Downloads/1091-231_ndvi.tif")
GeoTIFF geotiff = new GeoTIFF(file)
geotiff.write(output)

endTime = Calendar.instance.time
logger.info "Total elapsed time: ${(endTime.time - startTime.time)} ms"
logger.info "End: ${endTime}."
