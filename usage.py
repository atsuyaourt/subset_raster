from pathlib import Path
from salem import wgs84

from subset import subset


in_nc = Path("/home/egozo/Research/workdir/data/nc/rcm/CNRM_RCP45_precip_2006_2099.nc")

# subset using shapefile, specify date

date_range = slice("2006", "2065")
shp_file = "../../../ipif2/input/shp/basins/abra/basin.shp"
subset_ds1 = subset(in_nc, date_range=date_range, shape=shp_file)


# subset using corners
subset_opt = dict(corners=((120.25, 16.75), (121.25, 18.25)), crs=wgs84)
subset_ds2 = subset(in_nc, **subset_opt)
