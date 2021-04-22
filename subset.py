from pathlib import Path
import salem


def subset(raster, date_range=None, **kwargs):
    """Returns the subset of a raster file

    Args:
        raster (str): Full path of the raster file
        date_range (list-like, optional): Date range. Defaults to None.

    Returns:
        an xarray Dataset
    """
    if isinstance(raster, str):
        raster = Path(raster)

    if not raster.is_file():
        return None

    in_ds = salem.open_xr_dataset(raster)

    if date_range is not None:
        in_ds = in_ds.sel(time=date_range)

    out_ds = in_ds.salem.subset(margin=1, **kwargs)
    out_ds = out_ds.salem.roi(all_touched=True, **kwargs)

    return out_ds
